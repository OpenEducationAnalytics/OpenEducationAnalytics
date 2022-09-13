import os
import sys
from zipfile import ZipFile

def install(synapse_workspace_name, azure_client, rg_name):
    azure_client.create_notebook_with_ipynb('Clever_module_ingestion', 'modules/module_catalog/Clever/notebook/Clever_module_ingestion.ipynb', synapse_workspace_name)
    azure_client.create_notebook_with_ipynb('Clever_py', 'modules/module_catalog/Clever/notebook/Clever_py.ipynb', synapse_workspace_name)

    with ZipFile('modules/module_catalog/Clever/pipeline/clever_pipeline_template.zip') as zp:
        zp.extractall('modules/module_catalog/Clever/pipeline/tmp')
    with ZipFile('modules/module_catalog/Clever/pipeline/Extracts/clever_data_ingestion.zip') as zp:
        zp.extractall('modules/module_catalog/Clever/pipeline/tmp')

    os.system(f"az deployment group create --name CleverInstallation --resource-group {rg_name} --template-file modules/module_catalog/Clever/pipeline/tmp/clever_main_pipeline/clever_main_pipeline.json --parameters workspaceName='{synapse_workspace_name}' LS_SQL_Serverless_OEA='LS_SQL_Serverless_OEA' LS_ADLS_OEA='LS_ADLS_OEA' LS_HTTP='LS_HTTP'")
    os.system(f"az deployment group create --name CleverDataIngestion --resource-group {rg_name} --template-file modules/module_catalog/Clever/pipeline/tmp/clever_data_pipeline/clever_data_pipeline.json --parameters workspaceName='{synapse_workspace_name}' LS_SQL_Serverless_OEA='LS_SQL_Serverless_OEA' LS_ADLS_OEA='LS_ADLS_OEA' LS_HTTP='LS_HTTP'")

if(__name__ == '__main__'):

    if(len(sys.argv) < 3):
        raise ValueError("Please pass the required script arguments to run the installation script.")

    sys.path.append('/framework/infrastructure/python/')

    from AzureClient import AzureClient
    tenant_id = sys.argv[0]
    subscription_id = sys.argv[1]
    synapse_workspace_name = sys.argv[2]
    _azure_client = AzureClient(tenant_id, subscription_id)
    install(_azure_client, synapse_workspace_name)