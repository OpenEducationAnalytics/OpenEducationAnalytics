import os

class OEAFrameworkInstaller:
    def __init__(self, azure_client, storage_account, keyvault, synapse_workspace, framework_path_relative, logger):
        self.azure_client = azure_client
        self.storage_account = storage_account
        self.keyvault = keyvault
        self.synapse_workspace = synapse_workspace
        self.logger = logger
        self.framework_path_relative = framework_path_relative

    def replace_strings(self, file_path):
        with open(file_path) as f:
            data = f.read()
            data = data.replace('yourkeyvault', self.keyvault)\
                        .replace('yourstorageaccount', self.storage_account)\
                        .replace('yoursynapseworkspace', self.synapse_workspace)
        with open(file_path, 'wt') as f:
            f.write(data)

    def install_linked_services(self):
        if(os.path.isdir(f'{self.framework_path_relative}/linkedService/' is False)):
            self.logger.info('No Linked Service to Install.')
            return
        linked_services = os.listdir(f'{self.framework_path_relative}/linkedService/')
        for ls in linked_services:
            try:
                self.replace_strings(f'{self.framework_path_relative}/linkedService/{ls}')
                self.azure_client.create_linked_service(self.synapse_workspace, ls.split('.')[0], f'{self.framework_path_relative}/linkedService/{ls}')
            except Exception as e:
                self.logger.error(f"Failed to install the Linked Service - {ls.split('.')[0]} : {str(e)}")

    def install_datasets(self):
        if(os.path.isdir(f'{self.framework_path_relative}/dataset/' is False)):
            self.logger.info('No Dataset to Install.')
            return
        datasets = os.listdir(f'{self.framework_path_relative}/dataset/')
        for dataset in datasets:
            try:
                self.replace_strings(f'{self.framework_path_relative}/dataset/{dataset}')
                self.azure_client.create_dataset(self.synapse_workspace, dataset.split('.')[0], f'{self.framework_path_relative}/dataset/{dataset}')
            except Exception as e:
                self.logger.error(f"Failed to install the Dataset - {dataset.split('.')[0]} : {str(e)}")

    def install_notebooks(self):
        if(os.path.isdir(f'{self.framework_path_relative}/notebook/' is False)):
            self.logger.info('No Notebook to Install.')
            return
        notebooks = os.listdir(f'{self.framework_path_relative}/notebook/')
        for notebook in notebooks:
            try:
                self.replace_strings(f"{self.framework_path_relative}/notebook/{notebook}")
                if('json' in notebook):
                    self.azure_client.create_notebook(f"{self.framework_path_relative}/notebook/{notebook}", self.synapse_workspace)
                else:
                    self.azure_client.create_notebook_with_ipynb(notebook.split('.')[0], f"{self.framework_path_relative}/notebook/{notebook}", self.synapse_workspace)
            except Exception as e:
                self.logger.error(f"Failed to install the Notebook - {notebook.split('.')[0]} : {str(e)}")

    def install_pipelines(self):
        if(os.path.isdir(f'{self.framework_path_relative}/pipeline/' is False)):
            self.logger.info('No Pipelines to Install.')
            return
        pipelines = [item for item in os.listdir(f'{self.framework_path_relative}/pipeline/') if os.path.isfile(f'{self.framework_path_relative}/pipeline/{item}')]
        for pipeline in pipelines:
            try:
                self.replace_strings(f'{self.framework_path_relative}/pipeline/{pipeline}')
                self.azure_client.create_or_update_pipeline(self.synapse_workspace, f'{self.framework_path_relative}/pipeline/{pipeline}', pipeline.split('.')[0])
            except Exception as e:
                self.logger.error(f"Failed to install the Pipeline - {pipeline.split('.')[0]} : {str(e)}")

    def install_dataflows(self):
        if(os.path.isdir(f'{self.framework_path_relative}/dataflow/' is False)):
            self.logger.info('No Dataflows to Install.')
            return
        dataflows = [item for item in os.listdir(f'{self.framework_path_relative}/dataflow/') if os.path.isfile(f'{self.framework_path_relative}/pipeline/{item}')]
        for dataflow in dataflows:
            try:
                self.replace_strings(f'{self.framework_path_relative}/dataflow/{dataflow}')
                self.azure_client.create_or_update_dataflow(self.synapse_workspace, f'{self.framework_path_relative}/dataflow/{dataflow}', dataflow.split('.')[0])
            except Exception as e:
                self.logger.error(f"Failed to install the Dataflow - {dataflow.split('.')[0]} : {str(e)}")

    def install(self):
        self.logger.info('--> 1) Installing Linked Services')
        self.install_linked_services()

        self.logger.info('--> 2) Installing Datasets')
        self.install_datasets()

        self.logger.info('--> 3) Installing Notebooks')
        self.install_notebooks()

        self.logger.info('--> 4) Installing Pipelines')
        self.install_pipelines()

        self.logger.info('--> 5) Installing Dataflows')
        self.install_dataflows()
