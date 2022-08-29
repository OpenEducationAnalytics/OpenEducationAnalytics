# need to run "pip install -r requirements.txt"
import sys
import string
import logging
import os
from datetime import datetime
from azure.core.exceptions import HttpResponseError
from AzureClient import AzureClient
from msrest.exceptions import ValidationError

_oea_suffix = 'mytest14'
_subscription_id = 'xxxx'
_location = 'westus'
_tenant_id = 'xxxx'
_resource_group_name = 'rg-oea-' + _oea_suffix
_synapse_workspace_name = 'syn-oea-' + _oea_suffix
_storage_account_name = 'stoea' + _oea_suffix
_key_vault_name = 'kv-oea-' + _oea_suffix
_app_insights_name = 'appi-oea-' + _oea_suffix

_user_object_id = os.popen("az ad signed-in-user show --query id -o tsv").read()[:-1] # the last char is a newline, so we strip that off
_oea_version = "0.4+"
_tags = {'oea_version':_oea_version}
_oea_path = '/home/global/clouddrive/OpenEduAnalytics'

# Info on logging in Azure python sdk: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='setup_oea_log_{:%Y_%m_%d__%H_%M}.log'.format(datetime.now()), level=logging.DEBUG)
# uncomment this for verbose messages to be sent to console
#logging.getLogger("").addHandler(logging.StreamHandler(sys.stdout))
logger = logging.getLogger('oea_setup')
logger.addHandler(logging.StreamHandler(sys.stdout))

_azure_client = AzureClient(_tenant_id, _subscription_id, _location, _tags, _resource_group_name)

def env_prep():
    # 0) Ensure that the resource providers are registered in the subscription (more info about this here: https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/error-register-resource-provider )
    os.system("az provider register --namespace 'Microsoft.Sql'")
    os.system("az provider register --namespace 'Microsoft.ManagedIdentity'")
    os.system("az provider register --namespace 'Microsoft.Storage'")
    os.system("az provider register --namespace 'Microsoft.KeyVault'")
    os.system("az provider register --namespace 'Microsoft.DataShare'")
    os.system("az provider register --namespace 'Microsoft.Synapse'")
    os.system("az provider register --namespace 'Microsoft.MachineLearningServices'")

    # and allow for az extensions to be installed as needed without prompting (extensions like azure-cli-ml and application-insights end up being installed)
    os.system("az config set extension.use_dynamic_install=yes_without_prompt")

#_azure_client.create_notebook('C:/repos/OpenEduAnalytics/infrastructure/python/new_notebook.json', _synapse_workspace_name)
logger.info("starting installation...")
# 1) Create the resource group
logger.info(f"--> 1) Creating resource group: {_resource_group_name}")
try:
  _azure_client.create_resource_group(_resource_group_name)
  #_azure_client.create_resource_group("this_is_a_test_$$_ ^^")
  _azure_client.resource_group_name = _resource_group_name
except ValidationError as e:
    logger.error('Validation Error - failed to create resource group: ' + str(e))
    exit()
#todo: check to make sure the creation of the resource group actually happened

# 2) Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
logger.info(f"--> 2) Creating storage account: {_storage_account_name}")
storage_account = _azure_client.create_storage_account(_storage_account_name)
logger.info("--> Creating storage account containers.")
#_azure_client.create_containers(_storage_account_name, ['oea-framework', 'synapse-workspace', 'stage1np', 'stage2np', 'stage2p', 'stage3np', 'stage3p'])

# 3) Create Synapse workspace, configure firewall access, and create spark pool
# todo: specify a name for the managed resource group that gets created
logger.info(f"--> 3) Creating Synapse Workspace: {_synapse_workspace_name} (this is usually the longest step - it may take 5 to 10 minutes to complete)")
synapse_workspace = _azure_client.create_synapse_workspace(_synapse_workspace_name, _storage_account_name)
# This permission is necessary to allow a data pipeline in Synapse to invoke notebooks.
# In order to set this permission, the user has to have the role assignment of "Owner" on the Azure subscription.
_azure_client.create_role_assignment('Storage Blob Data Contributor', storage_account.id, synapse_workspace.identity.principal_id)

logger.info("--> Creating firewall rule for accessing Synapse Workspace.")
_azure_client.add_firewall_rule_for_synapse('allowAll', '0.0.0.0', '255.255.255.255', _synapse_workspace_name)

logger.info("--> Creating spark pool.")
_azure_client.create_spark_pool(_synapse_workspace_name, "spark3p1sm")
library_requirements = f"{os.path.dirname(__file__)}/requirements.txt"
# todo: this doesn't seem to be working
#_azure_client.update_spark_pool_with_requirements(_synapse_workspace_name, "spark3p1sm", library_requirements)

# 4) Create key vault for secure storage of credentials, and create app insights for logger
logger.info(f"--> 4) Creating key vault: {_key_vault_name}")
access_policy_for_synapse = { 'tenant_id': _tenant_id, 'object_id': synapse_workspace.identity.principal_id, 
                              'permissions': { 'secrets': ['get'] } 
                            }
