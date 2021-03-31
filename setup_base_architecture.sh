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

this_file_path=$(dirname $(realpath $0))

#read -p 'Enter an org id, using only letters and numbers (eg, ContosoISD3): ' org_id
org_id=$1
org_id_lowercase=${org_id,,}
source $this_file_path/set_names.sh $org_id
#read -p 'Enter the location for the Azure resources to be create in (eg, eastus, westus, northeurope) [eastus]: ' location
location=$2
location=${location:-eastus}
include_groups=$3
include_groups=${include_groups,,}
include_groups=${include_groups:-false}

subscription_id=$(az account show --query id -o tsv)
storage_account_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT"
user_object_id=$(az ad signed-in-user show --query objectId -o tsv)

# Verify that the specified org_id is not too long and doesn't have invalid characters
if [[ ${#org_id} -gt 12 || ! $org_id =~ ^[a-zA-Z0-9]+$ ]]; then
  echo "Invalid suffix: $org_id"
  echo "The chosen suffix must be less than 12 characters, and must contain only letters and numbers."
  exit 1
fi

# Verify that the user has the Owner role assignment
roles=$(az role assignment list --subscription $subscription_id --query [].roleDefinitionName -o tsv)
if [[ ! " ${roles[@]} " =~ "Owner" ]]; then
  echo "You do not have the role assignment of Owner on this subscription."
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription"
  exit 1
fi

# Create a tmp dir in order to write notebooks to for easier importing (this can be removed once the automated provisioning of notebooks is fixed)
mkdir $this_file_path/tmp

# 0) Ensure that the resource providers are registered in the subscription (more info about this here: https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/error-register-resource-provider )
az provider register --namespace 'Microsoft.DataFactory'
az provider register --namespace 'Microsoft.Sql'
az provider register --namespace 'Microsoft.ManagedIdentity'
az provider register --namespace 'Microsoft.Storage'
az provider register --namespace 'Microsoft.KeyVault'
az provider register --namespace 'Microsoft.DataShare'
az provider register --namespace 'Microsoft.Synapse'
az provider register --namespace 'Microsoft.MachineLearningServices'

# 1) Create the resource group
echo "--> Creating resource group: $OEA_RESOURCE_GROUP"
az group create -l $location -n $OEA_RESOURCE_GROUP

# 2) Create a budget for the resource group with an alert
email=$(az ad signed-in-user show --query mail -o tsv)
echo "--> Creating budget ($OEA_BUDGET) with alerts configured to be sent to: $email"
# make the start date be the current month, but use the first day of the month to satisfy the API, and make the end date be 10 years later
start_date=$(date +"%Y-%m-01")
end_date=`date '+%Y-%m-%d' -d "$start_date+10 years"`
request="https://management.azure.com/subscriptions/${subscription_id}/resourceGroups/${OEA_RESOURCE_GROUP}/providers/Microsoft.Consumption/budgets/${OEA_BUDGET}?api-version=2019-10-01"
body=$(cat <<EOF
{
  "properties": {
    "category": "Cost",
    "amount": 100,
    "timeGrain": "Monthly",
    "timePeriod": {"startDate": "${start_date}","endDate": "${end_date}"},
    "notifications": {
      "Actual_Exceeds_Threshold": {
        "enabled": true,
        "operator": "GreaterThan",
        "threshold": 100,
        "contactEmails": ["${email}"],
        "contactRoles": ["Contributor","Owner"],
        "thresholdType": "Actual"
      }  
    }
  }
}
EOF
)
# strip spaces and newline chars
body=${body//[$'\t\r\n ']}
az rest --method PUT --uri $request --body $body


# 3) Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
echo "--> Creating storage account: ${OEA_STORAGE_ACCOUNT}"
az storage account create --resource-group $OEA_RESOURCE_GROUP --name ${OEA_STORAGE_ACCOUNT} --location $location \
  --kind StorageV2 --sku Standard_RAGRS --enable-hierarchical-namespace true --access-tier Hot --default-action Allow

echo "--> Creating storage account containers: stage1, stage2, stage3, synapse"
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name synapse --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage1 --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage2 --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name stage3 --auth-mode login
az storage container create --account-name $OEA_STORAGE_ACCOUNT --name test-env --auth-mode login

# 4) Create Synapse workspace, configure firewall access, and create spark pool
echo "--> Creating Synapse Workspace: $OEA_SYNAPSE"
temporary_password="$(openssl rand -base64 12)" # Generate random password (because sql-admin-login-password is required, but not used in this solution)
az synapse workspace create --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP \
  --storage-account $OEA_STORAGE_ACCOUNT --file-system synapse --location $location \
  --sql-admin-login-user eduanalyticsuser --sql-admin-login-password $temporary_password

# This permission is necessary to allow a data pipeline in Synapse to invoke notebooks.
# In order to set this permission, the user has to have the role assignment of "Owner" on the Azure subscription.
synapse_principal_id=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP --query identity.principalId -o tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $synapse_principal_id --scope $storage_account_id

echo "--> Creating firewall rule for accessing Synapse Workspace."
az synapse workspace firewall-rule create --name allowAll --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP \
  --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

echo "--> Creating spark pool."
az synapse spark pool create --name spark1 --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP \
  --spark-version 2.4 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 10 \
  --enable-auto-scale true --delay 15 --enable-auto-pause true \
  --no-wait

# 5) Create data factory instance
echo "--> Creating data factory instance: ${OEA_DATA_FACTORY}"

# Now provision the Data Factory instance.
# Must use the REST API to provision the Data Factory in order to have it created with a Managed Identity, so that an access policy can be created to allow the Data Factory to access secrets in the key vault.
request="https://management.azure.com/subscriptions/${subscription_id}/resourceGroups/${OEA_RESOURCE_GROUP}/providers/Microsoft.DataFactory/factories/${OEA_DATA_FACTORY}?api-version=2018-06-01"
body=$(cat <<EOF
{
  "name":"${OEA_DATA_FACTORY}",
  "location":"${location}",
  "properties":{},
  "identity":{"type":"SystemAssigned"}
}
EOF
)
body=${body//[$'\t\r\n ']}
az rest --method PUT --uri $request --body $body
# This approach for provisioning ADF is more straightforward, but it doesn't support the creation of a managed identity. We'll revert to this approach once that feature is supported.
# az datafactory factory create --name $OEA_DATA_FACTORY --resource-group $OEA_RESOURCE_GROUP --location $location

# Give Data factory access to the data lake via the Managed Instance id
adf_id=$(az datafactory factory show --factory-name $OEA_DATA_FACTORY --resource-group $OEA_RESOURCE_GROUP --query identity.principalId -o tsv)
az role assignment create --role "Storage Blob Data Contributor" --assignee $adf_id --scope $storage_account_id
# Add a linked service to the Data factory that links to the data lake
properties='{"type":"AzureBlobFS","typeProperties":{"url":"https://'"${OEA_STORAGE_ACCOUNT}"'.dfs.core.windows.net"}}'
az datafactory linked-service create --factory-name $OEA_DATA_FACTORY --properties $properties --name $OEA_STORAGE_ACCOUNT --resource-group $OEA_RESOURCE_GROUP

# 6) Create machine learning resources (storage, keyvault, app insights, ml workspace)
echo "--> Creating storage account for ML workspace: ${OEA_ML_STORAGE_ACCOUNT}"
az storage account create --resource-group $OEA_RESOURCE_GROUP --name ${OEA_ML_STORAGE_ACCOUNT} --location $location \
  --kind StorageV2 --sku Standard_LRS --access-tier Hot --default-action Allow

echo "--> Creating key vault: ${OEA_KEYVAULT}"
az keyvault create --name $OEA_KEYVAULT --resource-group $OEA_RESOURCE_GROUP --location $location
# give the Data factory access to get secrets from the key vault, so that integration pipelines can retrieve credentials kept in the key vault
az keyvault set-policy -n $OEA_KEYVAULT --secret-permissions get --object-id $adf_id

echo "--> Creating app-insights: $OEA_APP_INSIGHTS"
az monitor app-insights component create --app $OEA_APP_INSIGHTS --resource-group $OEA_RESOURCE_GROUP --location $location

ml_storage_account_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_ML_STORAGE_ACCOUNT"
keyvault_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.KeyVault/vaults/$OEA_KEYVAULT"
app_insights_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/microsoft.insights/components/$OEA_APP_INSIGHTS"
az ml workspace create --workspace-name $OEA_ML_WORKSPACE --resource-group $OEA_RESOURCE_GROUP --location $location \
  --storage-account $ml_storage_account_id --keyvault $keyvault_id --app $app_insights_id


if [ "$include_groups" == "true" ]; then
  # 7) Create security groups in AAD, and grant access to storage
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
  az role assignment create --role "Owner" --assignee $global_admins --resource-group $OEA_RESOURCE_GROUP
  # Assign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
  az role assignment create --role "Storage Blob Data Contributor" --assignee $global_admins --scope $storage_account_id
  az role assignment create --role "Storage Blob Data Contributor" --assignee $data_scientists --scope $storage_account_id
  az role assignment create --role "Storage Blob Data Contributor" --assignee $data_engineers --scope $storage_account_id
  # Assign limited access to specific containers for the external data scientists
  stage3_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/stage3"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $stage3_id
  testdata_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/test-env"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $testdata_id
  # Assign "Storage Blob Data Contributor" for the "synapse" container so that External Data Scientists can create spark db's against data they have prepared.
  synapse_container_id="/subscriptions/$subscription_id/resourceGroups/$OEA_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$OEA_STORAGE_ACCOUNT/blobServices/default/containers/synapse"
  az role assignment create --role "Storage Blob Data Contributor" --assignee $external_data_scientists --scope $synapse_container_id

else
  # If security groups are not created, this user will need to have this role assignment to be able to query data from the storage account
  az role assignment create --role "Storage Blob Data Contributor" --assignee $user_object_id --scope $storage_account_id
fi

# Setup is complete. Provide a link for user to jump to synapse studio.
workspace_url=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP | jq -r '.connectivityEndpoints | .web')
echo "--> Setup complete."
echo "Click on this url to open your Synapse Workspace: $workspace_url"
