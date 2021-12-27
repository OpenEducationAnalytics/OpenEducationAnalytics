'''
Example submission of MLFlow project to AML

'''

import mlflow
import azureml
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

import os
import argparse
import json

def log_run_details(ws):
    print("SDK version:", azureml.core.VERSION)
    print("MLflow version:", mlflow.version.VERSION)
    print("WS name:", ws.name)
    print("WS resourcegroup:", ws.resource_group)
    print("WS subscription id:", ws.subscription_id)

def get_config_dict(configpath):
    try:
        with open(configpath) as f:
            config_data = json.load(f)
        return config_data
    except Exception as e:
        print("Missing config.json or Malformed AML Config in config.json")
        raise e

def parse_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datastore_name")
    parser.add_argument("--feature_dataset")
    parser.add_argument("--label_dataset")
    parser.add_argument("--sensitive_feature_dataset")
    parser.add_argument("--key")
    parser.add_argument("--model")
    parser.add_argument("--registered_name")
    parser.add_argument("--entrypoint")
    args = parser.parse_args()
    return args

def submit_job(ws, experiment_name, entry="main", compute="DEFAULT_COMPUTE_REPLACE"):

    backend_config = {"COMPUTE": compute, "USE_CONDA": True}

    backend_flag = "azureml"
    datastore = "datastore_stage3"
    feature_dataset_name = 'dataset-dataconfigA-feature'
    label_dataset_name = 'dataset-dataconfigA-label'
    sensitive_dataset_name = 'dataset-dataconfigA-sensitive_feature'
    key = '["StudentDwRefId_pseudonym"]'
    model = 'classification_logisticreg'
    registered_name = 'model_Azure_In_Action'
    
    params = {
        'datastore_name' : datastore,
        'feature_dataset' : feature_dataset_name,
        'label_dataset' : label_dataset_name,
        'sensitive_feature_dataset' : sensitive_dataset_name,
        'key' : key,
        'model' : model,
        'registered_name' : registered_name
    }
    
    mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())
    mlflow.set_experiment(experiment_name)

    remote_run = mlflow.projects.run(uri="./project", 
                                    parameters=params,
                                    entry_point=entry,
                                    backend = backend_flag,
                                    use_conda=True,
                                    backend_config = backend_config)

if __name__ == "__main__":

    config_path = 'config.json'
    
    config_data = get_config_dict(config_path)

    compute_name = "DEFAULT_COMPUTE_REPLACE"
    try:
        compute_name = config_data["compute"]
    except KeyError as e:
        print("No 'compute' in config, using default")
    
    authorization = None
    try:
        tenant = config_data["tenant_id"]
        authorization = InteractiveLoginAuthentication(tenant_id=tenant, force=False)
    except KeyError as e:
        print("No 'tenant_id' in config, logging in to default tenant")
        
    ws = Workspace.from_config(path=config_path, auth=authorization)
    log_run_details(ws)

    submit_job(ws=ws, experiment_name="template_test", entry="main", compute=compute_name)