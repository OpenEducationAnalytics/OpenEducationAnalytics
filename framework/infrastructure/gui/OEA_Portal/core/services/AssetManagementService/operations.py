from OEA_Portal.settings import OEA_ASSET_TYPES, BASE_DIR
from ..SynapseManagementService import SynapseManagementService
from ..utils import *
from OEA_Portal.auth.AzureClient import AzureClient
from OEA_Portal.core.models import OEAInstalledAsset, OEAInstance
from azure.mgmt.resource.resources.models import Deployment, DeploymentProperties
import urllib.request
import time
import os
import re
import json


def get_oea_assets(asset_type:str):
    """
    Returns a list of names of all available OEA assets of a given type.
    """
    if(asset_type not in OEA_ASSET_TYPES):
        raise Exception(f"{asset_type} is not an OEA supported Asset type.")
    url = f"https://api.github.com/repos/microsoft/OpenEduAnalytics/contents/{asset_type}s/{asset_type}_catalog?ref=main"
    request = urllib.request.Request(url)
    response = json.loads(urllib.request.urlopen(request))
    return [asset["name"] for asset in response]

def get_installed_assets_in_workspace(workspace_name, azure_client:AzureClient):
    """
    Returns the list of Installed modules, packages and assets in the given workspace.
    """
    workspace_object = next(ws for ws in azure_client.get_synapse_client().workspaces.list() if ws.name == workspace_name)
    storage_account = get_storage_account_from_url(workspace_object.default_data_lake_storage.account_url)
    data = get_blob_contents(azure_client, storage_account, f'oea/admin/workspaces/{workspace_name}/status.json')
    modules = [OEAInstalledAsset(asset['Name'], asset['Version'], asset['LastUpdatedTime']) for asset in data['module']]
    packages = [OEAInstalledAsset(asset['Name'], asset['Version'], asset['LastUpdatedTime']) for asset in data['package']]
    schemas = [OEAInstalledAsset(asset['Name'], asset['Version'], asset['LastUpdatedTime']) for asset in data['schema']]
    return modules, packages, schemas, data['OEA_Version']

def dfs(table_name, visited, dependency_dict, dependency_order):
    """
    Does a Depth First Search on the dependency matrix.
    """
    visited[table_name] = True
    if dependency_dict[table_name] == []:
        dependency_order.append(table_name)
        return
    for dependent_table in dependency_dict[table_name]:
        if(visited[dependent_table] is False):
            dfs(dependent_table, visited, dependency_dict, dependency_order)
        if(visited[dependent_table] is False):
            dependency_order.append(dependent_table)
    dependency_order.append(table_name)

def create_pipeline_dependency_order(dependency_dict):
    """
    Returns a topological sorted list of pipelines where for any pipeline at index n is not
    dependent of the pipelines from index greater than n.
    """
    visited = {}
    dependency_order = []
    pipelines = list(dependency_dict.keys())
    for pipeline in pipelines:
        pipeline_name = pipeline.split('.')[0] if '.' in pipeline else pipeline
        visited[pipeline_name] = False
    for pipeline in pipelines:
        pipeline_name = pipeline.split('.')[0] if '.' in pipeline else pipeline
        if(visited[pipeline_name] is False):
            dfs(pipeline_name, visited, dependency_dict, dependency_order)
    return dependency_order

def create_dependency_matrix_by_reading_all_files(pipeline_root_path):
    """
    Reads through all the pipeline files and returns a dependency matrix.
    It returns a where a pipeline name is a key and a list containing all the dependent pipelines as value
    """
    files = os.listdir(pipeline_root_path)
    dependency_dict = {}
    for file in files:
        if '.json' in file:
            key = file.split('.')[0]
            dependency_dict[key] = []
            with open(f"{pipeline_root_path}/{file}") as f:
                file_json = json.load(f)
            for x in get_values_from_json(file_json, 'pipeline'):
                if x['referenceName']+'.json' in files:
                    dependency_dict[key].append(x['referenceName'])
    return dependency_dict

