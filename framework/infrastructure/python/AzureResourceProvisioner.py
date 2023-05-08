# need to run "pip install -r requirements.txt"
import sys
import logging
import os
import re
from datetime import datetime
from AzureClient import AzureClient
from azure.core.exceptions import HttpResponseError
from msrest.exceptions import ValidationError

class AzureResourceProvisioner:
    def __init__(self, tenant_id, subscription_id, oea_suffix, location, oea_version, include_groups, logger):
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.oea_suffix = oea_suffix
        self.oea_version = oea_version
        self.location = location
        self.logger = logger
        self.include_groups = include_groups
        self.blobs = ['stage1', 'stage2', 'stage3', 'oea']
        self.keyvault = 'kv-oea-' + oea_suffix
        self.synapse_workspace_name = 'syn-oea-' + oea_suffix
        self.resource_group = 'rg-oea-' + oea_suffix
        self.storage_account = 'stoea' + oea_suffix
        self.app_insights = 'appi-oea-' + oea_suffix
        self.global_admins_name = 'Edu Analytics Global Admins'
        self.ds_group_name = 'Edu Analytics Data Scientists'
        self.eds_group_name = 'Edu Analytics External Data Scientists'
        self.de_group_name = 'Edu Analytics Data Engineers'
        self.user_object_id = os.popen("az ad signed-in-user show --query id -o tsv").read()[:-1] # the last char is a newline, so we strip that off
        self.tags = {'oea_version':oea_version}
        self.storage_account_id = f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.Storage/storageAccounts/{self.storage_account}"
        self.synapse_workspace_object = None
        self.storage_account_object = None
        self.external_data_scientists_id = None
        self.data_engineers_id = None
        self.data_scientists_id = None
        self.global_admins_id = None
        self.azure_client = AzureClient(self.tenant_id, self.subscription_id, self.location, self.tags, self.resource_group)

    def env_prep(self):
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

    def get_container_resourceId(self, container):
        return f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.Storage/storageAccounts/{self.storage_account}/blobServices/default/containers/{container}"

    def verify_permissions(self):
        # Check if user has "Owner" Permission on the subscription, fail if not.
        owner_role_def = self.azure_client.get_role('Owner', f"/subscriptions/{self.subscription_id}")
        owner_role_assignments = [role_assignment for role_assignment in self.azure_client.get_authorization_client().role_assignments.list(filter=f'principalId eq \'{self.user_object_id}\'') if role_assignment.role_definition_id == owner_role_def.id]
        if(len(owner_role_assignments) == 0):
            self.logger.error("--> Setup failed! The user does not have the \"Owner\" Permission on the Azure subscription")
            exit()

    def create_resource_group(self):
        try:
            self.azure_client.create_resource_group(self.resource_group)
            self.azure_client.resource_group_name = self.resource_group
        except ValidationError as e:
            self.logger.error('Validation Error - failed to create resource group: ' + str(e))
            exit()

    def create_storage_account(self):
        # Create the storage account and containers - https://docs.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create
        self.storage_account_object = self.azure_client.create_storage_account(self.storage_account)
        self.logger.info("\t--> Creating storage account containers.")
        self.azure_client.create_containers(self.storage_account, self.blobs)
        self.azure_client.setup_file_system(self.storage_account)

    def create_synapse_architecture(self):
        self.synapse_workspace_object = self.azure_client.create_synapse_workspace(self.synapse_workspace_name, self.storage_account)
        # This permission is necessary to allow a data pipeline in Synapse to invoke notebooks.
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.storage_account_object.id, self.synapse_workspace_object.identity.principal_id)

        self.logger.info("\t--> Creating firewall rule for accessing Synapse Workspace.")
        self.azure_client.add_firewall_rule_for_synapse('allowAll', '0.0.0.0', '255.255.255.255', self.synapse_workspace_name)

        self.logger.info("\t--> Creating spark pool.")
        self.azure_client.create_spark_pool(self.synapse_workspace_name, "spark3p3sm")
        library_requirements = f"{os.path.dirname(__file__)}/requirements.txt"
        # Creating pool with requirements is not working, so as a work around we create pool and update it.
        self.azure_client.update_spark_pool_with_requirements(self.synapse_workspace_name, "spark3p3sm", library_requirements)

    def create_keyvault_and_appinsights(self):
        access_policy_for_synapse = { 'tenant_id': self.tenant_id, 'object_id': self.synapse_workspace_object.identity.principal_id,
                                        'permissions': { 'secrets': ['get'] }
                                    }
        access_policy_for_user = { 'tenant_id': self.tenant_id, 'object_id': self.user_object_id,
                                    'permissions': { 'keys': ['all'], 'secrets': ['all'] }
                                }
        self.azure_client.create_key_vault(self.keyvault, [access_policy_for_synapse, access_policy_for_user])
        # self.azure_client.create_secret_in_keyvault(self.keyvault, 'oeaSalt')
        self.logger.info(f"--> Creating app-insights: {self.app_insights}")
        os.system(f"az monitor app-insights component create --app {self.app_insights} --resource-group {self.resource_group} --location {self.location} --tags {self.tags} -o none")

    def create_security_groups(self):
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

    def create_role_assignemnts(self):
        self.azure_client.create_role_assignment('Owner', f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/", self.global_admins_id)

        # Assign "Storage Blob Data Contributor" to security groups to allow users to query data via Synapse studio
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.global_admins_id)
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.data_scientists_id)
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.data_engineers_id)

        # Assign limited access to specific containers for the external data scientists
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('stage2'), self.external_data_scientists_id)
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('stage3'), self.external_data_scientists_id)
        self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.get_container_resourceId('oea'), self.external_data_scientists_id)
        self.azure_client.create_role_assignment('Reader', self.storage_account_id, self.data_engineers_id)

    def provision_resources(self):

        self.logger.info("--> Checking if the user has \"Owner\" Permission on the Azure Subscription.")
        self.verify_permissions()

        self.logger.info(f"--> 1) Creating resource group: {self.resource_group}")
        self.create_resource_group()

        self.logger.info(f"--> 2) Creating storage account: {self.storage_account}")
        self.create_storage_account()

        self.logger.info(f"--> 3) Creating Synapse Workspace: {self.synapse_workspace_name} (this is usually the longest step - it may take 5 to 10 minutes to complete)")
        self.create_synapse_architecture()

        self.logger.info(f"--> 4) Creating key vault: {self.keyvault}")
        self.create_keyvault_and_appinsights()

        if self.include_groups is True:
            self.logger.info("--> 5) Creating security groups in Azure Active Directory.")
            self.create_security_groups()

            self.logger.info("--> 6) Creating role assignments for Edu Analytics Global Admins, Edu Analytics Data Scientists, and Edu Analytics Data Engineers.")
            self.create_role_assignemnts()

        else:
            self.logger.info(f"--> 5 Creating \"Storage Blob Data Contributor\" role assignment for User to the storage account.")
            self.azure_client.create_role_assignment('Storage Blob Data Contributor', self.storage_account_id, self.user_object_id)





