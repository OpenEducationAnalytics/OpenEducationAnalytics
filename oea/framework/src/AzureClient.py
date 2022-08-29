# need to run "pip install -r requirements.txt"
#import sys
#import secrets
#import string
#import logging
#import os, random
#import json
#import time
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.synapse import SynapseManagementClient
from azure.synapse.artifacts import ArtifactsClient
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import HttpResponseError

class AzureClient:
    """ todo: consider removing self.resource_group_name and self.storage_account_name - those should probably be passed in as needed """
    def __init__(self, tenant_id, subscription_id, location, default_tags = None, resource_group_name = None):
        self.credential = AzureCliCredential()
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.location = location
        self.tags = default_tags if default_tags else {}
        self.resource_group_name = resource_group_name
        self.key_vault_client = None
        self.resource_client = None
        self.storage_client = None
        self.artifacts_client = {}
        self.synapse_client = None
        self.storage_account_name = None

    def get_storage_account_id(self):
        return f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.Storage/storageAccounts/{self.storage_account_name}"

    def get_resource_client(self):
        if not self.resource_client: self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)
        return self.resource_client

    def get_key_vault_client(self):
        if not self.key_vault_client: self.key_vault_client = KeyVaultManagementClient(self.credential, self.subscription_id)
        return self.key_vault_client

    def get_storage_client(self):
        if not self.storage_client: self.storage_client = StorageManagementClient(self.credential, self.subscription_id)
        return self.storage_client

    def get_synapse_client(self):
        if not self.synapse_client: self.synapse_client = SynapseManagementClient(self.credential, self.subscription_id)
        return self.synapse_client

    def get_artifacts_client(self, synapse_workspace_name):
        if not synapse_workspace_name in self.artifacts_client:
            self.artifacts_client[synapse_workspace_name] = ArtifactsClient(self.credential, f"https://{synapse_workspace_name}.dev.azuresynapse.net")
        return self.artifacts_client[synapse_workspace_name]        

    # ref info: https://docs.microsoft.com/en-us/python/api/azure-mgmt-keyvault/azure.mgmt.keyvault.keyvaultmanagementclient?view=azure-python#vaults
    # example: https://docs.microsoft.com/en-us/samples/azure-samples/resource-manager-python-resources-and-groups/manage-azure-resources-and-resource-groups-with-python/#create-resource
    def create_key_vault(self, key_vault_name, access_policies):
        #availability_result = self.get_key_vault_client().vaults.check_name_availability({ "name": key_vault_name }  )
        #if not availability_result.name_available:
        #    logger.error(f"Key Vault name {key_vault_name} is not available. Try another name.")
        #    exit()
        
        poller = self.get_key_vault_client().vaults.begin_create_or_update(self.resource_group_name, key_vault_name,
            {
                'location': self.location,
                'properties': {
                    'sku': { 'name': 'standard', 'family': 'A' },
                    'tenant_id': self.tenant_id,
                    'access_policies': access_policies
                }
            }
    )

    def create_notebook_with_ipynb(self, notebook_name, notebook_filename, synapse_workspace_name):
        # todo: remove hardcoded url - this is just an example
        with open(notebook_filename) as f: 
            notebook_dict = json.load(f)
        artifacts_client = self.get_artifacts_client(synapse_workspace_name)
        poller = artifacts_client.notebook.begin_create_or_update_notebook(notebook_name, {'name':notebook_name, 'properties':notebook_dict} )
        return poller

    def create_notebook(self, notebook_filename, synapse_workspace_name):
        """ Creates synapse notebook from json (using the json from git when Synapse studio is connected to a repo) """
        artifacts_client = ArtifactsClient(AzureCliCredential(), f"https://{synapse_workspace_name}.dev.azuresynapse.net")
        with open(notebook_filename) as f: notebook_dict = json.load(f)
        validate_notebook_json(notebook_dict)
        logger.info("Creating notebook: notebook_dict['name']")
        poller = artifacts_client.notebook.begin_create_or_update_notebook(notebook_dict['name'], notebook_dict)
        return poller #AzureOperationPoller

    def validate_notebook_json(self, nb_json):
        """ These attributes must exist for the call to begin_create_or_update_notebook to pass validation """
        if not 'nbformat' in nb_json: nb_json['properties']['nbformat'] = 4
        if not 'nbformat_minor' in nb_json: nb_json['properties']['nbformat_minor'] = 2
        for cell in nb_json['properties']['cells']:
            if not 'metadata' in cell: cell['metadata'] = {}

    def create_spark_pool(self):
        pass

    #create_notebook('new_notebook.json', 'syn-oea-cisdggv04r')

    def delete_resource_group(self, name):
        self.get_resource_client().resource_groups.begin_delete(name)
        self.resource_group_name = None

    def create_resource_group(self, resource_group_name, tags=None):
        if not tags: tags = {}
        self.get_resource_client().resource_groups.create_or_update(resource_group_name, {'location': self.location, 'tags': tags})
        self.resource_group_name = resource_group_name

    def create_synapse_workspace(self, synapse_workspace_name, storage_account_name):
        """ https://docs.microsoft.com/en-us/python/api/azure-mgmt-synapse/azure.mgmt.synapse.aio.operations.workspacesoperations?view=azure-python#begin-create-or-update-resource-group-name--str--workspace-name--str--workspace-info--azure-mgmt-synapse-models--models-py3-workspace----kwargs-----azure-core-polling--async-poller-asynclropoller--forwardref---models-workspace--- """
        # https://docs.microsoft.com/en-us/python/api/azure-mgmt-synapse/azure.mgmt.synapse.aio.operations.workspacesoperations?view=azure-python
        cmd = (f"az synapse workspace create --name {synapse_workspace_name} --resource-group {self.resource_group_name} --tags oea_version=0.4+ "
          f"--storage-account {storage_account_name} --file-system synapse-workspace --location {self.location} "
          f"--sql-admin-login-user oea-admin --sql-admin-login-password {AzureClient.create_random_password()}")
        os.system(cmd)

    def create_storage_account(self, storage_account_name):
        storage_client = self.get_storage_client()
        # Check if the account name is available.
        #availability_result = storage_client.storage_accounts.check_name_availability({ "name": storage_account_name })
        #if not availability_result.name_available:
            #logger.error(f"Storage name {storage_account_name} is already in use. Try another name.")
            #exit()

        poller = storage_client.storage_accounts.begin_create(self.resource_group_name, storage_account_name,
            {           
                "location" : self.location,
                "tags" : self.tags,
                "kind": "StorageV2",
                "sku": {"name": "Standard_RAGRS"},
                "enable-hierarchical-namespace": True,
                "access-tier": "Hot",
                "default-action": "Allow"
            }
        )
        # Call poller.result() to wait for completion
        account_result = poller.result()
        self.storage_account_name = storage_account_name
        return account_result

    def create_containers(self, storage_account_name, container_names):
        storage_client = self.get_storage_client()
        keys = storage_client.storage_accounts.list_keys(self.resource_group_name, storage_account_name)
        conn_string = f"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName={storage_account_name};AccountKey={keys.keys[0].value}"
        # Provision the containers in the account (this call is synchronous)
        for name in container_names:
            container = storage_client.blob_containers.create(self.resource_group_name, storage_account_name, name, {})

    def create_linked_service(self):
        #os.system("az synapse linked-service create --workspace-name syn-oea-cisdggv04r --name MSGraphAPI2 --file @./MSGraphAPI.json")
        pass

    def add_role_assignment_to_storage_account(self, role, assignee):
        os.system(f"az role assignment create --role \"{role}\" --assignee {assignee} --scope {self.get_storage_account_id()}")
    
    def add_firewall_rule_for_synapse(self, synapse_workspace_name):
        os.system(f"az synapse workspace firewall-rule create --name allowAll --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255")

    def create_spark_pool(self, synapse_workspace_name, spark_pool_name, library_requirements):
        os.system(f"az synapse spark pool create --name {spark_pool_name} --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} "
                   "--spark-version 3.1 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 10 --enable-auto-scale true --delay 15 --enable-auto-pause true")
        #Now update spark pool to include required libraries (note that this has to be done as a separate step or the create command will fail, despite what the docs say)
        os.system(f"az synapse spark pool update --name {spark_pool_name} --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} --library-requirements {library_requirements} --no-wait")       

    def create_random_password():
        password = secrets.choice(string.ascii_uppercase) + secrets.choice(string.digits) + secrets.choice(['*', '%', '#', '@'])
        for _ in range(9): password += secrets.choice(string.ascii_lowercase)
        return password    