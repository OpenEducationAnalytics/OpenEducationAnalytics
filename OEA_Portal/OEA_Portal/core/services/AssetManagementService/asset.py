import os
import json
import time
from OEA_Portal.settings import OEA_ASSET_TYPES, BASE_DIR
from OEA_Portal.core.models import OEAInstance
from ..SynapseManagementService import SynapseManagementService
from OEA_Portal.auth.AzureClient import AzureClient
from .operations import *
from ..utils import download_and_extract_zip_from_url

class BaseOEAAsset:
    """
    A BaseOEAAsset class represents an OEA Asset - module, package or schema.
    """
    def __init__(self, asset_name:str, version:str, asset_type:str):
        if(asset_type not in OEA_ASSET_TYPES):
            raise Exception(f"{asset_type} is not an OEA supported Asset type.")
        self.asset_name = asset_name
        self.version = version
        self.asset_type = asset_type
        self.local_asset_download_path = f"{BASE_DIR}/downloads/{asset_type}"
        self.local_asset_root_path =f"{BASE_DIR}/downloads/{asset_type}/{self.asset_type}_{self.asset_name}_v{self.version}"

        # Synapse Artifacts associated with the Asset.
        self.pipelines = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/pipeline"))) if os.path.isdir(f"{self.local_asset_root_path}/pipeline") else []
        self.dataflows = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/dataflow"))) if os.path.isdir(f"{self.local_asset_root_path}/dataflow") else []
        self.datasets = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/dataset"))) if os.path.isdir(f"{self.local_asset_root_path}/dataset") else []
        self.notebooks = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/notebook"))) if os.path.isdir(f"{self.local_asset_root_path}/notebook") else []
        self.linked_services = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/linkedService"))) if os.path.isdir(f"{self.local_asset_root_path}/linkedService") else []
        self.integration_runtimes = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/integrationRuntime"))) if os.path.isdir(f"{self.local_asset_root_path}/integrationRuntime") else []
        self.sql_scripts = list(filter( lambda x: '.md' not in x, os.listdir(f"{self.local_asset_root_path}/sqlScript"))) if os.path.isdir(f"{self.local_asset_root_path}/sqlScript") else []

        self.asset_url = f"https://github.com/microsoft/OpenEduAnalytics/releases/download/{asset_type}_{asset_name}_v{version}/{asset_type}_{asset_name}_v{version}.zip"
        #todo: Check If exists before downloading.
        if os.path.isdir(self.local_asset_root_path) is False:
            download_and_extract_zip_from_url(self.asset_url, self.local_asset_download_path)
        self.dependency_dict = create_dependency_matrix_by_reading_all_files(f"{self.local_asset_root_path}/pipeline")
        self.pipelines_dependency_order = create_pipeline_dependency_order(self.dependency_dict)

    def _verify_version_dependency(self, source_version:float, target_version:float, operation):
        if operation == '>':
            return source_version > target_version
        elif operation == '<':
            return source_version < target_version
        elif operation == '<=':
            return source_version <= target_version
        elif operation == '>=':
            return source_version >= target_version
        elif operation == '==':
            return source_version == target_version

    def _verify_asset_dependency(self, assets, dependent_asset, target_version, operation):
        if not(any(asset.asset_name == dependent_asset for asset in assets)):
            raise Exception(f"The asset you are trying to install has a dependency on the '{dependent_asset}' asset")

        installed_asset = next(asset for asset in assets if asset.asset_name == dependent_asset)
        if self._verify_version_dependency(installed_asset.version, target_version, operation) is False:
            raise Exception(f"The asset you are trying to install requires '{dependent_asset}' {operation} '{target_version}'. But found version {installed_asset.version}")


    def _validate_asset_installation(self, azure_client:AzureClient, oea_instance:OEAInstance):
        operators = ["==", ">=", "<=", ">", "<"]
        modules, packages, schemas, oea_version = get_installed_assets_in_workspace(oea_instance.workspace_name, azure_client)
        with open(f"{self.local_asset_root_path}/dependency.txt") as f:
            dependencies = f.readlines()
        for dependency in dependencies:
            op = next(op for op in operators if op in dependency)
            dependent_asset = dependency.split(op)[0].replace(' ', '')
            target_version = dependency.split(op)[1].replace(' ', '')
            if dependent_asset == 'OEA':
                if self._verify_version_dependency(oea_version, target_version, op) is False:
                    raise Exception(f"Expected {dependent_asset} asset to be {op} {target_version}. But found {oea_version}")
            else:
                if dependent_asset.split('_')[0] == 'module':
                    self._verify_asset_dependency(modules, '_'.join(dependent_asset.split('_')[1:]), target_version, op)
                elif dependent_asset.split('_')[0] == 'package':
                    self._verify_asset_dependency(packages, '_'.join(dependent_asset.split('_')[1:]), target_version, op)
                elif dependent_asset.split('_')[0] == 'schema':
                    self._verify_asset_dependency(schemas, '_'.join(dependent_asset.split('_')[1:]), target_version, op)


    def install(self, azure_client:AzureClient, oea_instance:OEAInstance):
        """
        Installs the Asset into the given Synapse workspace.
        """
        self._validate_asset_installation(azure_client, oea_instance)
        sms = SynapseManagementService(azure_client, oea_instance.resource_group)
        pipeline_file_names = [f"{pipeline}.json" for pipeline in self.pipelines_dependency_order]
        try:
            ir_pollers = sms.install_all_integration_runtimes(oea_instance, f"{self.local_asset_root_path}/integrationRuntime", self.integration_runtimes, wait_till_completion=False)
            ls_pollers = sms.install_all_linked_services(oea_instance, f"{self.local_asset_root_path}/linkedService", self.linked_services, wait_till_completion=False)
            nb_pollers = sms.install_all_notebooks(oea_instance, f"{self.local_asset_root_path}/notebook", self.notebooks, wait_till_completion=False)
            if ls_pollers is not None:
                # Wait for Datasets to install.
                while(any(poller.status() == 'InProgress' for poller in ls_pollers)):
                    time.sleep(2)
            ds_pollers = sms.install_all_datasets(oea_instance, f"{self.local_asset_root_path}/dataset", self.datasets, wait_till_completion=False)

            if ds_pollers is not None:
                # Wait for Datasets to install.
                while(any(poller.status() == 'InProgress' for poller in ds_pollers)):
                    time.sleep(2)

            df_pollers = sms.install_all_dataflows(oea_instance, f"{self.local_asset_root_path}/dataflow", self.dataflows, wait_till_completion=False)

            # Wait for dataflows, notebooks and integration runtimes to install.
            while(any(poller.status() == 'InProgress' for poller in df_pollers + nb_pollers + ir_pollers)):
                time.sleep(2)

            sms.install_all_pipelines(oea_instance, f"{self.local_asset_root_path}/pipeline", pipeline_file_names)

        except RuntimeError as e:
            raise RuntimeError(f"Error while installing asset '{self.asset_display_name}' on the workspace '{oea_instance.workspace_name} - {str(e)}")

        # log_installed_asset(azure_client, oea_instance.workspace_name, oea_instance.storage_account, self.asset_type, self.asset_display_name, self.version)

    def uninstall(self, azure_client:AzureClient, oea_instance:OEAInstance):
        """
        Uninstalls the Asset into the given Synapse workspace.
        """
        sms = SynapseManagementService(azure_client, oea_instance.resource_group)

        sms.delete_all_pipelines(oea_instance.workspace_name, pipelines=[pl.split('.')[0] for pl in self.pipelines_dependency_order[::-1]], wait_till_completion=True)

        nb_pollers = sms.delete_all_notebooks(oea_instance.workspace_name, notebooks=[nb.split('.')[0] for nb in self.notebooks], wait_till_completion=False)

        df_pollers = sms.delete_all_dataflows(oea_instance.workspace_name, dataflows=[df.split('.')[0] for df in self.dataflows], wait_till_completion=False)

        ir_pollers = sms.delete_all_integration_runtimes(oea_instance.resource_group, oea_instance.workspace_name, integration_runtimes=[ir.split('.')[0] for ir in self.integration_runtimes], wait_till_completion=False)
        if df_pollers:
            while(any(poller.status() == 'InProgress' for poller in df_pollers)):
                time.sleep(2)
        ds_pollers = sms.delete_all_datasets(oea_instance.workspace_name, datasets=[ds.split('.')[0] for ds in self.datasets], wait_till_completion=False)

        if ds_pollers:
            while(any(poller.status() == 'InProgress' for poller in ds_pollers)):
                time.sleep(2)
        ls_pollers = sms.delete_all_linked_services(oea_instance.workspace_name,linked_services=[ls.split('.')[0] for ls in self.linked_services], wait_till_completion=False)
