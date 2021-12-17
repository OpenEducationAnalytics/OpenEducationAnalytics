from typing import List, Tuple

import mlflow
import mlflow.lightgbm
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.metrics import roc_auc_score
from lightgbm import LGBMClassifier, LGBMRegressor
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe

from ..OEA_model import OEAModelInterface, ModelType, ExplanationType
from ..modeling_utils import log_metrics

def clip_outputs(pd, min=1, max=4):
    pd[pd < min] = min
    pd[pd > max] = max
    return pd

class lightgbm_basic(OEAModelInterface):
    def __init__(self, modelname):
        """
        Initialize Basic LightGBM Model utilities (base class)

        Parameters
        ----------
        modelname: String
            Name of the model for registration and saving purposes
        """
        self.predictor = None
        self.modelname = modelname

    def load_split_data(self, X, Y, A, key, split=.4, stratify=None):
        """
        Splits Data into training, validation, and test sets
        
        Parameters
        ----------
        X: pandas.DataFrame 
            Feature data
        Y: pandas.DataFrame
            Label data
        A: pandas.DataFrame
            Senstive Feature data (may or may not be overlap with X)
        key: String or List[Strings]
            Columns to identify as Keys for all three dataframes. Dropped at loading time.
        split: Float
            Percentage of data to exclude for testing set
        stratify: pandas.DataFrame
            Dataframe used to stratify split of data. I.e. if labels are provided, will ensure equal label distribution in train / test sets.

        Returns
        -------
        X_train: pandas.DataFrame 
            Feature data for training set
        X_val: pandas.DataFrame 
            Feature data for validation set
        X_test: pandas.DataFrame 
            Feature data for test set
        y_train: pandas.DataFrame
            Label data for training set
        y_val: pandas.DataFrame
            Label data for validation set
        y_test: pandas.DataFrame
            Label data for test set
        A_train: pandas.DataFrame
            Senstive Feature data for training set
        A_val: pandas.DataFrame
            Senstive Feature data for validation set
        A_test: pandas.DataFrame
            Senstive Feature data for test set
        classes: List[str]
           List of classes for classification problem outcomes
        """
        if not (A is None):
            (
                X_train,
                X_val_test,
                y_train,
                y_val_test,
                A_train,
                A_val_test,
            ) = train_test_split(
                X,
                Y,
                A,
                test_size=split,
                random_state=12345,
                # stratify=stratify,
            )

            (X_val, X_test, y_val, y_test, A_val, A_test) = train_test_split(
                X_val_test, y_val_test, A_val_test, test_size=0.5, random_state=12345
            )

        else:
            (X_train, X_val_test, y_train, y_val_test) = train_test_split(
                X,
                Y,
                test_size=split,
                random_state=12345,
                # stratify=stratify,
            )

            (X_val, X_test, y_val, y_test) = train_test_split(
                X_val_test, y_val_test, test_size=0.5, random_state=12345
            )

        X_train = X_train.drop(key, axis='columns').reset_index(drop=True)
        X_val = X_val.drop(key, axis='columns').reset_index(drop=True)
        X_test = X_test.drop(key, axis='columns').reset_index(drop=True)

        y_train = y_train.drop(key, axis='columns')
        y_train = y_train[y_train.columns[:1]].reset_index(drop=True)

        y_val = y_val.drop(key, axis='columns').reset_index(drop=True)
        y_val = y_val[y_val.columns[:1]].reset_index(drop=True)

        y_test = y_test.drop(key, axis='columns').reset_index(drop=True)
        y_test = y_test[y_test.columns[:1]].reset_index(drop=True)
        classes = None

        self.X_train = X_train
        self.X_val = X_val
        self.X_test = X_test
        self.y_train = y_train.values.reshape(-1)
        self.y_val = y_val.values.reshape(-1)
        self.y_test = y_test.values.reshape(-1)
        self.classes = classes
        
        if not(A is None):
            A_train = A_train.drop(key, axis='columns').reset_index(drop=True)
            A_val = A_val.drop(key, axis='columns').reset_index(drop=True)
            A_test = A_test.drop(key, axis='columns').reset_index(drop=True)
            self.A_train = A_train
            self.A_val = A_val
            self.A_test = A_test
        else:
            A_train = None
            A_val = None
            A_test = None
            self.A_train = A_train
            self.A_val = A_val
            self.A_test = A_test
        
        return (
            X_train,
            X_val,
            X_test,
            y_train,
            y_val,
            y_test,
            A_train,
            A_val,
            A_test,
            classes,
        )

    def infer(self, data):
        """
        Infer using model
        
        Parameters
        ----------
        data: pandas.DataFrame OR numpy array
            Feature data

        Returns
        -------
        predictions: pandas.DataFrame OR numpy array
            Results of running inference of the predictor
        
        """
        return self.predictor.predict(data)

    def train(self):
        """
        Trains model based on data originally loaded using load_split_data. Logs training metrics.

        For LightGBM, we call an initial Hyperparameter tuning step before training on the reamining set.
                
        Returns
        -------
        self.predictor: sklearn Predictor
            Trained predictor model object
        """

        best_hyperparams=self.hyper_tune(early_stop=100,num_trial=50)

        params={'num_leaves': int(best_hyperparams['num_leaves']),
                    'min_data_in_leaf': int(best_hyperparams['min_data_in_leaf']),
                    'learning_rate': best_hyperparams['learning_rate'],
                    "lambda_l1": best_hyperparams["lambda_l1"],
                    "lambda_l2": best_hyperparams["lambda_l2"],
                    "max_bin": int(best_hyperparams['max_bin']),
                    "bagging_fraction": best_hyperparams['bagging_fraction'],
                    "feature_fraction": best_hyperparams['feature_fraction'],
                    'objective': 'binary',
                    'max_depth': -1,
                    "boosting": "goss",
                    "bagging_seed": 1024,
                    #'n_estimators': 99999999,
                    "verbosity": -1,
                    "nthread": -1,
                    "random_state": 1024,
                    'metric': 'auc'}       

        self.predictor=LGBMClassifier(**params)
        self.predictor.fit(self.X_train, self.y_train, eval_set = [(self.X_val, self.y_val)],early_stopping_rounds=100)
        
        log_metrics(self, dataset="training")

        return self.predictor

    def test(self):
        """
        Evaluates model on the test set originally loaded using load_split_data. Logs testing metrics and returns predictions on test set.
                
        Returns
        -------
        preds: pandas.DataFrame OR numpy array
            Results of running inference of the predictor
        """
        preds = log_metrics(self, dataset="test")

        return preds
        
    def save_model(self, foldername):
        """
        Save LightGBM Model to a Path
        
        Parameters
        ----------
        foldername: String
            Name of intermediate folder to save model to using mlflow utilities.
        """
        mlflow.lightgbm.save_model(self.predictor.booster_, foldername)

    def register_model(self, foldername):
        """
        Register Model to repository attached to mlflow instance
        
        Parameters
        ----------
        foldername: String
            Path of folder to upload to model repository

        """
        mlflow.lightgbm.log_model(self.predictor.booster_, foldername, registered_model_name=self.modelname)

    def load_model(self, modelname, version):
        """
        Load Model from a registered endpoint

        Parameters
        ----------
        modelname: String
            name of model to load from remote repository
        version: String
            version of model to load from mllow model repository.

        Returns
        -------
        self.predictor: LightGBM Predictor
            Returns the predictor loaded from the registered endpoint
        """
        model_version_uri = "models:/{model_name}/{version}".format(model_name=modelname,version=version)
        self.predictor = mlflow.lightgbm.load_model(model_version_uri)
        return self.predictor
    
    def hyper_tune(self,early_stop=100,num_trial=100):
        """
        Hyper Parameter Tuning for LightGBM classifier

        Parameters
        ----------
        early_stop: Int
            Number of iterations to perform before stopping hyperparameter tuning models
        num_trial: Int
            Number of trials to explore in the hyperparameter tuning space

        Returns
        -------
        best_hyperparams: Dict
            SEt of LightGBM Hyperparameters that lead to best performance on the validation set
        """
        # define hyperparameters need to be tuned and space to search over
        space = {'num_leaves': hp.quniform('num_leaves', 10, 300, 10),        
                'min_data_in_leaf':hp.quniform('min_data_in_leaf', 30, 400, 10),
                'learning_rate': hp.uniform('learning_rate', 0.01, 0.2),
                "lambda_l1":  hp.uniform("lambda_l1", 0.01, 0.2),
                "lambda_l2": hp.uniform("lambda_l2", 0, 0.2),
                'max_bin': hp.quniform('max_bin', 10, 200, 10),
                'bagging_fraction':hp.uniform('bagging_fraction',0.1,0.9),
                'feature_fraction':hp.uniform('feature_fraction',0.1,0.9)
                }

        # define the hyperparameter tuning goal
        def objective(space):
            params = {'num_leaves': int(space['num_leaves']),
                    'min_data_in_leaf': int(space['min_data_in_leaf']),
                    'learning_rate': space['learning_rate'],
                    "lambda_l1": space["lambda_l1"],
                    "lambda_l2": space["lambda_l2"],
                    "max_bin": int(space['max_bin']),
                    "bagging_fraction": space['bagging_fraction'],
                    "feature_fraction": space['feature_fraction'],
                    'objective': 'binary',
                    'max_depth': -1,
                    "boosting": "goss",
                    "bagging_seed": 11,
                    'n_estimators': 99999999,
                    "verbosity": -1,
                    "nthread": -1,
                    "random_state": 1024,
                    'metric': 'auc'}

            lgbm = LGBMClassifier(**params)
            lgbm.fit(self.X_train, self.y_train, eval_set=[
                    (self.X_val, self.y_val)], eval_metric='AUC', early_stopping_rounds=early_stop)

            valid_pred_prob = lgbm.predict_proba(self.X_val)[:, 1]

            score_auc = roc_auc_score(self.y_val, valid_pred_prob)
            valid_pred = lgbm.predict(self.X_val)

            # score_acc = accuracy_score(self.y_val, valid_pred)
            precision, recall, f, _ = precision_recall_fscore_support(self.y_val, valid_pred,average='macro')

            print("SCORE:", score_auc)
            return {'loss': -score_auc, 'status': STATUS_OK}

        # set the hyperparameter tunning configurations and start tuning
        trials = Trials()
        rstate_generated = np.random.default_rng(1024) 
        best_hyperparams = fmin(fn=objective,
                                space=space,
                                algo=tpe.suggest,
                                max_evals=num_trial,
                                trials=trials,
                                rstate=rstate_generated)

        # print out the best hyperparameters
        print("finish tuning, get the best parameters", best_hyperparams)
        return best_hyperparams

