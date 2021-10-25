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
key_vault_$3
this_file_path=$(dirname $(realpath $0))
mkdir $this_file_path/tmp

echo "--> Setting up the OEA framework assets."
sed "s/yoursynapseworkspace/$synapse_workspace/" $this_file_path/linkedService/LS_SQL_Serverless_OEA.json > $this_file_path/tmp/LS_SQL_Serverless_OEA.json
sed "s/yourstorageaccount/$storage_account/" $this_file_path/linkedService/LS_ADLS_OEA.json > $this_file_path/tmp/LS_ADLS_OEA.json
sed "s/yourkeyvault/$key_vault/" $this_file_path/linkedService/LS_KeyVault_OEA.json > $this_file_path/tmp/LS_KeyVault_OEA.json

# install integration assets
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_ADLS_OEA --file @$this_file_path/tmp/LS_ADLS_OEA.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_SQL_Serverless_OEA --file @$this_file_path/tmp/LS_SQL_Serverless_OEA.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_KeyVault_OEA --file @$this_file_path/tmp/LS_KeyVault_OEA.json"
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_HTTP --file @$this_file_path/linkedService/LS_HTTP.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_ADLS_binary --file @$this_file_path/dataset/DS_ADLS_binary.json"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_HTTP_binary --file @$this_file_path/dataset/DS_HTTP_binary.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name OEA_ex1_data_ingestion --file @$this_file_path/pipeline/OEA_ex1_data_ingestion.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name OEA_ex2_data_ingestion --file @$this_file_path/pipeline/OEA_ex2_data_ingestion.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name OEA_ex3_data_ingestion --file @$this_file_path/pipeline/OEA_ex3_data_ingestion.json"
# install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name OEA_py --file @$this_file_path/notebook/OEA_py.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name DataGen_py --file @$this_file_path/notebook/DataGen_py.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name data_generation_example --file @$this_file_path/notebook/data_generation_example.ipynb --only-show-errors"

# install the ContosoISD package for an example the user can walk through
echo "--> Setting up the example OEA package."
$this_file_path/../packages/ContosoISD/setup.sh $synapse_workspace
echo "--> Setup complete. The OEA assets have been installed in the specified synapse workspace: $synapse_workspace"
