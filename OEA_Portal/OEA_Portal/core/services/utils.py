import json
import os
from OEA_Portal.settings import CONFIG_DATABASE, BASE_DIR
import urllib.request
import zipfile
from OEA_Portal.auth.AzureClient import AzureClient
from OEA_Portal.core.models import *
from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient


def download_and_extract_zip_from_url(url, path=f'{BASE_DIR}/downloads'):
    """
    Downloads a zip file from an given URL into local file system path. If the parameter path is not passed, it defaults
    the destination location to /downloads folder in the root directory.
    """
    try:
        zip_path, _ = urllib.request.urlretrieve(url)
        with zipfile.ZipFile(zip_path, "r") as f:
            f.extractall(path)
        return path
    except:
        raise Exception(f"Unable to Download or Extract ZIP file from URL - {url}")

def get_config_data():
    """
    Returns the Tenant ID and Subscription ID of the given azure account from the config JSON.
    """
    with open(CONFIG_DATABASE) as f:
        data = json.load(f)
    return data

def update_config_database(target_data):
    """
    Updates the Tenant ID and Subscription ID in the config JSON.
    """
    with open(CONFIG_DATABASE) as f:
        data = json.load(f)
        for key in target_data:
            if(key in data): data[key] = target_data[key]
    with open(CONFIG_DATABASE, 'w') as f:
        f.write(json.dumps(data))

def get_blob_contents(azure_client:AzureClient, storage_account_name, blob_path):
    """
    Downloads and returns the contents of a blob in a given storage account.
    """
    container_name = blob_path.split('/')[0].replace('/', '')
    blob_name = '/'.join(blob_path.split('/')[1:])
    try:
        data = azure_client.get_blob_client(storage_account_name, container_name, blob_name)\
                .download_blob(max_concurrency=1, encoding='UTF-8').readall()
        data_json = json.loads(data)

    except:
        raise Exception(f'Unable to download blob from Storage account - {storage_account_name}')
    return data_json

# todo: Fix this method.
def upload_blob_contents(azure_client: AzureClient, storage_account, blob_path, data):
    """
    Uploads the given content to a blob in a storage account.
    """
    container_name = blob_path.split('/')[0].replace('/', '')
    blob_name = '/'.join(blob_path.split('/')[1:])
    try:
        azure_client.get_blob_service_client(storage_account, azure_client.credential)\
            .get_container_client(container=container_name)\
            .get_blob_client(blob_name).upload_blob(data, blob_type='BlockBlob')

    except:
        raise Exception(f'Unable to upload blob to Storage account - {storage_account}')

def get_all_subscriptions_in_tenant():
    """
    Returns list of subscriptions in a given tenant containing the id and name.
    """
    subscription_models = []
    credential = DefaultAzureCredential()
    subscriptions = SubscriptionClient(credential).subscriptions.list()
    for subscription in subscriptions:
        subscription_models.append(AzureSubscription(subscription.display_name, subscription.id))
    return subscription_models

def get_storage_account_from_url(account_url):
    return account_url.replace('.dfs.core.windows.net', '').replace('https://', '')

def get_all_workspaces_in_subscription(azure_client:AzureClient):
    """
    Returns the list of all workspaces in a given subscription.
    """
    workspace_models = []
    workspaces = azure_client.get_synapse_client().workspaces.list()
    for workspace in workspaces:
        resource_group = workspace.id.split('/')[4]
        storage_account = get_storage_account_from_url(workspace.default_data_lake_storage.account_url)
        workspace_models.append(SynapseWorkspace(workspace.name, resource_group, azure_client.subscription_id, storage_account))
    return workspace_models

def get_workspace_object(azure_client:AzureClient, workspace_name):
    """
    Returns the "SynapseWorkspace" model for a given workspace.
    """
    workspaces = azure_client.get_synapse_client().workspaces.list()
    try:
        workspace = next(workspace for workspace in workspaces if workspace.name == workspace_name)
    except:
        raise Exception(f"No workspace exists with the name - '{workspace_name}'")
    # raise error if workspace not found.
    resource_group = workspace.id.split('/')[4]
    storage_account = get_storage_account_from_url(workspace.default_data_lake_storage.account_url)
    return SynapseWorkspace(workspace_name, resource_group, azure_client.subscription_id, storage_account)

def is_oea_installed_in_workspace(azure_client:AzureClient, workspace_name, resource_group_name, linked_storage_account=None):
    """
    Returns True if OEA is installed in the workspace, else False.
    """
    if linked_storage_account is None:
        linked_storage_account = azure_client.get_synapse_client().workspaces.get(resource_group_name=resource_group_name, workspace_name=workspace_name).default_data_lake_storage.account_url.replace('.dfs.core.windows.net', '').replace('https://', '')
    keys = azure_client.get_storage_client().storage_accounts.list_keys(resource_group_name, linked_storage_account)
    return azure_client.get_datalake_client(linked_storage_account, keys.keys[0].value).get_directory_client(file_system='oea', directory=f'admin/workspaces/{workspace_name}').exists()

def get_installed_oea_version(azure_client: AzureClient, workspace_name, resource_group_name=None, storage_account=None):
    """
    Returns the OEA version installed in the workspace. If 'storage_account' parameter is None,
    we retrieve the linked storage account for the workspace.
    """
    if storage_account is None or resource_group_name is None:
        workspaces = azure_client.get_synapse_client().workspaces.list()
        try:
            workspace = next(workspace for workspace in workspaces if workspace.name == workspace_name)
        except:
            raise Exception(f"No workspace exists with the name - '{workspace_name}'")
        storage_account = get_storage_account_from_url(workspace.default_data_lake_storage.account_url)
        resource_group_name = workspace.id.split('/')[4]

    if is_oea_installed_in_workspace(azure_client, workspace_name, resource_group_name, storage_account) is False:
        raise Exception(f"OEA is not installed in the workspace - {workspace_name}")

    return get_blob_contents(azure_client, storage_account, f'oea/admin/workspaces/{workspace_name}/status.json')['OEA_Version']

def get_all_storage_accounts_in_subscription(azure_client:AzureClient):
    """
    Returns the list of all storage accounts in a given subscription.
    """
    return [x.name for x in azure_client.get_storage_client().storage_accounts.list()]



