'''
Utilities related to interacting with Azure ML for model registration and datasets from synapse
'''

import os
import mlflow
import json

from azureml.core.run import Run
from azureml.core.model import Model
from azureml.core import Workspace, Datastore, Dataset

import azureml
from azureml.interpret import ExplanationClient
from azureml.contrib.fairness import upload_dashboard_dictionary, download_dashboard_by_upload_id
from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Experiment, Workspace, Dataset, Datastore
from azureml.data.dataset_factory import TabularDatasetFactory

import json

def get_ws_from_login(config_path):
    '''
    Useful if having trouble with login from config, instead can login manually. Enter info here
    '''
    interactive_auth = InteractiveLoginAuthentication(tenant_id="TENANT_ID", force=True)
    ws = Workspace(subscription_id="SUB_ID",
               resource_group="RG_NAME",
               workspace_name="WS_NAME",
               auth=interactive_auth)
    return ws

def get_ws_from_run():
    run = Run.get_context()
    ws = run.experiment.workspace

    return ws

def log_run_details(ws):
    print("SDK version:", azureml.core.VERSION)
    print("MLflow version:", mlflow.version.VERSION)
    print("WS name:", ws.name)
    print("WS resourcegroup:", ws.resource_group)
    print("WS subscription id:", ws.subscription_id)

def check_dataset_name(name, extra="Sensitive Data"):
    if name.lower().rstrip("\\") != "none":
        return True
    else:
        print(f"Invalid Dataset name - {extra}")
        return False

def load_dataset_as_pd(ws, dataset_name):
    if dataset_name.lower().rstrip("\\") != "none":
        dataset = Dataset.get_by_name(workspace = ws, name = dataset_name).to_pandas_dataframe()
        return dataset
    return None

def register_model_sk(model, foldername, modelname) :
    ws = get_ws_from_run()

    mlflow.sklearn.log_model(model, foldername, registered_model_name=modelname)
    model_id = Model(ws, modelname).id

    return model_id

def fetch_model_id(modelname, version=None):
    ws = get_ws_from_run()
    return  Model(ws, name=modelname, version=version).id

def save_model_sk(model, foldername):
    mlflow.sklearn.save_model(model, foldername)

def upload_interpretability_aml(global_explanation, comment, y_test):
    #Extract explanation client (remote or local?)
    run = Run.get_context()
    client = ExplanationClient.from_run(run)
    client.upload_model_explanation(global_explanation, comment=comment, true_ys=y_test)

def upload_fairness_aml(dash_dict, dashboard_title):
    #Upload Fairness evaluation to AzureML
    run = Run.get_context()
    upload_id = upload_dashboard_dictionary(run,
                                            dash_dict,
                                            dashboard_name=dashboard_title)
def upload_image_folder_to_aml(name, path):
    run = Run.get_context()
    run.upload_folder(name=name, path=path)
    mlflow.log_artifacts(name, artifact_path=path)

def register_dataset_to_store(ws, df, name):
    datastore = Datastore.get_default(ws)
    TabularDatasetFactory.register_pandas_dataframe(df, datastore, name = name)
