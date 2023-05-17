#!/bin/bash

# Installs the Microsoft Graph module
# This script can be invoked directly to install the Insights module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Microsoft Graph module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Microsoft Graph module assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name Graph_example --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Graph_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Graph_land_test_data --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Graph_land_test_data.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Graph_pre-processing --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Graph_pre-processing.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Graph_schema_correction --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Graph_schema_correction.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Graph_refine --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Graph_refine.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_graph --file @$this_file_path/pipeline/1_land_graph.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_graph --file @$this_file_path/pipeline/2_ingest_graph.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_graph --file @$this_file_path/pipeline/3_refine_graph.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_graph --file @$this_file_path/pipeline/4_reset_workspace_graph.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_graph --file @$this_file_path/pipeline/0_main_graph.json"

echo "--> Setup complete. The Microsoft Graph module assets have been installed in the specified synapse workspace: $synapse_workspace"