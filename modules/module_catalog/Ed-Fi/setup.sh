#!/bin/bash

# Installs the Ed-Fi module
# This script can be invoked directly to install the Ed-Fi module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Ed-Fi module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Ed-Fi module assets."

# 2) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name EdFi_Land --spark-pool-name spark3p3sm --file @$this_file_path/notebook/EdFi_Land.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name EdFi_Ingest --spark-pool-name spark3p3sm --file @$this_file_path/notebook/EdFi_Ingest.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name EdFi_Refine --spark-pool-name spark3p3sm --file @$this_file_path/notebook/EdFi_Refine.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name edfi_fetch_urls --spark-pool-name spark3p3sm --file @$this_file_path/notebook/edfi_fetch_urls.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name edfi_py --spark-pool-name spark3p3sm --file @$this_file_path/notebook/edfi_py.ipynb --only-show-errors"

# 3) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_edfi --file @$this_file_path/pipeline/1_land_edfi.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_edfi --file @$this_file_path/pipeline/2_ingest_edfi.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_edfi --file @$this_file_path/pipeline/3_refine_edfi.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_edfi --file @$this_file_path/pipeline/0_main_edfi.json"

echo "--> Setup complete. The Ed-Fi module assets have been installed in the specified synapse workspace: $synapse_workspace"