from delta.tables import DeltaTable
from notebookutils import mssparkutils
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType, TimestampType, BooleanType, ShortType
from pyspark.sql import functions as F
from pyspark.sql.utils import AnalysisException
from opencensus.ext.azure.log_exporter import AzureLogHandler, logging
import pandas as pd
import sys
import re
import json
import datetime
import random
import io

logger = logging.getLogger('OEA')

class OEA:
    def __init__(self, storage_account='', instrumentation_key='', salt='', logging_level=logging.DEBUG):
        if storage_account:
            self.storage_account = storage_account
        else:
            oea_id = mssparkutils.env.getWorkspaceName()[8:] # extracts the OEA id for this OEA instance from the synapse workspace name (based on OEA naming convention)
            self.storage_account = 'stoea' + oea_id # sets the name of the storage account based on OEA naming convention
        self.serverless_sql_endpoint = mssparkutils.env.getWorkspaceName() + '-ondemand.sql.azuresynapse.net'
        self._initialize_logger(instrumentation_key, logging_level)
        self.salt = salt
        self.stage1np = 'abfss://stage1np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage2np = 'abfss://stage2np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage2p = 'abfss://stage2p@' + self.storage_account + '.dfs.core.windows.net'
        self.stage3np = 'abfss://stage3np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage3p = 'abfss://stage3p@' + self.storage_account + '.dfs.core.windows.net'
        self.framework_path = 'abfss://oea-framework@' + self.storage_account + '.dfs.core.windows.net'
        self.registered_modules = {}

        logger.debug("OEA initialized.")

    def path(self, container_name, directory_path=None):
        if directory_path:
            return f'abfss://{container_name}@{self.storage_account}.dfs.core.windows.net/{directory_path}'
        else:
            return f'abfss://{container_name}@{self.storage_account}.dfs.core.windows.net'            

    def _initialize_logger(self, instrumentation_key, logging_level):
        logging.lastResort = None
        # the logger will print an error like "ValueError: I/O operation on closed file" because we're trying to have log messages also print to stdout
        # and apparently this causes issues on some of the spark executor nodes. The bottom line is that we don't want these logging errors to get printed in the notebook output.
        logging.raiseExceptions = False
        logger.setLevel(logging_level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if instrumentation_key:
            # Setup logging to go to app insights (more info here: https://github.com/balakreshnan/Samples2021/blob/main/Synapseworkspace/opencensuslog.md#azure-synapse-spark-logs-runtime-errors-to-application-insights)
            self.logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=' + instrumentation_key))


    def load(self, folder, table, stage=None, data_format='delta'):
        """ Loads a dataframe based on the path specified in the given args """
        if stage is None: stage = self.stage2p
        path = f"{stage}/{folder}/{table}"
        try:
            df = spark.read.load(f"{stage}/{folder}/{table}", format=data_format)
            return df        
        except AnalysisException as e:
            raise ValueError("Failed to load. Are you sure you have the right path?\nMore info below:\n" + str(e))

    def load_from_stage1(self, path_and_filename, data_format='csv'):
        """ Loads a dataframe with data from stage1, based on the path specified in the given args """
        path = f"{self.stage1np}/{path_and_filename}"
        df = spark.read.load(path, format=data_format)
        return df        

    def load_sample_from_csv_file(self, path_and_filename, header=True, stage=None):
        """ Loads a sample from the specified csv file and returns a pandas dataframe.
            Ex: print(load_sample_from_csv_file('/student_data/students.csv'))
        """
        if stage is None: stage = self.stage1np
        csv_str = mssparkutils.fs.head(f"{stage}/{path_and_filename}") # https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/microsoft-spark-utilities?pivots=programming-language-python#preview-file-content
        complete_lines = re.match(r".*\n", csv_str, re.DOTALL).group(0)
        if header: header = 0 # for info on why this is needed: https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.read_csv.html
        else: header = None
        pdf = pd.read_csv(io.StringIO(complete_lines), sep=',', header=header)
        return pdf

    def print_stage(self, path):
        """ Prints out the highlevel contents of the specified stage."""
        msg = path + "\n"
        folders = self.get_folders(path)
        for folder_name in folders:
            entities = self.get_folders(path + '/' + folder_name)
            msg += f"{folder_name}: {entities}\n"
        print(msg)            

    def fix_column_names(self, df):
        """ Fix column names to satisfy the Parquet naming requirements by substituting invalid characters with an underscore. """
        df_with_valid_column_names = df.select([F.col(col).alias(re.sub("[ ,;{}()\n\t=]+", "_", col)) for col in df.columns])
        return df_with_valid_column_names

    def to_spark_schema(self, schema):#: list[list[str]]):
        """ Creates a spark schema from a schema specified in the OEA schema format. 
            Example:
            schemas['Person'] = [['Id','string','hash'],
                                    ['CreateDate','timestamp','no-op'],
                                    ['LastModifiedDate','timestamp','no-op']]
            to_spark_schema(schemas['Person'])
        """
        fields = []
        for col_name, dtype, op in schema:
            fields.append(StructField(col_name, globals()[dtype.lower().capitalize() + "Type"](), True))
        spark_schema = StructType(fields)
        return spark_schema

    def ingest_incremental_csv_data(self, source_system, tablename, schema, partition_by, primary_key='id', has_header=True):
        """ Processes incremental batch data from stage1 into stage2 """
        source_path = f'{self.stage1np}/{source_system}/{tablename}'
        p_destination_path = f'{self.stage2p}/{source_system}/{tablename}_pseudo'
        np_destination_path = f'{self.stage2np}/{source_system}/{tablename}_lookup'
        logger.info(f'Processing incremental data from: {source_path} and writing out to: {p_destination_path}')

        spark_schema = self.to_spark_schema(schema)
        if has_header: header_flag = 'true'
        else: header_flag = 'false'
        df = spark.readStream.csv(source_path + '/**/*.csv', header=header_flag, schema=spark_schema)
        #df = spark.read.csv(source_path + '/**/*.csv', header=header_flag, schema=spark_schema)
        #display(df)
        df = df.dropDuplicates([primary_key])
        df_pseudo, df_lookup = self.pseudonymize(df, schema)

        if len(df_pseudo.columns) == 0:
            logger.info('No data to be written to stage2p')
        else:        
            query = df_pseudo.writeStream.format("delta").outputMode("append").trigger(once=True).option("checkpointLocation", source_path + '/_checkpoints_p').partitionBy(partition_by)
            query = query.start(p_destination_path)
            query.awaitTermination()   # block until query is terminated, with stop() or with error; A StreamingQueryException will be thrown if an exception occurs.
            logger.info(query.lastProgress)

        if len(df_lookup.columns) == 0:
            logger.info('No data to be written to stage2np')
        else:
            query2 = df_lookup.writeStream.format("delta").outputMode("append").trigger(once=True).option("checkpointLocation", source_path + '/_checkpoints_np').partitionBy(partition_by)
            query2 = query2.start(np_destination_path)
            query2.awaitTermination()   # block until query is terminated, with stop() or with error; A StreamingQueryException will be thrown if an exception occurs.
            logger.info(query2.lastProgress)        

    def pseudonymize(self, df, schema): #: list[list[str]]):
        """ Performs pseudonymization of the given dataframe based on the provided schema.
            For example, if the given df is for an entity called person, 
            2 dataframes will be returned, one called person that has hashed ids and masked fields, 
            and one called person_lookup that contains the original person_id, person_id_pseudo,
            and the non-masked values for columns marked to be masked."""
        
        df_pseudo = df_lookup = df

        for col_name, dtype, op in schema:
            if op == "hash-no-lookup" or op == "hnl":
                # This means that the lookup can be performed against a different table so no lookup is needed.
                df_pseudo = df_pseudo.withColumn(col_name, F.sha2(F.concat(F.col(col_name), F.lit(self.salt)), 256)).withColumnRenamed(col_name, col_name + "_pseudonym")
                df_lookup = df_lookup.drop(col_name)           
            elif op == "hash" or op == 'h':
                df_pseudo = df_pseudo.withColumn(col_name, F.sha2(F.concat(F.col(col_name), F.lit(self.salt)), 256)).withColumnRenamed(col_name, col_name + "_pseudonym")
                df_lookup = df_lookup.withColumn(col_name + "_pseudonym", F.sha2(F.concat(F.col(col_name), F.lit(self.salt)), 256))
            elif op == "mask" or op == 'm':
                df_pseudo = df_pseudo.withColumn(col_name, F.lit('*'))
            elif op == "partition-by":
                pass # make no changes for this column so that it will be in both dataframes and can be used for partitioning
            elif op == "no-op" or op == 'x':
                df_lookup = df_lookup.drop(col_name)

        df_pseudo = self.fix_column_names(df_pseudo)
        df_lookup = self.fix_column_names(df_lookup)

        return (df_pseudo, df_lookup)

    # Returns true if the path exists
    def path_exists(self, path):
        tableExists = False
        try:
            items = mssparkutils.fs.ls(path)
            tableExists = True
        except Exception as e:
            # This Exception comes as a generic Py4JJavaError that occurs when the path specified is not found.
            pass
        return tableExists

    def ls(self, path):
        folders = []
        files = []
        try:
            items = mssparkutils.fs.ls(path)
            for item in items:
                if item.isFile:
                    files.append(item.name)
                elif item.isDir:
                    folders.append(item.name)
        except Exception as e:
            logger.warning("[OEA] Could not peform ls on specified path: " + path + "\nThis may be because the path does not exist.")
        return (folders, files)

    def print_stage(self, path):
        print(path)
        folders = self.get_folders(path)
        for folder_name in folders:
            entities = self.get_folders(path + '/' + folder_name)
            print(f"{folder_name}: {entities}")

    # Return the list of folders found in the given path.
    def get_folders(self, path):
        dirs = []
        try:
            items = mssparkutils.fs.ls(path)
            for item in items:
                #print(item.name, item.isDir, item.isFile, item.path, item.size)
                if item.isDir:
                    dirs.append(item.name)
        except Exception as e:
            logger.warning("[OEA] Could not get list of folders in specified path: " + path + "\nThis may be because the path does not exist.")
        return dirs

    def get_latest_folder(self, path):
        folders = oea.get_folders(path)
        if len(folders) > 0: return folders[-1]
        else: return None

    # Remove a folder if it exists (defaults to use of recursive removal).
    def rm_if_exists(self, path, recursive_remove=True):
        try:
            mssparkutils.fs.rm(path, recursive_remove)
        except Exception as e:
            pass

    def pop_from_path(self, path):
        """ Pops the last arg in a path and returns the path and the last arg as a tuple.
            pop_from_path('abfss://stage2@xyz.dfs.core.windows.net/ms_insights/test.csv') # returns ('abfss://stage2@xyz.dfs.core.windows.net/ms_insights', 'test.csv')
        """
        m = re.match(r"(.*)\/([^/]+)", path)
        return (m.group(1), m.group(2))

    def parse_source_path(self, path):
        """ Parses a path that looks like this: abfss://stage2p@stoeacisd3ggimpl3.dfs.core.windows.net/ms_insights
            and returns a dictionary like this: {'stage_num': '2', 'ss': 'ms_insights'}
            Note that it will also return a 'stage_num' of 2 if the path is stage2p or stage2np - this is by design because the spark db with the s2 prefix will be used for data in stage2 and stage2p.
        """
        m = re.match(r".*:\/\/stage(?P<stage_num>\d+)[n]?[p]?@[^/]+\/(?P<ss>[^/]+)", path)
        return m.groupdict()
    
    def create_lake_db(self, stage_num, source_dir, source_format='DELTA'):
        """ Creates a spark db that points to data in the given stage under the specified source directory (assumes that every folder in the source_dir is a table).
            Example: create_lake_db(2, 'contoso_sis')
            Note that a spark db that points to source data in the delta format can't be queried via SQL serverless pool. More info here: https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/resources-self-help-sql-on-demand#delta-lake
        """
        db_name = f's{stage_num}_{source_dir}'
        spark.sql(f'CREATE DATABASE IF NOT EXISTS {db_name}')
        self.create_lake_views(db_name, self.path(f'stage{stage_num}p', source_dir), source_format)
        self.create_lake_views(db_name, self.path(f'stage{stage_num}np', source_dir), source_format)
        result = "Database created: " + db_name
        logger.info(result)
        return result        

    def create_lake_views(self, db_name, source_path, source_format):
        dirs = self.get_folders(source_path)
        for table_name in dirs:
            spark.sql(f"create table if not exists {db_name}.{table_name} using {source_format} location '{source_path}/{table_name}'")

    def drop_lake_db(self, db_name):
        spark.sql(f'DROP DATABASE IF EXISTS {db_name} CASCADE')
        result = "Database dropped: " + db_name
        logger.info(result)
        return result       

    def create_sql_db(self, stage_num, source_dir, source_format='DELTA'):
        """ Prints out the sql script needed for creating a sql serverless db and set of views. """
        db_name = f'sqls{stage_num}_{source_dir}'
        cmd += '-- Create a new sql script then execute the following in it:'
        cmd += f"IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{db_name}')\nBEGIN\n  CREATE DATABASE {db_name};\nEND;\nGO\n"
        cmd += f"USE {db_name};\nGO\n\n"
        cmd += self.create_sql_views(self.path(f'stage{stage_num}p', source_dir), source_format)
        cmd += self.create_sql_views(self.path(f'stage{stage_num}np', source_dir), source_format)
        print(cmd)

    def create_sql_views(self, source_path, source_format):
        cmd = ''      
        dirs = self.get_folders(source_path)
        for table_name in dirs:
            cmd += f"CREATE OR ALTER VIEW {table_name} AS\n  SELECT * FROM OPENROWSET(BULK '{source_path}/{table_name}', FORMAT='{source_format}') AS [r];\nGO\n"
        return cmd

    def drop_sql_db(self, db_name):
        print('Click on the menu next to the SQL db and select "Delete"')

    # List installed packages
    def list_packages(self):
        import pkg_resources
        for d in pkg_resources.working_set:
            print(d)

    def print_schema_starter(self, entity_name, df):
        """ Prints a starter schema that can be modified as needed when developing the oea schema for a new module. """
        st = f"self.schemas['{entity_name}'] = ["
        for col in df.schema:
            st += f"['{col.name}', '{str(col.dataType)[:-4].lower()}', 'no-op'],\n\t\t\t\t\t\t\t\t\t"
        return st[:-11] + ']'

    def write_rows_as_csv(data, folder, filename, container=None):
        """ Writes a dictionary as a csv to the specified location. This is helpful when creating test data sets and landing them in stage1np.
            data = [{'id':'1','fname':'John'}, {'id':'1','fname':'Jane'}]
        """
        if container == None: container = self.stage1np
        pdf = pd.DataFrame(data)
        mssparkutils.fs.put(f"{container}/{folder}/{filename}", pdf.to_csv(index=False), True) # True indicates overwrite mode  

    def write_rowset_as_csv(data, folder, container=None):
        """ Writes out as csv rows the passed in data. The inbound data should be in a format like this:
            data = { 'students':[{'id':'1','fname':'John'}], 'courses':[{'id':'31', 'name':'Math'}] }
        """
        if container == None: container = self.stage1np
        for entity_name, value in data.items():
            pdf = pd.DataFrame(value)
            mssparkutils.fs.put(f"{container}/{folder}/{entity_name}.csv", pdf.to_csv(index=False), True) # True indicates overwrite mode         

class BaseOEAModule:
    """ Provides data processing methods for Contoso SIS data (the student information system for the fictional Contoso school district).  """
    def __init__(self, source_folder, pseudonymize = True):
        self.source_folder = source_folder
        self.pseudonymize = pseudonymize
        self.stage1np = f"{oea.stage1np}/{source_folder}"
        self.stage2np = f"{oea.stage2np}/{source_folder}"
        self.stage2p = f"{oea.stage2p}/{source_folder}"
        self.stage3np = f"{oea.stage3np}/{source_folder}"
        self.stage3p = f"{oea.stage3p}/{source_folder}"
        self.module_path = f"{oea.framework_path}/modules/{source_folder}"
        self.schemas = {}

    def _process_entity_from_stage1(self, path, entity_name, format='csv', write_mode='overwrite', header='true'):
        spark_schema = oea.to_spark_schema(self.schemas[entity_name])
        df = spark.read.format(format).load(f"{self.stage1np}/{path}/{entity_name}", header=header, schema=spark_schema)

        if self.pseudonymize:
            df_pseudo, df_lookup = oea.pseudonymize(df, self.schemas[entity_name])
            df_pseudo.write.format('delta').mode(write_mode).save(f"{self.stage2p}/{entity_name}")
            if len(df_lookup.columns) > 0:
                df_lookup.write.format('delta').mode(write_mode).save(f"{self.stage2np}/{entity_name}_lookup")
        else:
            df = oea.fix_column_names(df)   
            df.write.format('delta').mode(write_mode).save(f"{self.stage2np}/{entity_name}")

    def delete_stage1(self):
        oea.rm_if_exists(self.stage1np)

    def delete_stage2(self):
        oea.rm_if_exists(self.stage2np)
        oea.rm_if_exists(self.stage2p)

    def delete_stage3(self):
        oea.rm_if_exists(self.stage3np)
        oea.rm_if_exists(self.stage3p)                

    def delete_all_stages(self):
        self.delete_stage1()
        self.delete_stage2()
        self.delete_stage3()

    def create_stage2_lake_db(self, format='DELTA'):
        oea.create_lake_db(self.stage2p, format)
        oea.create_lake_db(self.stage2np, format)

    def create_stage3_lake_db(self, format='DELTA'):
        oea.create_lake_db(self.stage3p, format)
        oea.create_lake_db(self.stage3np, format)

    def copy_test_data_to_stage1(self):
        mssparkutils.fs.cp(self.module_path + '/test_data', self.stage1np, True)   

class DataLakeWriter:
    def __init__(self, root_destination):
        self.root_destination = root_destination

    def write(self, path_and_filename, data_str, format='csv'):
        mssparkutils.fs.append(f"{self.root_destination}/{path_and_filename}", data_str, True) # Set the last parameter as True to create the file if it does not exist

oea = OEA()