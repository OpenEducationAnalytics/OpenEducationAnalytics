#!/bin/bash
resourceGroup="EduAnalytics9"
orgId="cisd9"
storageAccount="steduanalytics${orgId}"
location="eastus"
tmpPwd="$(openssl rand -base64 12)"
synapseWorkspace="syeduanalytics${orgId}"
userObjectId="$(az ad signed-in-user show --query objectId)"

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

az synapse workspace create --name $synapseWorkspace --resource-group $resourceGroup \
  --storage-account $storageAccount --file-system synapse --location $location \
  --sql-admin-login-user eduanalyticsuser --sql-admin-login-password $tmpPwd \

az synapse workspace firewall-rule create --name allowAll --workspace-name $synapseWorkspace --resource-group $resourceGroup \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

#az synapse role assignment create --workspace-name $synapseWorkspace --role "Workspace Admin" --assignee $userObjectId
#az synapse role assignment create --workspace-name $synapseWorkspace --role "Apache Spark Admin" --assignee $userObjectId