class classification_lightgbm(lightgbm_basic):
    """
    Model Class for LightGBM used for Binary Csassification. Inherits from base LightGBM class (OEA Interface Type)

    Classification type with standard explanation type
    """
    model_type = ModelType.binary_classification
    explanation_type = ExplanationType.normal

    def init_model(self):
        """Initialize Model"""
        #mlflow.lightgbm.autolog()
        self.predictor = None

class regression_lightgbm(lightgbm_basic):
    """
    Model Class for LightGBM used for Multiclass Classification. Inherits from base LightGBM class (OEA Interface Type)

    Classifier using underlying regression (ordered classification). Currently clips 1-4, change to number of classes
    """

    model_type = ModelType.multiclass_classification
    explanation_type = ExplanationType.normal

    def init_model(self, clip_min=1, clip_max=4):
        """Initialize Model"""
        self.predictor = None
        self.clip_min = clip_min
        self.clip_max = clip_max

    def hyper_tune(self, early_stop=100, num_trial=100):
        """
        Hyper Parameter Tuning for LightGBM classifier

        Parameters
        ----------
        early_stop: Int
            Number of iterations to perform before stopping hyperparameter tuning models
        num_trial: Int
            Number of trials to explore in the hyperparameter tuning space

        Returns
        -------
        best_hyperparams: Dict
            SEt of LightGBM Hyperparameters that lead to best performance on the validation set
        """
        # define hyperparameters need to be tuned and space to search over
        space = {
            "num_leaves": hp.quniform("num_leaves", 10, 300, 10),
            "min_data_in_leaf": hp.quniform("min_data_in_leaf", 30, 400, 10),
            "learning_rate": hp.uniform("learning_rate", 0.01, 0.2),
            "lambda_l1": hp.uniform("lambda_l1", 0.01, 0.2),
            "lambda_l2": hp.uniform("lambda_l2", 0, 0.2),
            "max_bin": hp.quniform("max_bin", 10, 200, 10),
            "bagging_fraction": hp.uniform("bagging_fraction", 0.1, 0.9),
            "feature_fraction": hp.uniform("feature_fraction", 0.1, 0.9),
        }

        # define the hyperparameter tuning goal
        def objective(space):
            params = {
                "num_leaves": int(space["num_leaves"]),
                "min_data_in_leaf": int(space["min_data_in_leaf"]),
                "learning_rate": space["learning_rate"],
                "lambda_l1": space["lambda_l1"],
                "lambda_l2": space["lambda_l2"],
                "max_bin": int(space["max_bin"]),
                "bagging_fraction": space["bagging_fraction"],
                "feature_fraction": space["feature_fraction"],
                "objective": "regression",
                "max_depth": -1,
                "boosting": "goss",
                "bagging_seed": 11,
                "n_estimators": 99999999,
                "verbosity": -1,
                "nthread": -1,
                "random_state": 1024,
                "metric": "l2"
                
            }

            lgbm = LGBMRegressor(**params)
            lgbm.fit(
                self.X_train,
                self.y_train,
                eval_set=[(self.X_val, self.y_val)],
                eval_metric="l2",
                early_stopping_rounds=early_stop,
            )
            
            valid_pred = lgbm.predict(self.X_val)
            valid_pred = clip_outputs(valid_pred, self.clip_min, self.clip_max)

            valid_pred = np.around(valid_pred).astype(int)
            score_acc = accuracy_score(self.y_val, valid_pred)

            print("SCORE:", score_acc)
            return {"loss": -score_acc, "status": STATUS_OK}

        # set the hyperparameter tunning configurations and start tuning
        trials = Trials()
        rstate_generated = np.random.default_rng(1024)
        best_hyperparams = fmin(
            fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=num_trial,
            trials=trials,
            rstate=rstate_generated,
        )

        # print out the best hyperparameters
        print("finish tuning, get the best parameters", best_hyperparams)
        return best_hyperparams

    def train(self):
        """
        Trains model based on data originally loaded using load_split_data. Logs training metrics.

        For LightGBM, we call an initial Hyperparameter tuning step before training on the reamining set.

        Returns
        -------
        self.predictor: sklearn Predictor
            Trained predictor model object
        """

        best_hyperparams = self.hyper_tune(early_stop=100, num_trial=50)

        params = {
            "num_leaves": int(best_hyperparams["num_leaves"]),
            "min_data_in_leaf": int(best_hyperparams["min_data_in_leaf"]),
            "learning_rate": best_hyperparams["learning_rate"],
            "lambda_l1": best_hyperparams["lambda_l1"],
            "lambda_l2": best_hyperparams["lambda_l2"],
            "max_bin": int(best_hyperparams["max_bin"]),
            "bagging_fraction": best_hyperparams["bagging_fraction"],
            "feature_fraction": best_hyperparams["feature_fraction"],
            "objective": "regression",
            "max_depth": -1,
            "boosting": "goss",
            "bagging_seed": 1024,
            "n_estimators": 99999999,
            "verbosity": -1,
            "nthread": -1,
            "random_state": 1024,
            "metric": "l2"
        }

        self.predictor = LGBMRegressor(**params)
        self.predictor.fit(
            self.X_train,
            self.y_train,
            eval_set=[(self.X_val, self.y_val)],
            eval_metric="l2",
            early_stopping_rounds=100,
        )

        preds = self.predictor.predict(self.X_train)
        preds = clip_outputs(preds, self.clip_min, self.clip_max)
        preds = np.around(preds).astype(int)

        acc = accuracy_score(self.y_train, preds)
        precision, recall, f, _ = precision_recall_fscore_support(
            self.y_train, preds, average="macro"
        )
    
        mlflow.log_metric("train_accuracy_score", acc)
        mlflow.log_metric("train_precision_score", precision)
        mlflow.log_metric("train_recall_score", recall)
        mlflow.log_metric("train_f1_score", f)

        return self.predictor

    def test(self):
        """
        Evaluates model on the test set originally loaded using load_split_data. Logs testing metrics and returns predictions on test set.

        Returns
        -------
        preds: pandas.DataFrame OR numpy array
            Results of running inference of the predictor
        """
        preds = self.predictor.predict(self.X_test)
        preds = clip_outputs(preds, self.clip_min, self.clip_max)
        preds = np.around(preds).astype(int)

        acc = accuracy_score(self.y_test, preds)
        precision, recall, f, _ = precision_recall_fscore_support(
            self.y_test, preds, average="macro"
        )

        mlflow.log_metric("test_accuracy_score", acc)
        mlflow.log_metric("test_precision_score", precision)
        mlflow.log_metric("test_recall_score", recall)
        mlflow.log_metric("test_f1_score", f)

        return preds