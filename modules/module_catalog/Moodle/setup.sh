#!/bin/bash

# Installs the Moodle module
# This script can be invoked directly to install the Moodle module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Moodle module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Moodle module assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name Moodle_example --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Moodle_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Moodle_ingest --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Moodle_ingest.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Moodle_refine --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Moodle_refine.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_moodle_test_data --file @$this_file_path/pipeline/1_land_moodle_test_data.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_moodle --file @$this_file_path/pipeline/2_ingest_moodle.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_moodle --file @$this_file_path/pipeline/3_refine_moodle.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_moodle --file @$this_file_path/pipeline/4_reset_workspace_moodle.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_moodle --file @$this_file_path/pipeline/0_main_moodle.json"

echo "--> Setup complete. The Moodle module assets have been installed in the specified synapse workspace: $synapse_workspace"