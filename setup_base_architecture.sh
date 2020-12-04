#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture. 
# Basic steps are:
# 1) create resource group
# 2) create storage account and storage containers (stage1, stage2, stage3, synapse)
# 3) create synapse workspace, configure firewall access, and create Spark pool
# 4) create security groups and assign them access to storage

if [ $# -ne 1 ] && [ $# -ne 2 ]; then
    echo "This setup script will install the Open Edu Analytics base architecture."
    echo "Invoke this script like this:  setup.sh <orgId>"
    echo "where orgId is the id for your organization (eg, contosoisd)."
    echo "By default, the Azure resources will be provisioned in  the East US location."
    echo "If you want to have the resources provisioned in an alternate location, invoke the script like this: setup.sh <orgId> <location>"
    echo "where orgId is the id for your organization (eg, contosoisd), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope)."
    exit 1
fi
#read -p 'Enter an org id, using only lowercase letters and numbers (eg, contosoisd3): ' org_id
org_id=$1
#read -p 'Enter the location for the Azure resources to be create in (eg, eastus, westus, northeurope) [eastus]: ' location
location=$2
location=${location:-eastus}

resource_group="EduAnalytics${org_id}"
subscription_id=$(az account show --query id -o tsv)
storage_account="steduanalytics${org_id}"
storage_account_id="/subscriptions/$subscription_id/resourceGroups/$resource_group/providers/Microsoft.Storage/storageAccounts/$storage_account"

synapse_workspace="syeduanalytics${org_id}"
user_object_id=$(az ad signed-in-user show --query objectId -o tsv)

# 1) Create the resource group
echo "--> Creating resource group: $resource_group"
az group create -l $location -n $resource_group

# 2) Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
echo "--> Creating storage account: steduanalytics${org_id}"
az storage account create --resource-group $resource_group --name steduanalytics${org_id} --location $location \
  --kind StorageV2 --sku Standard_RAGRS --enable-hierarchical-namespace true --access-tier Hot

echo "--> Creating storage account containers: stage1, stage2, stage3, synapse"
az storage container create --account-name $storage_account --name synapse --auth-mode login
az storage container create --account-name $storage_account --name stage1 --auth-mode login
az storage container create --account-name $storage_account --name stage2 --auth-mode login
az storage container create --account-name $storage_account --name stage3 --auth-mode login
az storage container create --account-name $storage_account --name test-env --auth-mode login

# 3) Create Synapse workspace, configure firewall access, and create spark pool
echo "--> Creating Synapse Workspace: $synapse_workspace"
temporary_password="$(openssl rand -base64 12)" # Generate random password (because sql-admin-login-password is required, but not used in this solution)
az synapse workspace create --name $synapse_workspace --resource-group $resource_group \
  --storage-account $storage_account --file-system synapse --location $location \
  --sql-admin-login-user eduanalyticsuser --sql-admin-login-password $temporary_password

echo "--> Creating firewall rule for accessing Synapse Workspace."
az synapse workspace firewall-rule create --name allowAll --workspace-name $synapse_workspace --resource-group $resource_group \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

echo "--> Creating spark pool."
az synapse spark pool create --name spark1 --workspace-name $synapse_workspace --resource-group $resource_group \
  --spark-version 2.4 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 10 \
  --enable-auto-scale true --delay 15 --enable-auto-pause true \
  --no-wait

#todo: determine why this is not working
#az synapse role assignment create --workspace-name $synapse_workspace --role "Apache Spark Admin" --assignee $user_object_id

# 4) Create security groups in AAD, and grant access to storage
echo "--> Creating security groups in Azure Active Directory."
az ad group create --display-name 'Edu Analytics Global Admins' --mail-nickname 'EduAnalyticsGlobalAdmins'
az ad group owner add --group 'Edu Analytics Global Admins' --owner-object-id $user_object_id

global_admins=$(az ad group show --group "Edu Analytics Global Admins" --query objectId --output tsv)

az ad group create --display-name 'Edu Analytics Data Scientists' --mail-nickname 'EduAnalyticsDataScientists'
az ad group owner add --group 'Edu Analytics Data Scientists' --owner-object-id $user_object_id
data_scientists=$(az ad group show --group "Edu Analytics Data Scientists" --query objectId --output tsv)

az ad group create --display-name 'Edu Analytics Data Engineers' --mail-nickname 'EduAnalyticsDataEngineers'
az ad group owner add --group 'Edu Analytics Data Engineers' --owner-object-id $user_object_id
data_engineers=$(az ad group show --group "Edu Analytics Data Engineers" --query objectId --output tsv)

az ad group create --display-name 'Edu Analytics External Data Scientists' --mail-nickname 'EduAnalyticsExternalDataScientists'
az ad group owner add --group 'Edu Analytics External Data Scientists' --owner-object-id $user_object_id
external_data_scientists=$(az ad group show --group "Edu Analytics External Data Scientists" --query objectId --output tsv)

echo "--> Creating role assignments for Edu Analytics Global Admins, Edu Analytics Data Scientists, and Edu Analytics Data Engineers."
az role assignment create --role "Owner" --assignee $global_admins --resource-group $resource_group
# Asssign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
az role assignment create --role "Storage Blob Data Contributor" --assignee $global_admins --scope $storage_account_id
az role assignment create --role "Storage Blob Data Contributor" --assignee $data_scientists --scope $storage_account_id
az role assignment create --role "Storage Blob Data Contributor" --assignee $data_engineers --scope $storage_account_id
# Assign limited access to specific containers for the external data scientists
stage3_id="/subscriptions/$subscription_id/resourceGroups/$resource_group/providers/Microsoft.Storage/storageAccounts/$storage_account/blobServices/default/containers/stage3"
az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $stage3_id
testdata_id="/subscriptions/$subscription_id/resourceGroups/$resource_group/providers/Microsoft.Storage/storageAccounts/$storage_account/blobServices/default/containers/test-env"
az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $testdata_id

# Setup is complete. Provide a link for user to jump to synapse studio.
workspace_url=$(az synapse workspace show --name $synapse_workspace --resource-group $resource_group | jq -r '.connectivityEndpoints | .web')
echo "--> Setup complete."
echo "Click on this url to open your Synapse Workspace: $workspace_url"