access_policy_for_user = { 'tenant_id': _tenant_id, 'object_id': _user_object_id,                
                           'permissions': { 'keys': ['all'], 'secrets': ['all'] }
                         }
_azure_client.create_key_vault(_key_vault_name, [access_policy_for_synapse, access_policy_for_user])

logger.info(f"--> Creating app-insights: {_app_insights_name}")
os.system(f"az monitor app-insights component create --app {_app_insights_name} --resource-group {_resource_group_name} --location {_location} --tags {_tags}")

if True:
  # 5) Create security groups in AAD, and grant access to storage
    logger.info("--> 5) Creating security groups in Azure Active Directory.")
    global_admins_name = 'Edu Analytics Global Admins'
    os.system(f"az ad group create --display-name '{global_admins_name}' --mail-nickname 'EduAnalyticsGlobalAdmins'")
    os.system(f"az ad group owner add --group '{global_admins_name}' --owner-object-id {_user_object_id}")
    global_admins_id = os.popen(f"az ad group show --group \"{global_admins_name}\" --query objectId --output tsv").read()[:-1]
    print(global_admins_id)

    ds_group_name = 'Edu Analytics Data Scientists'
    os.system(f"az ad group create --display-name '{ds_group_name}' --mail-nickname 'EduAnalyticsDataScientists'")
    os.system(f"az ad group owner add --group '{ds_group_name}' --owner-object-id {_user_object_id}")
    data_scientists_id = os.popen(f"az ad group show --group \"{ds_group_name}\" --query objectId --output tsv").read()[:-1]

    de_group_name = 'Edu Analytics Data Engineers'
    os.system(f"az ad group create --display-name '{de_group_name}' --mail-nickname 'EduAnalyticsDataEngineers'")
    os.system(f"az ad group owner add --group '{de_group_name}' --owner-object-id {_user_object_id}")
    data_engineers_id = os.popen(f"az ad group show --group \"{de_group_name}\" --query objectId --output tsv").read()[:-1]

    eds_group_name = 'Edu Analytics External Data Scientists'
    os.system(f"az ad group create --display-name '{eds_group_name}' --mail-nickname 'EduAnalyticsExternalDataScientists'")
    os.system(f"az ad group owner add --group '{eds_group_name}' --owner-object-id {_user_object_id}")
    external_data_scientists_id = os.popen(f"az ad group show --group \"{eds_group_name}\" --query objectId --output tsv").read()[:-1]

    logger.info("--> Creating role assignments for Edu Analytics Global Admins, Edu Analytics Data Scientists, and Edu Analytics Data Engineers.")
    os.system(f"az role assignment create --role \"Owner\" --assignee {global_admins_id} --resource-group {_resource_group_name}")
    # Assign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
    storage_account_id = f"/subscriptions/{_subscription_id}/resourceGroups/{_resource_group_name}/providers/Microsoft.Storage/storageAccounts/{_storage_account_name}"
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {global_admins_id} --scope {storage_account_id}")
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {data_scientists_id} --scope {storage_account_id}")
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {data_engineers_id} --scope {storage_account_id}")
    # Assign limited access to specific containers for the external data scientists
    stage2p_id = f"/subscriptions/{_subscription_id}/resourceGroups/{_resource_group_name}/providers/Microsoft.Storage/storageAccounts/{_storage_account_name}/blobServices/default/containers/stage2p"
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {external_data_scientists_id} --scope {stage2p_id}")
    stage3p_id = f"/subscriptions/{_subscription_id}/resourceGroups/{_resource_group_name}/providers/Microsoft.Storage/storageAccounts/{_storage_account_name}/blobServices/default/containers/stage3p"
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {external_data_scientists_id} --scope {stage3p_id}")
    oea_framework_id = f"/subscriptions/{_subscription_id}/resourceGroups/{_resource_group_name}/providers/Microsoft.Storage/storageAccounts/{_storage_account_name}/blobServices/default/containers/oea-framework"
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {external_data_scientists_id} --scope {oea_framework_id}")
    # Assign "Storage Blob Data Contributor" for the "synapse" container so that External Data Scientists can create spark db's against data they have prepared.
    synapse_container_id = f"/subscriptions/{_subscription_id}/resourceGroups/{_resource_group_name}/providers/Microsoft.Storage/storageAccounts/{_storage_account_name}/blobServices/default/containers/synapse"
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {external_data_scientists_id} --scope {synapse_container_id}")
    # Assign "Reader" access to the storage account so they can see the storage containers when browsing in synapse (this doesn't give access to the data in the containers)
    os.system(f"az role assignment create --role \"Reader\" --assignee {external_data_scientists_id} --scope {storage_account_id}")
else:
    # If security groups are not created, this user will need to have this role assignment to be able to query data from the storage account
    os.system(f"az role assignment create --role \"Storage Blob Data Contributor\" --assignee {_user_object_id} --scope {storage_account_id}")