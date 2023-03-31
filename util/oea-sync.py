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
from azure.core.exceptions import HttpResponseError

# 1. Get synapse suffix and destination directory
# 2. Ensure read/write access to each file and folder in directory/subdirectories.
# 3. Azure login
# 4. Get synapse data one by one, and copy into root folder.

# Constants
ROOT_FOLDERS = ['framework', 'modules', 'packages', 'schemas']
OEA_SYNAPSE_WORKSPACE_PREFIX = 'syn-oea'
OEA_SYNAPSE_DEV_WORKSPACE_FORMAT_STRING = 'https://syn-oea-{}.dev.azuresynapse.net'

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

    # get datasets
    _copy_synapse_datasets(client, path)

    # get notebooks
    # get pipelines
    # linked services
    # sql scripts

def _copy_synapse_datasets(client, path):
    dataset_iterator = client.dataset.get_datasets_by_workspace()
    datasets = []
    for item in dataset_iterator:
        datasets.append(item)

    print(datasets[0])

    ds_file = client.dataset.get_dataset(datasets[0].name)

    print(ds_file.properties)
    
    pass

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

