#!/bin/bash

# Installs the OEA framework assets.
# This script can be invoked directly to install the OEA framework into an existing Synapse Workspace.
# This script is also automatically called from the base setup.sh script when setting up the complete OEA example including the provisioning of Azure resources.
if [ $# -ne 3 ]; then
    echo "This setup script will install the OEA framework assets into an existing Synapse workspace."
    echo "Invoke this script like this:"
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
sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/notebook/OEA_py.ipynb > $this_file_path/tmp/OEA_py1.ipynb
sed "s/yourkeyvault/$key_vault/" $this_file_path/tmp/OEA_py1.ipynb > $this_file_path/tmp/OEA_py2.ipynb
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_py --spark-pool-name spark3p3sm --file @$this_file_path/tmp/OEA_py2.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 1_read_me --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/1_read_me.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 2_example_data_processing --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/2_example_data_processing.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name 3_example_working_with_schemas --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/3_example_working_with_schemas.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_connector --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/OEA_connector.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_tests --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/OEA_tests.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEATestKit_connector --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/OEATestKit_connector.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEATestKit_py --spark-pool-name spark3p3sm --file @$this_file_path/synapse/notebook/OEATestKit_py.ipynb --only-show-errors"

# 3) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_lake_db --file @$this_file_path/synapse/pipeline/create_lake_db.json"
sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/pipeline/create_sql_db.json > $this_file_path/tmp/create_sql_db.json
eval "az synapse pipeline create --workspace-name $synapse_workspace --name create_sql_db --file @$this_file_path/tmp/create_sql_db.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name delete_dataset --file @$this_file_path/synapse/pipeline/delete_dataset.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_data_from_URL --file @$this_file_path/synapse/pipeline/land_data_from_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_from_ls_datalake --file @$this_file_path/synapse/pipeline/land_from_ls_datalake.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_metadata_from_URL --file @$this_file_path/synapse/pipeline/land_metadata_from_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name ingest --file @$this_file_path/synapse/pipeline/ingest.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name refine --file @$this_file_path/synapse/pipeline/refine.json"

eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_contoso_v0p2 --file @$this_file_path/synapse/pipeline/1_land_contoso_v0p2.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_contoso_v0p2 --file @$this_file_path/synapse/pipeline/2_ingest_contoso_v0p2.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_contoso_v0p2 --file @$this_file_path/synapse/pipeline/3_refine_contoso_v0p2.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_contoso_v0p2 --file @$this_file_path/synapse/pipeline/4_reset_workspace_contoso_v0p2.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_contoso_v0p2 --file @$this_file_path/synapse/pipeline/0_main_contoso_v0p2.json"

echo "--> Setup complete. The OEA framework assets have been installed in the specified synapse workspace: $synapse_workspace"