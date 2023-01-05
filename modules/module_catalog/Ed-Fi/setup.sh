#!/bin/bash

# Installs the Ed-Fi module
# This script can be invoked directly to install the Ed-Fi module assets into an existing Synapse Workspace.
if [ $# -ne 2 ]; then
    echo "This setup script will install the Ed-Fi module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name> <resource_group_name>"
    exit 1
fi

synapse_workspace=$1
resource_group=$2
this_file_path=$(dirname $(realpath $0))

echo "--> Setting up the Ed-Fi module assets."

# 1) create datasets
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_JSON_File --file @$this_file_path/dataset/DS_JSON_File.json --only-show-errors"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_JSON --file @$this_file_path/dataset/DS_JSON.json --only-show-errors"
eval "az synapse dataset create --workspace-name $synapse_workspace --name DS_REST_Anonymous --file @$this_file_path/dataset/DS_REST_Anonymous.json --only-show-errors"

# 2) install dataflows
eval "az synapse data-flow create --workspace-name $synapse_workspace --name Create_CheckpointKeysFile --file @$this_file_path/dataflow/Create_CheckpointKeysFile.json --only-show-errors"
eval "az synapse data-flow create --workspace-name $synapse_workspace --name edfi_delete  --file @$this_file_path/dataflow/edfi_delete.json --only-show-errors"
eval "az synapse data-flow create --workspace-name $synapse_workspace --name edfi_upsert  --file @$this_file_path/dataflow/edfi_upsert.json --only-show-errors"

# 3) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name Refine_EdFi --spark-pool-name spark3p2sm --file @$this_file_path/notebook/Refine_EdFi.ipynb --only-show-errors"

# 4) create integration runtime
eval "az synapse integration-runtime managed create --workspace-name $synapse_workspace --resource-group $resource_group --name IR-DataFlows --time-to-live 10"

# 5) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_REST_Keyset_Parallel --file @$this_file_path/pipeline/Copy_from_REST_Keyset_Parallel.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_from_REST_Anonymous_to_ADLS --file @$this_file_path/pipeline/Copy_from_REST_Anonymous_to_ADLS.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_EdFi_Entities_to_Stage1 --file @$this_file_path/pipeline/Copy_EdFi_Entities_to_Stage1.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Copy_Stage1_To_Stage2 --file @$this_file_path/pipeline/Copy_Stage1_To_Stage2.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name Master_Pipeline --file @$this_file_path/pipeline/Master_Pipeline.json"

echo "--> Setup complete. The Ed-Fi module assets have been installed in the specified synapse workspace: $synapse_workspace"