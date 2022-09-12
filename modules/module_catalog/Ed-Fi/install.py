import os
import sys

def install(synapse_workspace_name, azure_client):
    azure_client.create_notebook_with_ipynb('EdFiResourceGenerator_py', 'modules/module_catalog/Ed-Fi/notebook/EdFiResourceGenerator_py.ipynb', synapse_workspace_name)

    azure_client.create_or_update_dataflow(synapse_workspace_name, "modules/module_catalog/Ed-Fi/dataflow/Process deletes.json")
    azure_client.create_or_update_dataflow(synapse_workspace_name, "modules/module_catalog/Ed-Fi/dataflow/Upsert_Descriptors.json")

    azure_client.create_or_update_pipeline(synapse_workspace_name, "modules/module_catalog/Ed-Fi/pipeline/Land All Entities to Stage1.json", "Land All Entities to Stage1")
    azure_client.create_or_update_pipeline(synapse_workspace_name, "modules/module_catalog/Ed-Fi/pipeline/Trigger All Entities.json", "Trigger All Entities")
    azure_client.create_or_update_pipeline(synapse_workspace_name, "modules/module_catalog/Ed-Fi/pipeline/Master Pipeline.json", "Master Pipeline")

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