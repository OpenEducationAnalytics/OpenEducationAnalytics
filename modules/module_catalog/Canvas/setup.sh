#!/bin/bash

# Installs the Canvas module
# This script can be invoked directly to install the Canvas module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Canvas module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Canvas module assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name Canvas_example --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Canvas_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Canvas_pre-processing --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Canvas_pre-processing.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Canvas_ingest --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Canvas_ingest.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Canvas_refine --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Canvas_refine.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_canvas_test_data --file @$this_file_path/pipeline/1_land_canvas_test_data.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_canvas --file @$this_file_path/pipeline/2_ingest_canvas.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_canvas --file @$this_file_path/pipeline/3_refine_canvas.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_canvas --file @$this_file_path/pipeline/4_reset_workspace_canvas.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_canvas --file @$this_file_path/pipeline/0_main_canvas.json"

echo "--> Setup complete. The Canvas module assets have been installed in the specified synapse workspace: $synapse_workspace"