#!/bin/bash

# Installs the SIF module
# This script can be invoked directly to install the SIF module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the SIF module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the SIF module assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name SIF_example --spark-pool-name spark3p2sm --file @$this_file_path/notebook/SIF_example.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name land_json_data_from_URL --file @$this_file_path/pipeline/land_json_data_from_URL.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name ingest_with_options --file @$this_file_path/pipeline/ingest_with_options.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_SIF --file @$this_file_path/pipeline/1_land_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_SIF --file @$this_file_path/pipeline/2_ingest_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_SIF --file @$this_file_path/pipeline/3_refine_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_SIF --file @$this_file_path/pipeline/4_reset_workspace_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_SIF --file @$this_file_path/pipeline/0_main_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_all_SIF --file @$this_file_path/pipeline/1_land_all_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_all_SIF --file @$this_file_path/pipeline/2_ingest_all_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_all_SIF --file @$this_file_path/pipeline/3_refine_all_SIF.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_all_SIF --file @$this_file_path/pipeline/0_main_all_SIF.json"

echo "--> Setup complete. The SIF module assets have been installed in the specified synapse workspace: $synapse_workspace"