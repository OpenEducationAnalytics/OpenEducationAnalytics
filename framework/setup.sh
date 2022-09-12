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
root_path = $(dirname $this_file_path)
mkdir $this_file_path/tmp

echo "--> Setting up the OEA framework assets."

# 1) install integration assets
#  - setup Linked Services
sed "s/yourkeyvault/$key_vault/" $this_file_path/synapse/linkedService/LS_KeyVault_OEA.json > $this_file_path/tmp/LS_KeyVault_OEA.json
sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/linkedService/LS_ADLS_OEA.json > $this_file_path/tmp/LS_ADLS_OEA.json
sed "s/yoursynapseworkspace/$synapse_workspace/" $this_file_path/synapse/linkedService/LS_SQL_Serverless_OEA.json > $this_file_path/tmp/LS_SQL_Serverless_OEA.json
for file in $this_file_path/synapse/linkedService/*
do
    filename=$(basename "$file")
    eval "az synapse linked-service create --workspace-name $synapse_workspace --name ${filename:: -5} --file @$this_file_path/synapse/linkedService/$filename"
done

#  - setup Datasets
for file in $this_file_path/synapse/dataset/*
do
    filename=$(basename "$file")
    eval "az synapse dataset create --workspace-name $synapse_workspace --name ${filename:: -5} --file @$this_file_path/synapse/dataset/$filename"
done
# 2) install notebooks
for file in $this_file_path/synapse/notebook/*
do
    filename=$(basename "$file")
    eval "az synapse notebook import --workspace-name $synapse_workspace --name ${filename:: -6} --spark-pool-name spark3p1sm --file @$this_file_path/synapse/notebook/$filename --only-show-errors"
done
# 3) setup pipelines
sed "s/yourstorageaccount/$storage_account/" $this_file_path/synapse/pipeline/example_main_pipeline.json > $this_file_path/tmp/example_main_pipeline.json
eval "az synapse pipeline create --workspace-name $synapse_workspace --name example_main_pipeline --file @$this_file_path/tmp/example_main_pipeline.json"
for file in $this_file_path/synapse/pipeline/*
do
    filename=$(basename "$file")
    eval "az synapse pipeline create --workspace-name $synapse_workspace --name ${filename:: -5} --file @$this_file_path/synapse/pipeline/$filename"
done

# 4) install the ContosoSIS_py notebook for use with the 'example_main_pipeline' that comes with the framework
eval "az synapse notebook import --workspace-name $synapse_workspace --name ContosoSIS_py --spark-pool-name spark3p1sm --file @$this_file_path/../modules/module_catalog/Student_and_School_Data_Systems/notebook/ContosoSIS_py.ipynb --only-show-errors"

echo "--> Setup complete. The OEA framework assets have been installed in the specified synapse workspace: $synapse_workspace"

