#!/bin/bash

# Installs the Student Attrition package v1
# This script can be invoked directly to install the Student Attrition package v1 assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Student Attrition package v1 assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

datetime=$(date "+%Y%m%d_%H%M%S")
logfile="student_attrition_package_setup_${datetime}.log"
exec 3>&1 1>>${logfile} 2>&1

org_id=$1
synapse_workspace=$1

this_file_path=$(dirname $(realpath $0))
source $this_file_path/set_names.sh $org_id

echo "--> Setting up the Student Attrition package v1 assets."
output=$(az synapse workspace list | grep $OEA_SYNAPSE)

if [[ $? != 1 ]]; then
  synapse_workspace=$OEA_SYNAPSE
fi

echo "--> Setting up the Student Attrition package v1 assets."

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name attrition_preprocesing --spark-pool-name spark3p3sm --file @$this_file_path/notebooks/attrition_preprocesing.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_preland_rai --file @$this_file_path/pipeline/1_preland_rai.json"

eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_land_rai --file @$this_file_path/pipeline/2_land_rai.json"

eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_ingest_rai --file @$this_file_path/pipeline/3_ingest_rai.json"

eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_refine_rai --file @$this_file_path/pipeline/4_refine_rai.json"

eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_attrition --file @$this_file_path/pipeline/0_main_attrition.json"

echo "--> Setup complete. The Student Attrition package v1 assets have been installed in the specified synapse workspace: $synapse_workspace"