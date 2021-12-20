'''
Main Training Script

Currently contains all the training components, as well as ancillary calls to responsible ai, registration, and data loading.
'''
import argparse
import importlib
import json
from json.decoder import JSONDecodeError

import mlflow
import pandas as pd

from utils import *
from modeling.OEA_model import OEAModelInterface, ModelType, ExplanationType

def get_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("--datastore_name")
    parser.add_argument("--feature_dataset")
    parser.add_argument("--label_dataset")
    parser.add_argument("--sensitive_feature_dataset")
    parser.add_argument("--key")
    parser.add_argument("--model")
    parser.add_argument("--registered_name")
    parser.add_argument("--test_split", default=.3)

    return parser

def load_class_from_module(class_name):
    module = importlib.import_module('modeling.models')
    my_class = getattr(module, class_name)
    return my_class

def load_datasets(feature_dataset_name, label_dataset_name, sensitive_feature_dataset_name):
    check_dataset_name(feature_dataset_name, "Features")
    X = load_dataset_as_pd(ws, feature_dataset_name)

    check_dataset_name(label_dataset_name, "Labels")
    Y = load_dataset_as_pd(ws, label_dataset_name)

    if check_dataset_name(sensitive_feature_dataset_name, "Sensitive Feature"):
        A = load_dataset_as_pd(ws, sensitive_feature_dataset_name)
    else:
        A = None

    return X, Y, A

if __name__ == "__main__":

    # READ INCOMING PARAMETERS
    parser = get_parser()
    args = parser.parse_args()

    datastore_name = args.datastore_name
    registered_name = args.registered_name

    #model_name = args.model
    #feature_dataset_name = args.feature_dataset
    #label_dataset_name = args.label_dataset
    #sensitive_feature_dataset_name = args.sensitive_feature_dataset
    #testing_split = float(args.test_split)

    ws = get_ws_from_run()
    with mlflow.start_run(nested = True, run_name='TEST') as active_run:

        model_class = load_class_from_module(args.model)

        # CHECKS THAT IMPORTED CLASS MEETS REQUIREMENTS (Redundant if tests were run)
        is_allowed = issubclass(model_class, OEAModelInterface)
        print("Importing class {} - subclass status: {}".format(model_class.__name__, is_allowed))

        # CORE DATA LOADING AND TRAINING
        save_path = registered_name
        example_model = model_class(modelname = registered_name)
        example_model.init_model()

        #TODO: Parse Key for more sophisticated scenarios
        try:
            key_pre = args.key
            key = json.loads(key_pre)
        except JSONDecodeError as e:
            print("JSON Decode Failure for Key: {}, make sure it is an Array of Key values".format(args.key))
            raise e

        # LOAD DATA FROM WORKSPACE
        X, Y, A = load_datasets(
            args.feature_dataset, 
            args.label_dataset, 
            args.sensitive_feature_dataset)

        # STRATIFY BY LABELS IF CATEGORICAL
        if (model_class.model_type == ModelType.regression):
            stratify_value = None
        else:
            stratify_value = Y.drop(key, axis='columns')
        
        # SPLIT DATA ACCORDING TO MODEL DEMANDS
        split_data = example_model.load_split_data(
            X, 
            Y, 
            A, 
            key, 
            split=float(args.test_split), 
            stratify=stratify_value)

        X_train, X_val, X_test, y_train, y_val, y_test, A_train, A_val, A_test, model_classes = split_data

        # RUN TRAINING SCRIPT
        trained_model = example_model.train()
        predictions = example_model.test()

        # MODEL REGISTRATION
        example_model.register_model(save_path)
        model_id = fetch_model_id(example_model.modelname)

        # SAVE PREDICTIONS
        results_name = registered_name+"-results"
        prediction_df = pd.DataFrame(predictions, columns = ['Prediction'])
        results_df = pd.concat([X_test, prediction_df, y_test], axis=1)
        register_dataset_to_store(ws, results_df, results_name)

        # RESPONSIBLE AI
        print("Switching on types: {}, {}".format(model_class.model_type, model_class.explanation_type))

        # EXPLAINABILITY
        interpretability_comment = "this is an interpretability comment"
        try:
            print("EXPLAINABILITY")
            explain_task = "regression" if model_class.model_type == ModelType.regression else "classification"
            if model_class.explanation_type == ExplanationType.normal : 
                global_explanations = interpret_global(model=trained_model, 
                    train=X_train, 
                    test=X_test,
                    features=X_test.columns,
                    classes=model_classes,
                    task = explain_task)

                upload_interpretability_aml(global_explanations, interpretability_comment, y_test.to_numpy())

            elif model_class.explanation_type == ExplanationType.ebm :
                global_explanations = interpret_global(model=trained_model, 
                    train=X_train, 
                    test=X_test,
                    features=X_test.columns,
                    classes=model_classes,
                    task = explain_task)

                upload_interpretability_aml(global_explanations, interpretability_comment, y_test.to_numpy())

                #Currently no Mechanism to upload EBM particular dashboard, upload images instead:
                save_ebm_explanations(trained_model.model)
                upload_image_folder_to_aml("explanations", "images")

        except TypeError as e:
            print("Interpretability Dahsboard not Uploaded, Likely datatype mismatch from spark (no decimal allowed), see error:")
            print(e)

        # FAIRNESS
        sensitive_features = A_test
        if not(sensitive_features is None):
            print("FAIRNESS")
            fairness_comment = f'Fairness dashboard for model: {registered_name} covering columns {sensitive_features.columns}'
            try:
                if (model_class.model_type == ModelType.multiclass_classification):
                    dashboard = fairness_multiclass(trained_model, model_id, sensitive_features, X_test, y_test)
                    upload_fairness_aml(dashboard, fairness_comment)

                elif (model_class.model_type == ModelType.binary_classification):
                    dashboard = fairness_binary(trained_model, model_id, sensitive_features, X_test, y_test)
                    upload_fairness_aml(dashboard, fairness_comment)

                elif (model_class.model_type == ModelType.regression):
                    dashboard = fairness_regression(trained_model, model_id, sensitive_features, X_test, y_test)
                    upload_fairness_aml(dashboard, fairness_comment)
            except ValueError as e:
                print("Fairness Dashboard not Uploaded, Likely data inbalance, see error:")
                print(e)
        else:
            print("No sensitive features provided for Fairness analysis")




