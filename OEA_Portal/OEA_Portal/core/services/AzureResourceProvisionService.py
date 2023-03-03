import secrets
import string
import logging
from uuid import uuid4
from OEA_Portal.auth.AzureClient import AzureClient
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.v2018_09_01_preview import models as authorization_model
from azure.core.exceptions import ResourceExistsError
from azure.mgmt.synapse.models import DataLakeStorageAccountDetails, ManagedIdentity

logger = logging.getLogger('AzureResourceProvisionService')

class AzureResourceProvisionService:
    """
    This class contains all the necessary capabilities to provision the required
    assets in the Azure Portal for the OEA framework to be running seamlessly.
    """
    def __init__(self, azure_client:AzureClient):
        self.azure_client = azure_client

    def delete_resource_group(self, name):
        """ Deletes the given resource group from the subscription. """
        self.azure_client.get_resource_client().resource_groups.begin_delete(name)

    def create_resource_group(self, resource_group_name, tags=None):
        """ Creates an empty resource group in the Azure Subscription """
        if not tags: tags = {}
        result = self.azure_client.get_resource_client().resource_groups.create_or_update(resource_group_name, {'location': self.azure_client.location, 'tags': tags})


    def create_key_vault(self, key_vault_name, resource_group_name, access_policies):
        """ Creates a keyvault with the given name and access policies, waits for the creation to finish an returns the keyvault object """
        poller = self.azure_client.get_key_vault_client().vaults.begin_create_or_update(resource_group_name, key_vault_name,
            {
                'location': self.azure_client.location,
                'properties': {
                    'sku': { 'name': 'standard', 'family': 'A' },
                    'tenant_id': self.azure_client.tenant_id,
                    'access_policies': access_policies
                }
            }
        )
        return poller.result()

    def create_secret_in_keyvault(self, keyvault_name, secret_name, secret_value):
        """ Creates or updates a secret in the keyvault with the given value """
        self.azure_client.get_secret_client(keyvault_name).set_secret(secret_name, secret_value)

    def list_resources_in_resource_group(self, resource_group_name):
        """ Retuns a csv string listing all of the resources in the given resource group. """
        resource_list = self.azure_client.get_resource_client().resources.list_by_resource_group(resource_group_name, expand = 'createdTime,changedTime')
        resources = "name,resource_type,created_time,changed_time\n"
        for resource in list(resource_list):
            resources += f"{resource.name},{resource.type},{str(resource.created_time)}{str(resource.changed_time)}\n"
        return resources

    def create_synapse_workspace(self, synapse_workspace_name, resource_group_name, storage_account_name):
        """ Creates a Synapse workspace, waits for the creation to finish and returns the synapse workspace object """
        default_data_lake_storage = DataLakeStorageAccountDetails(account_url=f"https://{storage_account_name}.dfs.core.windows.net", filesystem="oea")

        poller = self.azure_client.get_synapse_client().workspaces.begin_create_or_update(resource_group_name, synapse_workspace_name,
            {
                "location" : self.azure_client.location,
                "tags" : self.azure_client.tags,
                "identity" : ManagedIdentity(type="SystemAssigned"),
                "default_data_lake_storage" : default_data_lake_storage,
                "sql_administrator_login" : "eduanalyticsuser",
                "sql_administrator_login_password" : AzureResourceProvisionService.create_random_password(),
            }
        )
        return poller.result()

    def create_storage_account(self, storage_account_name, resource_group_name):
        """ Create a storage account, waits for the creation to complete and returns the storage account object """
        storage_client = self.azure_client.get_storage_client()
        poller = storage_client.storage_accounts.begin_create(resource_group_name, storage_account_name,
            {
                "location" : self.azure_client.location,
                "tags" : self.azure_client.tags,
                "kind": "StorageV2",
                "sku": {"name": "Standard_RAGRS"},
                "is_hns_enabled": True,
                "access-tier": "Hot",
                "default-action": "Allow"
            }
        )
        account_result = poller.result()
        return account_result

    def create_containers_and_directories(self, storage_account_name, resource_group_name, container_names, directory_list):
        """ Creates the given containers and directories in a given storage account """
        storage_client = self.azure_client.get_storage_client()
        keys = storage_client.storage_accounts.list_keys(resource_group_name, storage_account_name)
        for name in container_names:
            container = storage_client.blob_containers.create(resource_group_name, storage_account_name, name, {})
            for directory_path in ['/'.join(x.split('/')[1:]) for x in directory_list if x.split('/')[0] == name]:
                logger.info(directory_path)
                self.azure_client.get_datalake_client(storage_account_name, keys.keys[0].value).get_file_system_client(name).create_directory(directory_path)

    def get_role(self, role_name, resource_id):
        auth_client = AuthorizationManagementClient(self.azure_client.credential, self.azure_client.subscription_id)
        # Get built-in role as a RoleDefinition object
        roles = list(auth_client.role_definitions.list(resource_id, filter="roleName eq '{}'".format(role_name)))
        return roles[0]

    def create_role_assignment(self, role_name, resource_id, principal_id):
        """ Creates a role assignment for an Azure resource for a given Service Principal """
        role = self.get_role(role_name, resource_id)
        try:
            self.azure_client.get_authorization_client().role_assignments.create(resource_id, uuid4(),
                authorization_model.RoleAssignmentCreateParameters(
                    role_definition_id=role.id,
                    principal_id=principal_id)
            )
        except ResourceExistsError as e:
            logger.info(f"The {role_name} role assignment already exists for {principal_id} on resource {resource_id}.")

    def create_random_password():
        """ Creates a random password using secrets module """
        password = secrets.choice(string.ascii_uppercase) + secrets.choice(string.digits) + secrets.choice(['*', '%', '#', '@'])
        for _ in range(9): password += secrets.choice(string.ascii_lowercase)
        return password