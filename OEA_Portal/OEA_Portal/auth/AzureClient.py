import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.filedatalake import DataLakeServiceClient
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.resource import ResourceManagementClient
from azure.storage.blob import BlobClient, BlobServiceClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.synapse import SynapseManagementClient
from azure.synapse.artifacts import ArtifactsClient
from azure.mgmt.storage import StorageManagementClient

logger = logging.getLogger('AzureClient')

class AzureClient:
    """ todo: consider removing self.resource_group_name - it should probably be passed in as needed """
    def __init__(self, tenant_id, subscription_id, location = 'eastus', default_tags = None, resource_group_name = None):
        self.credential = DefaultAzureCredential()
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.location = location
        self.tags = default_tags if default_tags else {}
        self.resource_group_name = resource_group_name
        self.resource_group = None
        self.key_vault_client = None
        self.resource_client = None
        self.graph_rbac_client = None
        self.secret_client = None
        self.blob_service_client = None
        self.authorization_client = None
        self.blob_client = None
        self.storage_client = None
        self.artifacts_client = {}
        self.synapse_client = None
        self.datalake_client = None

    def get_authorization_client(self):
        # Note that we need to use at least version 2018-01-01-preview in order to be able to set the role assignments later,
        # otherwise we'll get an exception of type UnsupportedApiVersionForRoleDefinitionHasDataActions
        if not self.authorization_client: self.authorization_client = AuthorizationManagementClient(self.credential, self.subscription_id, api_version='2018-01-01-preview')
        return self.authorization_client

    def get_resource_client(self):
        if not self.resource_client: self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)
        return self.resource_client

    def get_key_vault_client(self):
        if not self.key_vault_client: self.key_vault_client = KeyVaultManagementClient(self.credential, self.subscription_id)
        return self.key_vault_client

    def get_secret_client(self, keyvault_name):
        if not self.secret_client: self.secret_client = SecretClient(f"https://{keyvault_name}.vault.azure.net", self.credential)
        return self.secret_client

    def get_datalake_client(self, storage_account_name, account_key):
        if not self.datalake_client: self.datalake_client = DataLakeServiceClient(account_url=f"https://{storage_account_name}.dfs.core.windows.net", credential={"account_name":storage_account_name, "account_key": account_key})
        return self.datalake_client

    def get_storage_client(self):
        if not self.storage_client: self.storage_client = StorageManagementClient(self.credential, self.subscription_id)
        return self.storage_client

    def get_synapse_client(self):
        if not self.synapse_client: self.synapse_client = SynapseManagementClient(self.credential, self.subscription_id)
        return self.synapse_client

    def get_artifacts_client(self, synapse_workspace_name) -> ArtifactsClient:
        if not synapse_workspace_name in self.artifacts_client:
            self.artifacts_client[synapse_workspace_name] = ArtifactsClient(self.credential, f"https://{synapse_workspace_name}.dev.azuresynapse.net")
        return self.artifacts_client[synapse_workspace_name]

    def get_blob_client(self, storage_account_name, container_name, blob_name):
        if not self.blob_client: self.blob_client = BlobClient(account_url=f"https://{storage_account_name}.dfs.core.windows.net", container_name=container_name, blob_name=blob_name, credential=self.credential)
        return self.blob_client

    def get_blob_service_client(self, storage_account_name, credential):
        if not self.blob_service_client: self.blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.dfs.core.windows.net", credential=credential)
        return self.blob_service_client

    def get_subscription_client(self):
        if not self.subscription_client: self.subscription_client = SubscriptionClient(self.credential)
        return self.subscription_client
