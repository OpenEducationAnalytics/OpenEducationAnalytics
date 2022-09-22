from delta.tables import DeltaTable
from notebookutils import mssparkutils
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType, TimestampType, BooleanType, ShortType, DateType
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import pandas as pd
import sys
import re
import json
import datetime
import pytz
import random
import io
import logging

logger = logging.getLogger('OEA')

class OEA:
    def __init__(self, storage_account='', instrumentation_key=None, salt='', logging_level=logging.DEBUG):
        if storage_account:
            self.storage_account = storage_account
        else:
            oea_id = mssparkutils.env.getWorkspaceName()[8:] # extracts the OEA id for this OEA instance from the synapse workspace name (based on OEA naming convention)
            self.storage_account = 'stoea' + oea_id # sets the name of the storage account based on OEA naming convention
            self.keyvault = 'kv-oea-' + oea_id
        self.keyvault_linked_service = 'LS_KeyVault_OEA'
        self.serverless_sql_endpoint = mssparkutils.env.getWorkspaceName() + '-ondemand.sql.azuresynapse.net'
        self._initialize_logger(logging_level)
        self.salt = salt
        self.timezone = 'EST'
        self.stage1np = 'abfss://stage1np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage2np = 'abfss://stage2np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage2p = 'abfss://stage2p@' + self.storage_account + '.dfs.core.windows.net'
        self.stage3np = 'abfss://stage3np@' + self.storage_account + '.dfs.core.windows.net'
        self.stage3p = 'abfss://stage3p@' + self.storage_account + '.dfs.core.windows.net'
        self.framework_path = 'abfss://oea-framework@' + self.storage_account + '.dfs.core.windows.net'

        # Initialize framework db
        spark.sql(f"CREATE DATABASE IF NOT EXISTS oea")
        spark.sql(f"CREATE TABLE IF NOT EXISTS oea.env (name string not null, value string not null, description string) USING DELTA LOCATION '{self.framework_path}/db/env'")
        df = spark.sql("select value from oea.env where name='storage_account'")
        if df.first(): spark.sql(f"UPDATE oea.env set value='{self.storage_account}' where name='storage_account'")
        else: spark.sql(f"INSERT INTO oea.env VALUES ('storage_account', '{self.storage_account}', 'The name of the data lake storage account for this OEA instance.')")
        spark.sql(f"CREATE TABLE IF NOT EXISTS OEA.watermark (source string not null, entity string not null, watermark timestamp not null) USING DELTA LOCATION '{self.framework_path}/db/watermark'")

        logger.debug("OEA initialized.")
    
    def path(self, container_name, directory_path=None):
        if directory_path:
            return f'abfss://{container_name}@{self.storage_account}.dfs.core.windows.net/{directory_path}'
        else:
            return f'abfss://{container_name}@{self.storage_account}.dfs.core.windows.net'

    def convert_path(self, path):
        """ Converts the given path into a valid url.
            eg, convert_path('stage1np/contoso_sis/student/*') # returns abfss://stage1np@storageaccount.dfs.core.windows.net/contoso_sis/student/*
        """
        path_args = path.split('/')
        stage = path_args.pop(0)
        return self.path(stage, '/'.join(path_args))            

    def _initialize_logger(self, logging_level):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        for handler in logging.getLogger().handlers:
            handler.setFormatter(formatter)           
        # Customize log level for all loggers
        logging.getLogger().setLevel(logging_level)        

    def get_value_from_db(self, query):
        df = spark.sql(query)
        if df.first(): return df.first()[0]
        else: return None

    def get_last_watermark(self, source, entity):
        return self.get_value_from_db(f"select w.watermark from oea.watermark w where w.source='{source}' and w.entity='{entity}' order by w.watermark desc")

    def insert_watermark(self, source, entity, watermark_datetime):
        spark.sql(f"insert into oea.watermark values ('{source}', '{entity}', '{watermark_datetime}')")

    def get_secret(self, secret_name):
        """ Retrieves the specified secret from the keyvault.
            This method assumes that the keyvault linked service has been setup and is accessible.
        """
        sc = SparkSession.builder.getOrCreate()
        token_library = sc._jvm.com.microsoft.azure.synapse.tokenlibrary.TokenLibrary
        value = token_library.getSecret(self.keyvault, secret_name, self.keyvault_linked_service)        
        return value

    def delete(self, path):
        oea.rm_if_exists(self.convert_path(path))

    def land(self, data_source, entity, df, partition_label='', format_str='csv', header=True, mode='overwrite'):
        """ Lands data in stage1np. If partition label is not provided, the current datetime is used with the label of 'batchdate'.
            eg, land('contoso_isd', 'student', data, 'school_year=2021')
        """
        tz = pytz.timezone(self.timezone)
        datetime_str = datetime.datetime.now(tz).replace(microsecond=0).isoformat()
        datetime_str = datetime_str.replace(':', '') # Path names can't have a colon - https://github.com/apache/hadoop/blob/trunk/hadoop-common-project/hadoop-common/src/site/markdown/filesystem/introduction.md#path-names
        df.write.format(format_str).save(self.path('stage1np', f'{data_source}/{entity}/{partition_label}/batchdate={datetime_str}'), header=header, mode=mode)

    def load(self, folder, table, stage=None, data_format='delta'):
        """ Loads a dataframe based on the path specified in the given args """
        if stage is None: stage = self.stage2p
        path = f"{stage}/{folder}/{table}"
        try:
            df = spark.read.load(f"{stage}/{folder}/{table}", format=data_format)
            return df        
        except AnalysisException as e:
            raise ValueError("Failed to load. Are you sure you have the right path?\nMore info below:\n" + str(e)) 

    def load_csv(self, path, header=True):
        """ Loads a dataframe based on the path specified 
            eg, df = load_csv('stage1np/example/student/*')
        """
        url_path = self.convert_path(path)
        try:
            df = spark.read.load(url_path, format='csv', header=header)
            return df        
        except AnalysisException as e:
            raise ValueError(f"Failed to load from: {url_path}. Are you sure you have the right path?\nMore info below:\n" + str(e))

    def load_delta(self, path):
        """ Loads a dataframe based on the path specified 
            eg, df = load_delta('stage2np/example/student/*')
        """
        url_path = self.convert_path(path)
        try:
            df = spark.read.load(url_path, format='delta')
            return df        
        except AnalysisException as e:
            raise ValueError(f"Failed to load from: {url_path}. Are you sure you have the right path?\nMore info below:\n" + str(e))

    def load_from_stage1(self, path_and_filename, data_format='csv', header=True):
        """ Loads a dataframe with data from stage1, based on the path specified in the given args """
        path = f"{self.stage1np}/{path_and_filename}"
        df = spark.read.load(path, format=data_format, header=header)
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

    def ingest_incremental_data(self, source_system, tablename, schema, partition_by, primary_key='id', data_format='csv', has_header=True):
        """ Processes incremental batch data from stage1 into stage2 """
        source_path = f'{self.stage1np}/{source_system}/{tablename}'
        p_destination_path = f'{self.stage2p}/{source_system}/{tablename}_pseudo'
        np_destination_path = f'{self.stage2np}/{source_system}/{tablename}_lookup'
        logger.info(f'Processing incremental data from: {source_path} and writing out to: {p_destination_path}')

        if has_header: header_flag = 'true'
        else: header_flag = 'false'
        spark_schema = self.to_spark_schema(schema)
        df = spark.readStream.load(source_path + '/*', format=data_format, header=header_flag, schema=spark_schema)
        #df = spark.read.load(source_path + '/*', format=data_format, header=header_flag, schema=spark_schema)
        #display(df)
        #df = df.withColumn('batchdate', F.to_timestamp(df.batchdate, "yyyy-MM-dd'T'HHmmssZ"))
        df = df.dropDuplicates([primary_key]) # drop duplicates across batches. More info: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#streaming-deduplication
        
        df_pseudo, df_lookup = self.pseudonymize(df, schema)

        if len(df_pseudo.columns) == 0:
            logger.info('No data to be written to stage2p')
        else:        
            query = df_pseudo.writeStream.format("delta").outputMode("append").trigger(once=True).option("checkpointLocation", source_path + '/_checkpoints/incremental_p').partitionBy(partition_by)
            query = query.start(p_destination_path)
            query.awaitTermination()   # block until query is terminated, with stop() or with error; A StreamingQueryException will be thrown if an exception occurs.
            logger.info(query.lastProgress)

        if len(df_lookup.columns) == 0:
            logger.info('No data to be written to stage2np')
        else:
            query2 = df_lookup.writeStream.format("delta").outputMode("append").trigger(once=True).option("checkpointLocation", source_path + '/_checkpoints/incremental_np').partitionBy(partition_by)
            query2 = query2.start(np_destination_path)
            query2.awaitTermination()   # block until query is terminated, with stop() or with error; A StreamingQueryException will be thrown if an exception occurs.
            logger.info(query2.lastProgress)        

    def _merge_into_table(self, df, destination_path, checkpoints_path, condition):
        """ Merges data from the given dataframe into the delta table at the specified destination_path, based on the given condition.
            If not delta table exists at the specified destination_path, a new delta table is created and the data from the given dataframe is inserted.
            eg, merge_into_table(df_lookup, np_destination_path, source_path + '/_checkpoints/delta_np', "current.id_pseudonym = updates.id_pseudonym")
        """
        if DeltaTable.isDeltaTable(spark, destination_path):      
            dt = DeltaTable.forPath(spark, destination_path)
            def upsert(batch_df, batchId):
                dt.alias("current").merge(batch_df.alias("updates"), condition).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()                
            query = df.writeStream.format("delta").foreachBatch(upsert).outputMode("update").trigger(once=True).option("checkpointLocation", checkpoints_path)
        else:
            logger.info(f'Delta table does not yet exist at {destination_path} - creating one now and inserting initial data.')
            query = df.writeStream.format("delta").outputMode("append").trigger(once=True).option("checkpointLocation", checkpoints_path)
        query = query.start(destination_path)
        query.awaitTermination()   # block until query is terminated, with stop() or with error; A StreamingQueryException will be thrown if an exception occurs.
        logger.info(query.lastProgress)    

    def ingest_delta_data(self, source_system, tablename, schema, partition_by, primary_key='id', data_format='csv', has_header=True):
        """ Processes delta batch data from stage1 into stage2 """
        source_path = f'{self.stage1np}/{source_system}/{tablename}'
        p_destination_path = f'{self.stage2p}/{source_system}/{tablename}_pseudo'
        np_destination_path = f'{self.stage2np}/{source_system}/{tablename}_lookup'
        logger.info(f'Processing delta data from: {source_path} and writing out to: {p_destination_path}')

        if has_header: header_flag = 'true'
        else: header_flag = 'false'
        spark_schema = self.to_spark_schema(schema)
        df = spark.readStream.load(source_path + '/*', format=data_format, header=header_flag, schema=spark_schema)
        
        df_pseudo, df_lookup = self.pseudonymize(df, schema)

        if len(df_pseudo.columns) == 0:
            logger.info('No data to be written to stage2p')
        else:
            self._merge_into_table(df_pseudo, p_destination_path, source_path + '/_checkpoints/delta_p', "current.id_pseudonym = updates.id_pseudonym")

        if len(df_lookup.columns) == 0:
            logger.info('No data to be written to stage2np')
        else:
            self._merge_into_table(df_lookup, np_destination_path, source_path + '/_checkpoints/delta_np', "current.id_pseudonym = updates.id_pseudonym")

    def ingest_snapshot_data(self, source_system, tablename, schema, partition_by, primary_key='id', data_format='csv', has_header=True):
        """ Processes snapshot batch data from stage1 into stage2 """
        source_path = f'{self.stage1np}/{source_system}/{tablename}'
        latest_batch = self.get_latest_folder(source_path)
        source_path = source_path + '/' + latest_batch
        p_destination_path = f'{self.stage2p}/{source_system}/{tablename}_pseudo'
        np_destination_path = f'{self.stage2np}/{source_system}/{tablename}_lookup'
        logger.info(f'Processing snapshot data from: {source_path} and writing out to: {p_destination_path}')

        if has_header: header_flag = 'true'
        else: header_flag = 'false'
        spark_schema = self.to_spark_schema(schema)
        df = spark.read.load(source_path, format=data_format, header=header_flag, schema=spark_schema)
        df = df.dropDuplicates([primary_key]) # More info: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#streaming-deduplication
        
        df_pseudo, df_lookup = self.pseudonymize(df, schema)

        if len(df_pseudo.columns) == 0:
            logger.info('No data to be written to stage2p')
        else:
            df_pseudo.write.save(p_destination_path, format='delta', mode='overwrite', partitionBy=partition_by) 

        if len(df_lookup.columns) == 0:
            logger.info('No data to be written to stage2np')
        else:
            df_lookup.write.save(np_destination_path, format='delta', mode='overwrite', partitionBy=partition_by) 

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
        if not path.startswith("abfss:"):
            path = self.convert_path(path)
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
        folders = self.get_folders(path)
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

    def create_empty_dataframe(self, schema):
        """ Creates an empty dataframe based on the given schema which is specified as an array of column names and sql types.
            eg, schema = [['data_source','string'], ['entity','string'], ['watermark','timestamp']]
        """
        fields = []
        for col_name, col_type in schema:
            fields.append(StructField(col_name, globals()[col_type.lower().capitalize() + "Type"](), True))
        spark_schema = StructType(fields)
        df = spark.createDataFrame(spark.sparkContext.emptyRDD(), spark_schema)
        return df

    def delete_data_source(self, data_source):
        self.rm_if_exists(self.convert_path(f'stage1np/{data_source}'))
        self.rm_if_exists(self.convert_path(f'stage2np/{data_source}'))
        self.rm_if_exists(self.convert_path(f'stage2p/{data_source}'))

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