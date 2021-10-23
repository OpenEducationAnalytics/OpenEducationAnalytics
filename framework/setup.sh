#!/bin/bash

# Installs the OEA framework assets.
# This script should not be invoked directly - it's invoked through OpenEduAnalytics/setup.sh
if [ $# -ne 1 ]; then
    echo "This setup script will install the OEA framework assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <mysuffix>"
    echo "where mysuffix is the unique suffix used for your organization (eg, contosoisd)"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the OEA framework assets."
# install integration assets
eval "az synapse linked-service create --workspace-name $synapse_workspace --name LS_ADLS_OEA --file @$this_file_path/linkedService/LS_ADLS_OEA.json"
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
