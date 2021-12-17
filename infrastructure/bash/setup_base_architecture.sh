#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture. 
# Basic steps are:
# 1) create resource group
# 2) create storage account and storage containers (stage1, stage2, stage3, synapse)
# 3) create synapse workspace, configure firewall access, and create Spark pool
# 4) create keyvault instance and appinsights for logging
# 5) create security groups and assign them access to storage

org_id=$1
location=$2
include_groups=$3
subscription_id=$4
oea_path=$5
logfile=$6
storage_account_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT"
user_object_id=$(az ad signed-in-user show --query objectId -o tsv)

# 0) Ensure that the resource providers are registered in the subscription (more info about this here: https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/error-register-resource-provider )
az provider register --namespace 'Microsoft.Sql'
az provider register --namespace 'Microsoft.ManagedIdentity'
az provider register --namespace 'Microsoft.Storage'
az provider register --namespace 'Microsoft.KeyVault'
az provider register --namespace 'Microsoft.DataShare'
az provider register --namespace 'Microsoft.Synapse'
az provider register --namespace 'Microsoft.MachineLearningServices'

# and allow for az extensions to be installed as needed without prompting (extensions like azure-cli-ml and application-insights end up being installed)
az config set extension.use_dynamic_install=yes_without_prompt

# In some cases, the correct extensions are not installed. Forcing
az extension add --name azure-cli-ml

# 1) Create the resource group
echo "--> 1) Creating resource group: $OEA_RESOURCE_GROUP"
echo "--> 1) Creating resource group: $OEA_RESOURCE_GROUP" 1>&3
az group create -l $location -n $OEA_RESOURCE_GROUP --tags oea_version=$OEA_VERSION
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

# 2) Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
echo "--> 2) Creating storage account: ${OEA_STORAGE_ACCOUNT}"
echo "--> 2) Creating storage account: ${OEA_STORAGE_ACCOUNT}" 1>&3
az storage account create --resource-group $OEA_RESOURCE_GROUP --name ${OEA_STORAGE_ACCOUNT} --location $location --tags oea_version=$OEA_VERSION $OEA_ADDITIONAL_TAGS \
  --kind StorageV2 --sku Standard_RAGRS --enable-hierarchical-namespace true --access-tier Hot --default-action Allow
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

echo "--> Creating storage account containers."
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name synapse-workspace --auth-mode login
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name oea-framework --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage1np --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage2np --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage2p --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage3np --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage3p --auth-mode login

# 3) Create Synapse workspace, configure firewall access, and create spark pool
# todo: specify a name for the managed resource group that gets created
# todo: see if it's still necessary to specify a random pwd for sql (it's not necessary when creating manually in portal)
echo "--> 3) Creating Synapse Workspace: $OEA_SYNAPSE (this is usually the longest step - it may take 5 to 10 minutes to complete)"
echo "--> 3) Creating Synapse Workspace: $OEA_SYNAPSE (this is usually the longest step - it may take 5 to 10 minutes to complete)" 1>&3
temporary_password="$(openssl rand -base64 12)" # Generate random password (because sql-admin-login-password is required, but not used in this solution)
az synapse workspace create --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP --tags oea_version=$OEA_VERSION $OEA_ADDITIONAL_TAGS \
  --storage-account $OEA_STORAGE_ACCOUNT --file-system synapse-workspace --location $location \
  --sql-admin-login-user eduanalyticsuser --sql-admin-login-password $temporary_password
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

# This permission is necessary to allow a data pipeline in Synapse to invoke notebooks.
# In order to set this permission, the user has to have the role assignment of "Owner" on the Azure subscription.
synapse_principal_id=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP --query identity.principalId -o tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $synapse_principal_id --scope $storage_account_id

echo "--> Creating firewall rule for accessing Synapse Workspace."
az synapse workspace firewall-rule create --name allowAll --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

echo "--> Creating spark pool."
az synapse spark pool create --name spark3p1sm --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP \
  --spark-version 3.1 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 5 \
  --enable-auto-scale true --delay 15 --enable-auto-pause true --tags oea_version=$OEA_VERSION $OEA_ADDITIONAL_TAGS
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

echo "--> Update spark pool to include required libraries (note that this has to be done as a separate step or the create command will fail, despite what the docs say)."
az synapse spark pool update --name spark3p1sm --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP --library-requirements $oea_path/framework/requirements.txt
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

# 4) Create key vault for secure storage of credentials, and create app insights for logging
echo "--> 4) Creating key vault: ${OEA_KEYVAULT}"
echo "--> 4) Creating key vault: ${OEA_KEYVAULT}" 1>&3
az keyvault create --name $OEA_KEYVAULT --resource-group $OEA_RESOURCE_GROUP --location $location --tags oea_version=$OEA_VERSION $OEA_ADDITIONAL_TAGS
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }
# give the Synapse workspace access to list and get secrets from the key vault, for use in Synapse pipelines
az keyvault set-policy -n $OEA_KEYVAULT --secret-permissions get list --object-id $synapse_principal_id
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

echo "--> Creating app-insights: $OEA_APP_INSIGHTS"
az monitor app-insights component create --app $OEA_APP_INSIGHTS --resource-group $OEA_RESOURCE_GROUP --location $location --tags oea_version=$OEA_VERSION $OEA_ADDITIONAL_TAGS
[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }

keyvault_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.KeyVault/vaults/$OEA_KEYVAULT"
app_insights_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/microsoft.insights/components/$OEA_APP_INSIGHTS"


if [ "$include_groups" == "true" ]; then
  # 5) Create security groups in AAD, and grant access to storage
  echo "--> 5) Creating security groups in Azure Active Directory."
  echo "--> 5) Creating security groups in Azure Active Directory." 1>&3
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
  az role assignment create --role "Owner" --assignee $global_admins --resource-group $OEA_RESOURCE_GROUP
  # Assign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
  az role assignment create --role "Storage Blob Data Contributor" --assignee $global_admins --scope $storage_account_id
  az role assignment create --role "Storage Blob Data Contributor" --assignee $data_scientists --scope $storage_account_id
  az role assignment create --role "Storage Blob Data Contributor" --assignee $data_engineers --scope $storage_account_id
  # Assign limited access to specific containers for the external data scientists
  stage2p_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/stage2p"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $stage2p_id
  stage3p_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/stage3p"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $stage3p_id
  oea_framework_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/oea-framework"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $oea_framework_id
  # Assign "Storage Blob Data Contributor" for the "synapse" container so that External Data Scientists can create spark db's against data they have prepared.
  synapse_container_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/synapse"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $synapse_container_id
  # Assign "Reader" access to the storage account so they can see the storage containers when browsing in synapse (this doesn't give access to the data in the containers)
  az role assignment create --role "Reader" --assignee $external_data_scientists --scope $storage_account_id

else
  # If security groups are not created, this user will need to have this role assignment to be able to query data from the storage account
  az role assignment create --role "Storage Blob Data Contributor" --assignee $user_object_id --scope $storage_account_id
fi
