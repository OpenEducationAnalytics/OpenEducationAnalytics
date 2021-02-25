#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture. 
# Basic steps are:
# 1) create resource group
# 2) create storage account and storage containers (stage1, stage2, stage3, synapse)
# 3) create synapse workspace, configure firewall access, and create Spark pool
# 4) create security groups and assign them access to storage

if [ $# -ne 1 ] && [ $# -ne 2 ] && [ $# -ne 3 ]; then
    echo "This setup script will install the Open Edu Analytics base architecture."
    echo ""
    echo "Invoke this script like this:  "
    echo "    setup.sh <mysuffix>"
    echo "where mysuffix is a suffix representing your organization (eg, CISD3). This value must be 12 characters or less (consider using an abbreviation) and must contain only letters and/or numbers."
    echo ""
    echo "By default, the Azure resources will be provisioned in the East US location."
    echo "If you want to have the resources provisioned in an alternate location, invoke the script like this: "
    echo "    setup.sh <mysuffix> <location>"
    echo "where mysuffix is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope)."
    echo ""
    echo "If you have Global Admin rights for the tenant associated with your Azure subscription, and you want to have the script setup security groups to facilitate the management of role based access control, you can invoke the script like this:"
    echo "You can opt to create a set of resources (eg, for a test env) without setting up the security groups like this:"
    echo "    setup.sh <mysuffix> <location> true"
    echo "where mysuffix is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope), and true specifies that security groups should be created."
    exit 1
fi
#read -p 'Enter an org id, using only letters and numbers (eg, ContosoISD3): ' org_id
org_id=$1
org_id_lowercase=${org_id,,}
#read -p 'Enter the location for the Azure resources to be create in (eg, eastus, westus, northeurope) [eastus]: ' location
location=$2
location=${location:-eastus}
include_groups=$3
include_groups=${include_groups,,}
include_groups=${include_groups:-false}

resource_group="EduAnalytics${org_id}"
subscription_id=$(az account show --query id -o tsv)
storage_account="steduanalytics${org_id_lowercase}"
storage_account_id="/subscriptions/$subscription_id/resourceGroups/$resource_group/providers/Microsoft.Storage/storageAccounts/$storage_account"

synapse_workspace="syeduanalytics${org_id_lowercase}"
user_object_id=$(az ad signed-in-user show --query objectId -o tsv)

# Verify that the user has the Owner role assignment
roles=$(az role assignment list --subscription $subscription_id --query [].roleDefinitionName -o tsv)
if [[ ! " ${roles[@]} " =~ "Owner" ]]; then
  echo "You do not have the role assignment of Owner on this subscription."
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription"
  exit 1
fi

# Create a tmp dir in order to write notebooks to for easier importing (this can be removed once the automated provisioning of notebooks is fixed)
this_file_path=$(dirname $(realpath $0))
mkdir $this_file_path/tmp

# 1) Create the resource group
echo "--> Creating resource group: $resource_group"
az group create -l $location -n $resource_group

# 2) Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
echo "--> Creating storage account: ${storage_account}"
az storage account create --resource-group $resource_group --name ${storage_account} --location $location \
  --kind StorageV2 --sku Standard_RAGRS --enable-hierarchical-namespace true --access-tier Hot --default-action Allow

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

# This permission is necessary to allow a data pipeline in Synapse to invoke notebooks.
# In order to set this permission, the user has to have the role assignment of "Owner" on the Azure subscription.
synapse_principal_id=$(az synapse workspace show --name $synapse_workspace --resource-group $resource_group --query identity.principalId -o tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $synapse_principal_id --scope $storage_account_id

echo "--> Creating firewall rule for accessing Synapse Workspace."
az synapse workspace firewall-rule create --name allowAll --workspace-name $synapse_workspace --resource-group $resource_group \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

echo "--> Creating spark pool."
az synapse spark pool create --name spark1 --workspace-name $synapse_workspace --resource-group $resource_group \
  --spark-version 2.4 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 10 \
  --enable-auto-scale true --delay 15 --enable-auto-pause true \
  --no-wait

if [ "$include_groups" == "true" ]; then
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

else
  # If security groups are not created, this user will need to have this role assignment to be able to query data from the storage account
  az role assignment create --role "Storage Blob Data Contributor" --assignee $user_object_id --scope $storage_account_id

fi

# Setup is complete. Provide a link for user to jump to synapse studio.
workspace_url=$(az synapse workspace show --name $synapse_workspace --resource-group $resource_group | jq -r '.connectivityEndpoints | .web')
echo "--> Setup complete."
echo "Click on this url to open your Synapse Workspace: $workspace_url"