#todo; upload_blob_contents is not working.
def log_installed_asset(azure_client, workspace_name, storage_account, asset_type, asset_name, version):
    """
    Log the installed asset in the Workspace DB.
    """
    data = get_blob_contents(azure_client, storage_account, f'oea/admin/workspaces/{workspace_name}/status.json')
    data[asset_type].append({
        "Name": asset_name,
        "Version": version,
        "LastUpdatedTime": time.asctime()
    })
    upload_blob_contents(azure_client, storage_account, f'oea/admin/workspaces/{workspace_name}/status.json', json.dumps(data))

def create_dependency_matrix_by_reading_template(template_file=None, template_json=None):
    """
    Reads a pipelines template JSON file and creates a dependency matrix over all the pipelines.
    """
    if template_file is None and template_json is None:
        raise Exception("You must pass 'template_file' or 'template_json' parameters.")
    if template_json is None:
        with open(template_file) as f: template_json = json.loads(f.read())
    dependency_dict = {}
    for resource in template_json["resources"]:
        if resource["type"] == "Microsoft.Synapse/workspaces/pipelines":
            resource["name"] = re.sub('[^a-zA-Z0-9_]', '', resource["name"].split(",")[-1])
            dependency_dict[resource["name"]] = []
            for x in get_values_from_json(resource, 'pipeline'):
                dependency_dict[resource["name"]].append(x['referenceName'])
    return dependency_dict


def get_values_from_json(file_json, target_field):
    for k,v in file_json.items():
        if k == target_field:
            yield v
        elif isinstance(v, dict):
            for item in get_values_from_json(v, target_field):
                yield item
        elif isinstance(v, list):
            for x in v:
                if isinstance(x, dict):
                    for item in get_values_from_json(x, target_field):
                        yield item


def parse_deployment_template_and_install_artifacts(file_path:str, azure_client:AzureClient):
    with open(file_path) as f:
        template_str = f.read()
        template_json = json.loads(template_str)

    parameters = template_json["parameters"]
    sms = SynapseManagementService(azure_client, 'rg-oea-abhinav4')
    for param in list(parameters.keys())[1:]:
        template_str = template_str.replace(f"[parameters('{param}')]", param)
    # todo: Figure out how to get target OEA instance.
    target_oea_instance = OEAInstance('syn-oea-abhinav4', 'rg-oea-abhinav4', 'kv-oea-abhinav4', 'stoeaabhinav4')
    template_json = json.loads(template_str)

    pipeline_config_json = {}
    pollers_pass1 = []
    pollers_pass2 = []
    for resource in template_json["resources"]:
        resource["name"] = re.sub('[^a-zA-Z0-9_]', '', resource["name"].split(",")[-1])
        if resource["type"] == "Microsoft.Synapse/workspaces/pipelines":
            pipeline_config_json[resource["name"]] = resource
        if resource["type"] == "Microsoft.Synapse/workspaces/datasets":
            pollers_pass1.append(sms.create_or_update_dataset(target_oea_instance, dataset_dict=resource, wait_till_completion=False))
        elif resource["type"] == "Microsoft.Synapse/workspaces/notebooks":
            pollers_pass1.append(sms.create_or_update_notebook(target_oea_instance, notebook_dict=resource, wait_till_completion=False))

    while(not(any(poller.status() == 'InProgress' for poller in pollers_pass1))):
        time.sleep(2)

    for resource in template_json["resources"]:
        if resource["type"] == "Microsoft.Synapse/workspaces/dataflows":
            pollers_pass2.append(sms.create_or_update_dataflow(target_oea_instance, dataflow_dict=resource, wait_till_completion=False))

    while(not(any(poller.status() == 'InProgress' for poller in pollers_pass2))):
        time.sleep(2)

    dependency_dict = create_dependency_matrix_by_reading_template(template_json=template_json)
    pipeline_dependency_order = create_pipeline_dependency_order(dependency_dict)

    for pipeline in pipeline_dependency_order:
        sms.create_or_update_pipeline(target_oea_instance, pipeline_dict=pipeline_config_json[pipeline], wait_till_completion=True)

