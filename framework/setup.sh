#!/bin/bash

# Installs the OEA framework assets.
# This script can be invoked directly to install the OEA framework into an existing Synapse Workspace.
# This script is also automatically called from the base setup.sh script when setting up the complete OEA example including the provisioning of Azure resources.
if [ $# -ne 3 ]; then
    echo "This setup script will install the OEA framework assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name> <storage_account_name> <key_vault_name>"
    exit 1
fi

synapse_workspace=$1
storage_account=$2
key_vault=$3
this_file_path=$(dirname $(realpath $0))
mkdir $this_file_path/tmp

echo "--> Setting up the OEA framework assets."

# 1) install integration assets
#  - setup Linked Services 
sed "s/yourkeyvault/$key_vault/" $this_file_path/synapse/linkedService/LS_KeyVault.json > $this_file_path/tmp/LS_KeyVault.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_KeyVault --file @$this_file_path/tmp/LS_KeyVault.json"
sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/linkedService/LS_DataLake.json > $this_file_path/tmp/LS_DataLake.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_DataLake --file @$this_file_path/tmp/LS_DataLake.json"
sed "s/yoursynapseworkspace/$synapse_workspace/" $this_file_path/synapse/linkedService/LS_SQL_Serverless.json > $this_file_path/tmp/LS_SQL_Serverless.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_SQL_Serverless --file @$this_file_path/tmp/LS_SQL_Serverless.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_Azure_SQL_DB --file @$this_file_path/synapse/linkedService/LS_Azure_SQL_DB.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_HTTP --file @$this_file_path/synapse/linkedService/LS_HTTP.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_REST --file @$this_file_path/synapse/linkedService/LS_REST.json"

#  - setup Datasets
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_datalake_file --file @$this_file_path/synapse/dataset/DS_datalake_file.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_datalake_folder --file @$this_file_path/synapse/dataset/DS_datalake_folder.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_HTTP_binary --file @$this_file_path/synapse/dataset/DS_HTTP_binary.json"
#eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_parquet --file @$this_file_path/synapse/dataset/DS_parquet.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_Azure_SQL_DB --file @$this_file_path/synapse/dataset/DS_Azure_SQL_DB.json"

# 2) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_py --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/OEA_py.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 1_read_me --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/1_read_me.ipynb --only-show-errors"
#eval "az synapse notebook import --workspace-name $synapse_workspace --name 2_batch_processing_demo --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/2_batch_processing_demo.ipynb --only-show-errors"
#eval "az synapse notebook import --workspace-name $synapse_workspace --name 3_data_generation_demo --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/3_data_generation_demo.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_connector --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/OEA_connector.ipynb --only-show-errors"
#eval "az synapse notebook import --workspace-name $synapse_workspace --name DataGen_py --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/DataGen_py.ipynb --only-show-errors"
# (this is the ContosoSIS_py notebook for use with the 'example_main_pipeline' that comes with the framework)
#eval "az synapse notebook import --workspace-name $synapse_workspace --name ContosoSIS_py --spark-pool-name spark3p2sm --file @$this_file_path/synapse/notebook/ContosoSIS_py.ipynb --only-show-errors"

# 3) setup pipelines
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_data_from_URL --file @$this_file_path/synapse/pipeline/land_data_from_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_from_each_URL --file @$this_file_path/synapse/pipeline/land_from_each_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name example_main_pipeline --file @$this_file_path/synapse/pipeline/example_main_pipeline.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_URL --file @$this_file_path/synapse/pipeline/Copy_from_URL.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_each_URL --file @$this_file_path/synapse/pipeline/Copy_from_each_URL.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_Azure_SQL_DB --file @$this_file_path/synapse/pipeline/Copy_from_Azure_SQL_DB.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_all_from_Azure_SQL_DB --file @$this_file_path/synapse/pipeline/Copy_all_from_Azure_SQL_DB.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name call_oea_framework --file @$this_file_path/synapse/pipeline/call_oea_framework.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_lake_db --file @$this_file_path/synapse/pipeline/create_lake_db.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_sql_db --file @$this_file_path/synapse/pipeline/create_sql_db.json"
#sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/pipeline/example_main_pipeline.json > $this_file_path/tmp/example_main_pipeline.json
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name example_main_pipeline --file @$this_file_path/tmp/example_main_pipeline.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name reset_all_for_source --file @$this_file_path/synapse/pipeline/reset_all_for_source.json"
#eval "az synapse pipeline create --workspace-name $synapse_workspace --name reset_ingestion_of_table --file @$this_file_path/synapse/pipeline/reset_ingestion_of_table.json"

echo "--> Setup complete. The OEA framework assets have been installed in the specified synapse workspace: $synapse_workspace"