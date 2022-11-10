import os
import sys
import os
from AzureClient import AzureClient
from AzureResourceProvisioner import AzureResourceProvisioner
from OEAFrameworkInstaller import OEAFrameworkInstaller
import logging
from datetime import datetime


# Info on logging in Azure python sdk: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='setup_oea_log_{:%Y_%m_%d__%H_%M}.log'.format(datetime.now()), level=logging.DEBUG)
_logger = logging.getLogger('setup')
_logger.addHandler(logging.StreamHandler(sys.stdout))

_tenant_id = os.popen('az account show --query homeTenantId -o tsv').read().replace('\n', '')
_subscription_id = os.popen('az account show --query id -o tsv').read().replace('\n', '')
_oea_version = "0.7"

if(len(sys.argv) < 2):
    raise Exception("Setup script expects at least 1 Argument.")
_oea_suffix = sys.argv[1]
_location = "eastus" if len(sys.argv) < 3 else sys.argv[2]
_include_groups = True if (len(sys.argv) > 3 and sys.argv[3] in ['true', 'True']) else False

# Instantiate AzureClient class to connect with Azure CLI using Python SDK
azure_client = AzureClient(_tenant_id, _subscription_id, _location)

# Instantiate AzureResourceProvisioner class to setup the required infrastructure in your Azure Tenant.
_logger.info('Setting up infrastructure in Azure Tenant.')
resource_provisioner = AzureResourceProvisioner(_tenant_id, _subscription_id, _oea_suffix, _location, _oea_version, _include_groups, _logger)
resource_provisioner.provision_resources()
_logger.info('Completed setting up infrastructure.')

# Instantiate OEAFrameworkInstaller class to install the Base OEA framework in your Synapse workspace.
_logger.info('Installing Base OEA Framework in Synapse workspace.')
oea_installer = OEAFrameworkInstaller(azure_client, resource_provisioner.storage_account, resource_provisioner.keyvault, resource_provisioner.synapse_workspace_name, 'framework/synapse', _logger)
oea_installer.install()
_logger.info('Successfully Installed Base OEA Framework.')
