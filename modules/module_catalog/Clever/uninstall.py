import os
import sys

def uninstall(synapse_workspace_name, azure_client):
    azure_client.delete_notebook('EdFiResourceGenerator_py', synapse_workspace_name)

    azure_client.delete_dataflow("Process deletes", synapse_workspace_name)
    azure_client.delete_dataflow("Upsert_Descriptors", synapse_workspace_name)

    azure_client.delete_pipeline("Land All Entities to Stage1", synapse_workspace_name)
    azure_client.delete_pipeline("Trigger All Entities.json", synapse_workspace_name)
    azure_client.delete_pipeline("Master Pipeline.json", synapse_workspace_name)

if(__name__ == '__main__'):

    if(len(sys.argv) < 3):
        raise ValueError("Please pass the required script arguments to run the installation script.")

    delete_confirm = input('Are you sure you want to uninstall the Ed-Fi Module? (y/n):')
    if(delete_confirm not in ['y', 'Y']):
        exit()

    from AzureClient import AzureClient
    tenant_id = sys.argv[0]
    subscription_id = sys.argv[1]
    synapse_workspace_name = sys.argv[2]
    _azure_client = AzureClient(tenant_id, subscription_id)
    uninstall(_azure_client, synapse_workspace_name)