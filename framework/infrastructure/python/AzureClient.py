# need to run "pip install -r requirements.txt"
from asyncio.windows_utils import pipe
from dis import dis
import sys
import secrets
import string
import os, random
import json
import logging
from uuid import uuid4
from datetime import datetime
from azure.identity import AzureCliCredential, DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.v2018_09_01_preview import models as authorization_model
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.synapse import SynapseManagementClient
from azure.mgmt.synapse.models import Workspace, DataLakeStorageAccountDetails, ManagedIdentity, IpFirewallRuleInfo
from azure.mgmt.synapse.models import BigDataPoolResourceInfo, AutoScaleProperties, AutoPauseProperties, LibraryRequirements, NodeSizeFamily, NodeSize, BigDataPoolPatchInfo
from azure.synapse.artifacts import ArtifactsClient
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import HttpResponseError, ResourceExistsError

logger = logging.getLogger('AzureClient')

class AzureClient:
    """ todo: consider removing self.resource_group_name - it should probably be passed in as needed """
    def __init__(self, tenant_id, subscription_id, location = 'eastus', default_tags = None, resource_group_name = None):
        self.credential = AzureCliCredential()
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.location = location
        self.tags = default_tags if default_tags else {}
        self.resource_group_name = resource_group_name
        self.resource_group = None
        self.key_vault_client = None
        self.resource_client = None
        self.graph_rbac_client = None
        self.authorization_client = None
        self.storage_client = None
        self.artifacts_client = {}
        self.synapse_client = None

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

    def get_role(self, role_name, resource_id):
        auth_client = AuthorizationManagementClient(self.credential, self.subscription_id)
        # Get built-in role as a RoleDefinition object
        roles = list(auth_client.role_definitions.list(resource_id, filter="roleName eq '{}'".format(role_name)))
        return roles[0]

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

    """
    # This is not working as the GraphRbacManagementClient is expecting a credential with an
    # attribute "signed_session" while AzureCliCredential does not provide one.
    def create_aad_group(self, display_name, nick_name):
        poller = self.get_graph_rbac_client().groups.create(
            {
                'display_name':display_name,
                'mail_nickname':nick_name
            }
        )
        return poller
    """

    def create_or_update_dataflow(self, synapse_workspace, dataflow_file_path):
        with open(dataflow_file_path) as f: dataflow_dict = json.load(f)
        poller = self.get_artifacts_client(synapse_workspace).data_flow.begin_create_or_update_dataflow(dataflow_dict['name'], dataflow_dict)
        return poller

    def create_or_update_pipeline(self, synapse_workspace, pipeline_file_path, pipeline_name):
        with open(pipeline_file_path) as f: pipeline_dict = json.load(f)
        poller = self.get_artifacts_client(synapse_workspace).pipeline.begin_create_or_update_pipeline(pipeline_name, pipeline_dict)
        return poller

    def create_notebook_with_ipynb(self, notebook_name, file_path, synapse_workspace_name):
        os.system(f"az synapse notebook create --workspace-name {synapse_workspace_name} --name {notebook_name} --file @{file_path} -o none")

    def create_notebook(self, notebook_filename, synapse_workspace_name):
        """ Creates synapse notebook from json (using the json from git when Synapse studio is connected to a repo) """
        artifacts_client = self.get_artifacts_client(synapse_workspace_name)
        with open(notebook_filename) as f: notebook_dict = json.load(f)
        self.validate_notebook_json(notebook_dict)
        logger.info(f"Creating notebook: {notebook_dict['name']}")
        poller = artifacts_client.notebook.begin_create_or_update_notebook(notebook_dict['name'], notebook_dict)
        return poller #AzureOperationPoller

    def validate_notebook_json(self, nb_json):
        """ These attributes must exist for the call to begin_create_or_update_notebook to pass validation """
        if not 'nbformat' in nb_json['properties']: nb_json['properties']['nbformat'] = 4
        if not 'nbformat_minor' in nb_json['properties']: nb_json['properties']['nbformat_minor'] = 2
        for cell in nb_json['properties']['cells']:
            if not 'metadata' in cell: cell['metadata'] = {}
        if 'bigDataPool' in nb_json['properties']:
            nb_json['properties'].pop('bigDataPool', None) #Remove bigDataPool if it's there

    def delete_notebook(self, notebook_name, synapse_workspace_name):
        """ Deletes the synapse notebook from the workspace."""
        poller = self.get_artifacts_client(synapse_workspace_name).notebook.delete_notebook(notebook_name)
        return poller

    def delete_pipeline(self, pipeline_name, synapse_workspace_name):
        """ Deletes the Synapse pipeline from the workspace."""
        poller = self.get_artifacts_client(synapse_workspace_name).pipeline.delete_pipeline(pipeline_name)
        return poller

    def delete_dataflow(self, dataflow_name, synapse_workspace_name):
        """ Deletes the Synapse pipeline from the workspace."""
        poller = self.get_artifacts_client(synapse_workspace_name).data_flow.delete_dataflow(dataflow_name)
        return poller

    def delete_linked_service(self, linked_service_name, synapse_workspace_name):
        """ Deletes the Synapse Linked Service from the workspace."""
        poller = self.get_artifacts_client(synapse_workspace_name).linked_service.delete_linked_service(linked_service_name)
        return poller

    def delete_dataset(self, dataset_name, synapse_workspace_name):
        """ Deletes the Synapse Dataset from the workspace."""
        poller = self.get_artifacts_client(synapse_workspace_name).dataset.delete_dataset(dataset_name)
        return poller

    def delete_resource_group(self, name):
        self.get_resource_client().resource_groups.begin_delete(name)
        self.resource_group_name = None
        self.resource_group = None

    def create_resource_group(self, resource_group_name, tags=None):
        if not tags: tags = {}
        result = self.get_resource_client().resource_groups.create_or_update(resource_group_name, {'location': self.location, 'tags': tags})
        self.resource_group = result
        self.resource_group_name = result.name

    def list_resources_in_resource_group(self, resource_group_name):
        """ Retuns a csv string listing all of the resources in the given resource group. """
        resource_list = self.get_resource_client().resources.list_by_resource_group(resource_group_name, expand = 'createdTime,changedTime')
        resources = "name,resource_type,created_time,changed_time\n"
        for resource in list(resource_list):
            resources += f"{resource.name},{resource.type},{str(resource.created_time)}{str(resource.changed_time)}\n"
        return resources

    def create_synapse_workspace(self, synapse_workspace_name, storage_account_name):
        """ https://docs.microsoft.com/en-us/python/api/azure-mgmt-synapse/azure.mgmt.synapse.aio.operations.workspacesoperations?view=azure-python#begin-create-or-update-resource-group-name--str--workspace-name--str--workspace-info--azure-mgmt-synapse-models--models-py3-workspace----kwargs-----azure-core-polling--async-poller-asynclropoller--forwardref---models-workspace--- """
        default_data_lake_storage = DataLakeStorageAccountDetails(account_url=f"https://{storage_account_name}.dfs.core.windows.net", filesystem="synapse-workspace")

        poller = self.get_synapse_client().workspaces.begin_create_or_update(self.resource_group_name, synapse_workspace_name,
            {
                "location" : self.location,
                "tags" : self.tags,
                "identity" : ManagedIdentity(type="SystemAssigned"),
                "default_data_lake_storage" : default_data_lake_storage,
                "sql_administrator_login" : "oea-admin",
                "sql_administrator_login_password" : AzureClient.create_random_password(),
            }
        )
        # Call poller.result() to wait for completion
        # returns a synapse Workspace object
        return poller.result()

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

    def create_linked_service(self, workspace_name, linked_service_name, file_path):
        os.system(f"az synapse linked-service create --workspace-name {workspace_name} --name {linked_service_name} --file @{file_path} -o none")

    def create_dataset(self, workspace_name, dataset_name, file_path):
        os.system(f"az synapse dataset create --workspace-name {workspace_name} --name {dataset_name} --file @{file_path} -o none")


    def add_role_assignment_to_resource(self, role_name, resource_id, principal_id):
        role = self.get_role(role_name, resource_id)
        self.get_authorization_client().role_assignments.create(resource_id, uuid4(),
            authorization_model.RoleAssignmentCreateParameters(role_definition_id=role.id, principal_id=principal_id)
        )
        return

    def create_role_assignment(self, role_name, resource_id, principal_id):
        # https://docs.microsoft.com/en-us/python/api/azure-mgmt-authorization/azure.mgmt.authorization.v2020_10_01_preview.operations.roleassignmentsoperations?view=azure-python#create-scope--role-assignment-name--parameters----kwargs-
        role = self.get_role(role_name, resource_id)
        try:
            self.get_authorization_client().role_assignments.create(resource_id, uuid4(),
                authorization_model.RoleAssignmentCreateParameters(
                    role_definition_id=role.id,
                    principal_id=principal_id)
            )
        except ResourceExistsError as e:
            logger.info(f"The {role_name} role assignment already exists for {principal_id} on resource {resource_id}.")
            #print(f"The {role_name} role assignment already exists for {principal_id} on resource {resource_id}.")

    def add_firewall_rule_for_synapse(self, rule_name, start_ip_address, end_ip_address, synapse_workspace_name):
        """ https://docs.microsoft.com/en-us/python/api/azure-mgmt-synapse/azure.mgmt.synapse.aio.operations.ipfirewallrulesoperations?view=azure-python """
        #os.system(f"az synapse workspace firewall-rule create --name allowAll --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255")
        ip_firewall_rule_info = IpFirewallRuleInfo(name=rule_name, start_ip_address=start_ip_address, end_ip_address=end_ip_address)
        #poller = self.get_synapse_client().ip_firewall_rules.begin_create_or_update(self.resource_group_name, synapse_workspace_name, rule_name, ip_firewall_rule_info)
        poller = self.get_synapse_client().ip_firewall_rules.begin_create_or_update(self.resource_group_name, synapse_workspace_name, rule_name,
            {
                "name" : rule_name,
                "start_ip_address" : start_ip_address,
                "end_ip_address" : end_ip_address
            }
        )
        return poller

    def create_spark_pool(self, synapse_workspace_name, spark_pool_name):
        """ https://docs.microsoft.com/en-us/python/api/azure-mgmt-synapse/azure.mgmt.synapse.aio.operations.bigdatapoolsoperations?view=azure-python """
        #os.system(f"az synapse spark pool create --name {spark_pool_name} --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} "
        #           "--spark-version 3.1 --node-count 3 --node-size Small --min-node-count 3 --max-node-count 10 --enable-auto-scale true --delay 15 --enable-auto-pause true")
        #Now update spark pool to include required libraries (note that this has to be done as a separate step or the create command will fail, despite what the docs say)
        #os.system(f"az synapse spark pool update --name {spark_pool_name} --workspace-name {synapse_workspace_name} --resource-group {self.resource_group_name} --library-requirements {library_requirements} --no-wait")
        poller = self.get_synapse_client().big_data_pools.begin_create_or_update(self.resource_group_name, synapse_workspace_name, spark_pool_name,
            BigDataPoolResourceInfo(
                tags = self.tags,
                location = self.location,
                auto_scale = AutoScaleProperties(enabled=True, min_node_count=3, max_node_count=10),
                auto_pause = AutoPauseProperties(delay_in_minutes=15, enabled=True),
                spark_version = '3.1',
                node_size = NodeSize.SMALL,
                node_size_family = NodeSizeFamily.MEMORY_OPTIMIZED,
            )
        )

        # todo: now install the requirements file, this can only be done after the pool has been created
        #echo "--> Update spark pool to include required libraries (note that this has to be done as a separate step or the create command will fail, despite what the docs say)."
        #az synapse spark pool update --name spark3p1sm --workspace-name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP --library-requirements $oea_path/framework/requirements.txt --no-wait
        #[[ $? != 0 ]] && { echo "Provisioning of azure resource failed. See $logfile for more details." 1>&3; exit 1; }
        result = poller.result() # wait for completion of spark pool


        return

    def update_spark_pool_with_requirements(self, synapse_workspace_name, spark_pool_name, library_requirements_path_and_filename):
        with open(library_requirements_path_and_filename, 'r') as f: lib_contents = f.read()
        poller = self.get_synapse_client().big_data_pools.update(self.resource_group_name, synapse_workspace_name, spark_pool_name,
            BigDataPoolPatchInfo (
                library_requirements = LibraryRequirements(filename=os.path.basename(library_requirements_path_and_filename), content=lib_contents)
            )
        )

    def create_random_password():
        password = secrets.choice(string.ascii_uppercase) + secrets.choice(string.digits) + secrets.choice(['*', '%', '#', '@'])
        for _ in range(9): password += secrets.choice(string.ascii_lowercase)
        return password