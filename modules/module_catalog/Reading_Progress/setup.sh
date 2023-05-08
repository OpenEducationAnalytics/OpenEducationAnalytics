#!/bin/bash

# Installs the Reading Progress module
# This script can be invoked directly to install the Reading Progress module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Reading Progress module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Reading Progress module assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name ReadingProgress_example --spark-pool-name spark3p2med --file @$this_file_path/notebook/ReadingProgress_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name ReadingProgress_ingest --spark-pool-name spark3p2med --file @$this_file_path/notebook/ReadingProgress_ingest.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name ReadingProgress_schema_correction --spark-pool-name spark3p2med --file @$this_file_path/notebook/ReadingProgress_schema_correction.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name ReadingProgress_refine --spark-pool-name spark3p2med --file @$this_file_path/notebook/ReadingProgress_refine.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_reading_progress --file @$this_file_path/pipeline/1_land_reading_progress.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_reading_progress --file @$this_file_path/pipeline/2_ingest_reading_progress.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_reading_progress --file @$this_file_path/pipeline/3_refine_reading_progress.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_reading_progress --file @$this_file_path/pipeline/4_reset_workspace_reading_progress.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_reading_progress --file @$this_file_path/pipeline/0_main_reading_progress.json"

echo "--> Setup complete. The Reading Progress module assets have been installed in the specified synapse workspace: $synapse_workspace"