#!/bin/bash

# Installs the Microsoft Education Insights module
# This script can be invoked directly to install the Insights module assets into an existing Synapse Workspace.
if [ $# -ne 1 ]; then
    echo "This setup script will install the Microsoft Education Insights module assets into an existing Synapse workspace."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace_name>"
    exit 1
fi

org_id=$1
synapse_workspace=$1

this_file_path=$(dirname $(realpath $0))
source $this_file_path/set_names.sh $org_id

echo "--> Setting up the Microsoft Education Insights module assets."
output=$(az synapse workspace list | grep $OEA_SYNAPSE)

if [[ $? != 1 ]]; then
  synapse_workspace=$OEA_SYNAPSE
fi

# 1) install notebooks
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_example --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_pre-processing --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_pre-processing.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_ingest --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_ingest.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_schema_correction --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_schema_correction.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_refine --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_refine.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name Insights_DataValidation --spark-pool-name spark3p3sm --file @$this_file_path/notebook/Insights_DataValidation.ipynb --only-show-errors"

# 2) setup pipelines
# Note that the ordering below matters because pipelines that are referred to by other pipelines must be created first.
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_insights_prod_data --file @$this_file_path/pipeline/1_land_insights_prod_data.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 1_land_insights_test_data --file @$this_file_path/pipeline/1_land_insights_test_data.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 2_ingest_insights --file @$this_file_path/pipeline/2_ingest_insights.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 3_refine_insights --file @$this_file_path/pipeline/3_refine_insights.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 4_reset_workspace_insights --file @$this_file_path/pipeline/4_reset_workspace_insights.json"
eval "az synapse pipeline create --workspace-name $synapse_workspace --name 0_main_insights --file @$this_file_path/pipeline/0_main_insights.json"

echo "--> Setup complete. The Microsoft Education Insights module assets have been installed in the specified synapse workspace: $synapse_workspace"