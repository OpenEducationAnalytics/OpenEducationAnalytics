# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import argparse
import json
import logging
import os

from azure.synapse.artifacts import ArtifactsClient
from azure.identity import DefaultAzureCredential
#from azure.core.exceptions import HttpResponseError

# 1. Get synapse suffix and destination directory
# 2. Ensure read/write access to each file and folder in directory/subdirectories.
# 3. Azure login
# 4. Get synapse data one by one, and copy into root folder.

# Constants
ROOT_FOLDERS = ['framework', 'modules', 'packages', 'schemas']

OEA_SYNAPSE_WORKSPACE_PREFIX = 'syn-oea'
OEA_SYNAPSE_DEV_WORKSPACE_FORMAT_STRING = 'https://syn-oea-{}.dev.azuresynapse.net'
OEA_FRAMEWORK_DATASET_PATH_FROM_ROOT = 'framework\\synapse\\dataset'
OEA_FRAMEWORK_PIPELINE_PATH_FROM_ROOT = 'framework\\synapse\\pipeline'

OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME = 'OEA_Framework' # TODO: This folder might not be necessary / or needs to exist for every artifact.
OEA_SYNAPSE_FRAMEWORK_CONTOSO_FOLDER_NAME = 'contoso_v0p2' # TODO: standardize all folder names to be same casing and pattern.

ARTIFACT_NAME_KEY = "name"
ARTIFACT_TYPE_KEY = "type"
ARTIFACT_PROPERTIES_KEY = "properties"

# Instances
_logger = logging.getLogger(__name__)

def _ensure_oea_root_directory(path):
    if not os.path.isdir(path):
        _logger.error('This is not a folder path: \'{}\'.'.format(path))
        exit(1)

    # ensure provided path is the root of the OEA repository.
    subfolder_tuples = [ (f.path, f.name) for f in os.scandir(path) if f.is_dir()]
    subfolder_names = [t[1] for t in subfolder_tuples]
    subfolder_paths = [t[0] for t in subfolder_tuples]

    if (not all(root_folder in subfolder_names for root_folder in ROOT_FOLDERS)):
        _logger.error('This is not the root OEA folder: \'{}\'. Please provide the path to the root of the OEA repository.'.format(path))
        exit(1)

    _ensure_read_write_access(subfolder_paths)

def _ensure_read_write_access(folders):
    # perform shallow check of write access to directory.
    for folder in folders:
        if not os.access(folder, os.X_OK | os.W_OK):
            _logger.error('We do not have write access to the following folder: \'{}\'.'.format(folder))
            exit(1)

def _copy_synapse_artifacts(suffix, path):
    token_credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    endpoint = OEA_SYNAPSE_DEV_WORKSPACE_FORMAT_STRING.format(suffix)
    client = ArtifactsClient(credential=token_credential, endpoint=endpoint)

    #_copy_synapse_datasets(client, path) # get datasets
    _copy_synapse_pipelines(client, path) # get pipelines

    # get notebooks
    # linked services
    # sql scripts

def _copy_synapse_datasets(client: ArtifactsClient, path):
    dataset_iterator = client.dataset.get_datasets_by_workspace()
    datasets = []
    for item in dataset_iterator:
        artifact = {
            ARTIFACT_NAME_KEY: item.name,
            ARTIFACT_PROPERTIES_KEY: item.serialize()[ARTIFACT_PROPERTIES_KEY],
            ARTIFACT_TYPE_KEY: item.type,
        }
        datasets.append(artifact)

    # separate the datasets by folders.
    # if the dataset is put into the root synapse folder, then the folder key will be missing.
    dataset_folders = _get_folder_partitioned_artifacts(datasets)

    # Write out the files to the relevant folders.
    for key, ds_list in dataset_folders.items():
        for dataset in ds_list:

            # TODO: THIS ONLY HANDLES FRAMEWORK PIPELINES, HANDLE MODULE PIPELINES AS WELL.
            
            if key == OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME:
                file_path = '{}\\{}\\{}.json'.format(path[:-1], OEA_FRAMEWORK_DATASET_PATH_FROM_ROOT, dataset['name'])
                
                with open(file_path, "w") as dataset_file:
                    json_data_pp = json.dumps(dataset, sort_keys=True, indent=4)
                    dataset_file.write(json_data_pp)

def _copy_synapse_pipelines(client: ArtifactsClient, path):
    pipeline_iterator = client.pipeline.get_pipelines_by_workspace()
    pipelines = []
    for item in pipeline_iterator:
        artifact = {
            ARTIFACT_NAME_KEY: item.name,
            ARTIFACT_PROPERTIES_KEY: item.serialize()[ARTIFACT_PROPERTIES_KEY],
            ARTIFACT_TYPE_KEY: item.type,
        }
        pipelines.append(artifact)

    # separate pipelines by folders
    # if the pipelinee is put into the root synapse folder
    pipeline_folders = _get_folder_partitioned_artifacts(pipelines)
    
    # Write out the files to the relevant folders.
    for key, ds_list in pipeline_folders.items():
        for dataset in ds_list:

            # TODO: THIS ONLY HANDLES FRAMEWORK PIPELINES, HANDLE MODULE PIPELINES AS WELL.

            if key == OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME or key == OEA_SYNAPSE_FRAMEWORK_CONTOSO_FOLDER_NAME:
                file_path = '{}\\{}\\{}.json'.format(path[:-1], OEA_FRAMEWORK_PIPELINE_PATH_FROM_ROOT, dataset['name'])
                with open(file_path, "w") as dataset_file:
                    json_data_pp = json.dumps(dataset, sort_keys=True, indent=4)
                    dataset_file.write(json_data_pp)

def _get_folder_partitioned_artifacts(artifact_list):
    artifact_folder_dictionary = {}

    for artifact in artifact_list:
        if 'folder' not in artifact['properties']:
            # this dataset belongs in the framework
            if OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME not in artifact_folder_dictionary:
                artifact_folder_dictionary[OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME] = [artifact]
            else:
                artifact_folder_dictionary[OEA_SYNAPSE_FRAMEWORK_FOLDER_NAME].append(artifact)
        else:
            if artifact['properties']['folder']['name'] not in artifact_folder_dictionary:
                artifact_folder_dictionary[artifact['properties']['folder']['name']] = [artifact]
            else:
                artifact_folder_dictionary[artifact['properties']['folder']['name']].append(artifact)

    return artifact_folder_dictionary

# Main app entrypoint.
def main():
    parser = argparse.ArgumentParser(description='A tool for syncing a live OEA Azure Synapse workspace with the OEA repository.')
    parser.add_argument('suffix', help='the suffix for the oea synapse workspace (e.g. syn-oea-\{suffix\})')
    parser.add_argument('repository', help='the repository root')

    args = parser.parse_args(['insmod1', 'C:\\Users\\dastewa\\Documents\\Repos\\OpenEduAnalytics\\'])

    _ensure_oea_root_directory(args.repository)
    _copy_synapse_artifacts(args.suffix, args.repository)

if __name__ == '__main__':
    main()