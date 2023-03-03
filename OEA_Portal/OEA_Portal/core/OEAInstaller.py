import os
from base64 import b64encode
from OEA_Portal.settings import BASE_DIR
import uuid
import zipfile
import urllib.request
import secrets
from OEA_Portal.core.models import OEAInstance
from OEA_Portal.auth.AzureClient import AzureClient
from OEA_Portal.core.services.AzureResourceProvisionService import AzureResourceProvisionService
from OEA_Portal.core.services.SynapseManagementService import SynapseManagementService
import logging
class OEAInstaller():
    """
    OEA Installer class which handles all tasks related to installing and uninstalling an OEA instance.
    """
    def __init__(self, tenant_id, subscription_id, oea_suffix, oea_version='0.7', location='eastus', tags=None, include_groups=False):
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.location = location
        self.tags = {'OEA_Version':oea_version}
        self.include_groups = include_groups
        self.framework_path_relative = f"{BASE_DIR}/downloads/OEA_v{oea_version}/framework/synapse".replace('\\', '/')
        self.framework_zip_url = "https://github.com/microsoft/OpenEduAnalytics/releases/download/v0.7/OEA_v0.7.zip"
        #todo: Find way to get signed-in user id using python sdk.
        self.user_object_id = '34b26f30-cbfc-47ec-9131-27fef4433705'
        self.resource_group_name = f"rg-oea-{oea_suffix}"
        self.storage_account_name = f"stoea{oea_suffix}"
        self.keyvault_name = f"kv-oea-{oea_suffix}"
        self.appinsights_name = f"appi-oea-{oea_suffix}"
        self.synapse_workspace_name = f"syn-oea-{oea_suffix}"
        self.containers = ['oea', 'stage1', 'stage2', 'stage3']
        self.dirs = ['stage1/Transactional','stage2/Ingested','stage2/Refined','oea/sandboxes/sandbox1/stage1/Transactional',\
            'oea/sandboxes/sandbox1/stage2/Ingested','oea/sandboxes/sandbox1/stage2/Refined','oea/sandboxes/sandbox1/stage3',\
                'oea/dev/stage1/Transactional','oea/dev/stage2/Ingested','oea/dev/stage2/Refined','oea/dev/stage3']
        self.storage_account_id = f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.Storage/storageAccounts/{self.storage_account_name}"
        self.global_admins_name = None
        self.ds_group_name = None
        self.eds_group_name = None
        self.de_group_name = None
        self.logger = logging.getLogger('OEAInstaller')

    def verify_permissions(self, azure_client, resouce_provision_service):
        """ Check if user has "Owner" Permission on the subscription, fail if not """
        owner_role_def = resouce_provision_service.get_role('Owner', f"/subscriptions/{self.subscription_id}")
        owner_role_assignments = [role_assignment for role_assignment in azure_client.get_authorization_client().role_assignments.list(filter=f'principalId eq \'{self.user_object_id}\'') if role_assignment.role_definition_id == owner_role_def.id]
        if(len(owner_role_assignments) == 0):
            self.logger.error("--> Setup failed! The user does not have the \"Owner\" Permission on the Azure subscription")
            raise PermissionError("User does not enough permissions.")

    def get_container_resourceId(self, container):
        """ Returns the Resource Id of the given container """
        return f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.Storage/storageAccounts/{self.storage_account_name}/blobServices/default/containers/{container}"

    def create_synapse_architecture(self, azure_resource_provision_service:AzureResourceProvisionService, synapse_management_service:SynapseManagementService):
        """
        Creates the Synapse infrastructure required for an OEA installation.
        This includes;
            1. Creating Synapse workspace.
            2. Creating 'Storage Blob Data Contributor' Role assignment to the user.
            3. Adding firewall rule.
            3. Create 2 spark pools - spark3p2sm and spark3p2med
        """
        self.synapse_workspace_object = azure_resource_provision_service.create_synapse_workspace(self.synapse_workspace_name, self.resource_group_name, self.storage_account_name)
        azure_resource_provision_service.create_role_assignment('Storage Blob Data Contributor', self.storage_account_object.id, self.synapse_workspace_object.identity.principal_id)
        synapse_management_service.add_firewall_rule_for_synapse('allowAll', '0.0.0.0', '255.255.255.255', self.synapse_workspace_name)
        synapse_management_service.create_spark_pool(self.synapse_workspace_name, "spark3p2sm",
                {
                    "node_size": "small",
                    "max_node_count": 5
                }
            )
        synapse_management_service.create_spark_pool(self.synapse_workspace_name, "spark3p2med",
                {
                    "node_size": "medium",
                    "max_node_count": 10
                }
            )

    def create_aad_groups(self):
        """
        Create the AAD groups required for the OEA installation.
        """
        #todo: Migrate this step to use Python SDK.
        os.system(f"az ad group create --display-name \"{self.global_admins_name}\" --mail-nickname 'EduAnalyticsGlobalAdmins'")
        os.system(f"az ad group owner add --group \"{self.global_admins_name}\" --owner-object-id {self.user_object_id}")
        self.global_admins_id = os.popen(f"az ad group show --group \"{self.global_admins_name}\" --query id --output tsv").read()[:-1]
        os.system(f"az ad group create --display-name \"{self.ds_group_name}\" --mail-nickname 'EduAnalyticsDataScientists'")
        os.system(f"az ad group owner add --group \"{self.ds_group_name}\" --owner-object-id {self.user_object_id}")
        self.data_scientists_id = os.popen(f"az ad group show --group \"{self.ds_group_name}\" --query id --output tsv").read()[:-1]
        os.system(f"az ad group create --display-name \"{self.de_group_name}\" --mail-nickname 'EduAnalyticsDataEngineers' -o none")
        os.system(f"az ad group owner add --group \"{self.de_group_name}\" --owner-object-id {self.user_object_id} -o none")
        self.data_engineers_id = os.popen(f"az ad group show --group \"{self.de_group_name}\" --query id --output tsv").read()[:-1]
        os.system(f"az ad group create --display-name \"{self.eds_group_name}\" --mail-nickname 'EduAnalyticsExternalDataScientists' -o none")
        os.system(f"az ad group owner add --group \"{self.eds_group_name}\" --owner-object-id {self.user_object_id} -o none")
        self.external_data_scientists_id = os.popen(f"az ad group show --group \"{self.eds_group_name}\" --query id --output tsv").read()[:-1]

    def create_role_assignments_to_groups(self, provision_resource_service):
        """
        Create the role assignments to the different groups.
        """
        provision_resource_service.create_role_assignment('Owner', f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/", self.global_admins_id)
        # Assign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.global_admins_id)
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.data_scientists_id)
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.data_engineers_id)
        # Assign limited access to specific containers for the external data scientists
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('stage2'), self.external_data_scientists_id)
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('stage3'), self.external_data_scientists_id)
        provision_resource_service.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('oea'), self.external_data_scientists_id)
        provision_resource_service.create_role_assignment('Reader', self.storage_account_id, self.data_engineers_id)

    def download_and_extract_framework(self):
        """
        Download and extract the OEA framework ZIP file into file system.
        """
        zip_path, _ = urllib.request.urlretrieve(self.framework_zip_url)
        with zipfile.ZipFile(zip_path, "r") as f:
            f.extractall(f"{BASE_DIR}/downloads")

    def install(self):
        """
        Installs the OEA framework and all the required assets in the Azure Subscription.
        As part of the Installation, the following steps are done:

        1. Verify if the user has "owner" permissions on the Azure Subscription.
        2. Create a resource group.
        3. Create a storage account along with the required containers and directories.
        4. Set up the Azure Synapse Analytics Architecture.
        5. Create a keyvault and secret.
        6. Create AAD groups and role assignments, if required.
        7. Install the OEA framework artifacts in the Synapse workspace.
        """
        self.download_and_extract_framework()
        azure_client = AzureClient(self.tenant_id, self.subscription_id, location=self.location, default_tags=self.tags)
        azure_resource_provision_service = AzureResourceProvisionService(azure_client)
        synapse_management_service = SynapseManagementService(azure_client, self.resource_group_name)
        oea_instance = OEAInstance(self.synapse_workspace_name, self.resource_group_name, self.keyvault_name, self.storage_account_name)
        self.verify_permissions(azure_client, azure_resource_provision_service)

        azure_resource_provision_service.create_resource_group(self.resource_group_name)

        self.storage_account_object = azure_resource_provision_service.create_storage_account(self.storage_account_name, self.resource_group_name)
        azure_resource_provision_service.create_containers_and_directories(self.storage_account_name, self.resource_group_name, self.containers, self.dirs)

        self.create_synapse_architecture(azure_resource_provision_service, synapse_management_service)
        access_policy_for_synapse = { 'tenant_id': self.tenant_id, 'object_id': self.synapse_workspace_object.identity.principal_id,
                                            'permissions': { 'secrets': ['get'] }
                                        }
        access_policy_for_user = { 'tenant_id': self.tenant_id, 'object_id': self.user_object_id,
                                    'permissions': { 'keys': ['all'], 'secrets': ['all'] }
                                }

        azure_resource_provision_service.create_key_vault(self.keyvault_name, self.resource_group_name, [access_policy_for_synapse, access_policy_for_user])
        azure_resource_provision_service.create_secret_in_keyvault(self.keyvault_name, 'oeaSalt', b64encode(secrets.token_bytes(16)).decode())
        #todo: Migrate this step to use Python SDK.
        # os.system(f"az monitor app-insights component create --app {self.appinsights_name} --resource-group {self.resource_group_name} --location {self.location} --tags {self.tags} -o none")
        if self.include_groups is True:
            self.create_aad_groups()
            self.create_role_assignments_to_groups()
        else:
            azure_resource_provision_service.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.user_object_id)

        synapse_management_service.install_all_linked_services(oea_instance, f'{self.framework_path_relative}/linkedService')

        synapse_management_service.install_all_datasets(oea_instance, f'{self.framework_path_relative}/dataset')

        synapse_management_service.install_all_notebooks(oea_instance, f'{self.framework_path_relative}/notebook', wait_till_completion=False)

        synapse_management_service.install_all_dataflows(oea_instance, f'{self.framework_path_relative}/dataflow', wait_till_completion=False)

        synapse_management_service.install_all_pipelines(oea_instance, f'{self.framework_path_relative}/pipeline')
