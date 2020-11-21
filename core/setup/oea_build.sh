#!/bin/bash
resourceGroup="EduAnalytics"
orgId="cisd"
storageAccount="steduanalytics${orgId}"
location="northeurope"
tmpPwd="$(openssl rand -base64 12)"
synapseWorkspace="syeduanalytics${orgId}"
userObjectId=$(az ad signed-in-user show --query objectId -o tsv)

# Create the resource group
az group create -l $location -n $resourceGroup

# Create the storage account and containers
# ref here: https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
az storage account create --resource-group $resourceGroup --name steduanalytics${orgId} --location $location \
  --kind StorageV2 --sku Standard_RAGRS --enable-hierarchical-namespace true --access-tier Hot

az storage container create --account-name $storageAccount --name synapse --auth-mode login
az storage container create --account-name $storageAccount --name stage1 --auth-mode login
az storage container create --account-name $storageAccount --name stage2 --auth-mode login
az storage container create --account-name $storageAccount --name stage3 --auth-mode login

# Create Synapse workspace, and configure firewall to allow access to workspace
az synapse workspace create --name $synapseWorkspace --resource-group $resourceGroup \
  --storage-account $storageAccount --file-system synapse --location $location \
  --sql-admin-login-user eduanalyticsuser --sql-admin-login-password $tmpPwd \

az synapse workspace firewall-rule create --name allowAll --workspace-name $synapseWorkspace --resource-group $resourceGroup \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

#az synapse role assignment create --workspace-name $synapseWorkspace --role "Workspace Admin" --assignee $userObjectId
#az synapse role assignment create --workspace-name $synapseWorkspace --role "Apache Spark Admin" --assignee $userObjectId

# Create security groups in AD, and grant access to storage
az ad group create --display-name 'Edu Analytics Global Admin' --mail-nickname 'EduAnalyticsGlobalAdmin'
az ad group owner add --group 'Edu Analytics Global Admin' --owner-object-id $userObjectId

az ad group create --display-name 'Edu Analytics Data Scientists' --mail-nickname 'EduAnalyticsDataScientists'
az ad group owner add --group 'Edu Analytics Data Scientists' --owner-object-id $userObjectId

az ad group create --display-name 'Edu Analytics Data Engineers' --mail-nickname 'EduAnalyticsDataEngineers'
az ad group owner add --group 'Edu Analytics Data Engineers' --owner-object-id $userObjectId

az ad group create --display-name 'Edu Analytics External Data Scientists' --mail-nickname 'EduAnalyticsExternalDataScientists'
az ad group owner add --group 'Edu Analytics External Data Scientists' --owner-object-id $userObjectId

globalAdmins=$(az ad group show --group "Edu Analytics Global Admin" --query objectId --output tsv)
az role assignment create --role "Owner" --assignee $globalAdmins --resource-group $resourceGroup
az role assignment create --role "Storage Blob Data Contributor" --assignee $globalAdmins --resource-group $resourceGroup

dataScientists=$(az ad group show --group "Edu Analytics Data Scientists" --query objectId --output tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $dataScientists --resource-group $resourceGroup

dataEngineers=$(az ad group show --group "Edu Analytics Data Engineers" --query objectId --output tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $dataEngineers --resource-group $resourceGroup
