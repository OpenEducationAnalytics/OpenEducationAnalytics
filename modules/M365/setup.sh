#!/bin/bash

orgId=$1
resourceGroup="EduAnalytics${orgId}"
storageAccount="steduanalytics${orgId}"

module_path=$(dirname $(realpath $0))
# copy test data set
az storage copy -s $module_path/test_data/m365 -d https://$storageAccount.blob.core.windows.net/stage1 --recursive

# todo: determine why neither of these work
# https://docs.microsoft.com/en-us/cli/azure/synapse/notebook?view=azure-cli-latest#az_synapse_notebook_import
#az synapse notebook import --workspace-name syeduanalyticsx6 --name mytest --file @/home/gene/clouddrive/OpenEduAnalytics/modules/M365/m365.ipynb
#az synapse notebook create --workspace-name syeduanalyticsx6 --name mytest --file @/home/gene/clouddrive/OpenEduAnalytics/modules/M365/m365.ipynb
