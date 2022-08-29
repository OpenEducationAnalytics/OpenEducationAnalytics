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
sed "s/yourkeyvault/$key_vault/" $this_file_path/linkedService/LS_KeyVault_OEA.json > $this_file_path/tmp/LS_KeyVault_OEA.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_KeyVault_OEA --file @$this_file_path/tmp/LS_KeyVault_OEA.json"
sed "s/yourstorageaccount/$storage_account/" $this_file_path/linkedService/LS_ADLS_OEA.json > $this_file_path/tmp/LS_ADLS_OEA.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_ADLS_OEA --file @$this_file_path/tmp/LS_ADLS_OEA.json"
sed "s/yoursynapseworkspace/$synapse_workspace/" $this_file_path/linkedService/LS_SQL_Serverless_OEA.json > $this_file_path/tmp/LS_SQL_Serverless_OEA.json
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_SQL_Serverless_OEA --file @$this_file_path/tmp/LS_SQL_Serverless_OEA.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_Azure_SQL_DB --file @$this_file_path/linkedService/LS_Azure_SQL_DB.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_HTTP --file @$this_file_path/linkedService/LS_HTTP.json"
#  - setup Datasets
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_ADLS_binary_file --file @$this_file_path/dataset/DS_ADLS_binary_file.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_ADLS_binary_folder --file @$this_file_path/dataset/DS_ADLS_binary_folder.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_HTTP_binary --file @$this_file_path/dataset/DS_HTTP_binary.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_ADLS_parquet --file @$this_file_path/dataset/DS_ADLS_parquet.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_Azure_SQL_DB --file @$this_file_path/dataset/DS_Azure_SQL_DB.json"

# 2) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_py --spark-pool-name spark3p1sm --file @$this_file_path/notebook/OEA_py.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 1_read_me --spark-pool-name spark3p1sm --file @$this_file_path/notebook/1_read_me.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 2_batch_processing_demo --spark-pool-name spark3p1sm --file @$this_file_path/notebook/2_batch_processing_demo.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 3_data_generation_demo --spark-pool-name spark3p1sm --file @$this_file_path/notebook/3_data_generation_demo.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_connector --spark-pool-name spark3p1sm --file @$this_file_path/notebook/OEA_connector.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name DataGen_py --spark-pool-name spark3p1sm --file @$this_file_path/notebook/DataGen_py.ipynb --only-show-errors"

# 3) setup pipelines
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_URL --file @$this_file_path/pipeline/Copy_from_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_each_URL --file @$this_file_path/pipeline/Copy_from_each_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_Azure_SQL_DB --file @$this_file_path/pipeline/Copy_from_Azure_SQL_DB.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_all_from_Azure_SQL_DB --file @$this_file_path/pipeline/Copy_all_from_Azure_SQL_DB.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name call_oea_framework --file @$this_file_path/pipeline/call_oea_framework.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_lake_db --file @$this_file_path/pipeline/create_lake_db.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_sql_db --file @$this_file_path/pipeline/create_sql_db.json"
sed "s/yourstorageaccount/$storage_account/" $this_file_path/pipeline/example_main_pipeline.json > $this_file_path/tmp/example_main_pipeline.json
eval "az synapse pipeline create --workspace-name $synapse_workspace --name example_main_pipeline --file @$this_file_path/tmp/example_main_pipeline.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name reset_all_for_source --file @$this_file_path/pipeline/reset_all_for_source.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name reset_ingestion_of_table --file @$this_file_path/pipeline/reset_ingestion_of_table.json"


# 4) install the ContosoSIS_py notebook for use with the 'example_main_pipeline' that comes with the framework
eval "az synapse notebook import --workspace-name $synapse_workspace --name ContosoSIS_py --spark-pool-name spark3p1sm --file @$this_file_path/../modules/Student_and_School_Data_Systems/notebook/ContosoSIS_py.ipynb --only-show-errors"

echo "--> Setup complete. The OEA framework assets have been installed in the specified synapse workspace: $synapse_workspace"

