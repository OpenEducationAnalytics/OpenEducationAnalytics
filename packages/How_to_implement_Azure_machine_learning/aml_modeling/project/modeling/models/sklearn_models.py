from typing import List, Tuple

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import roc_auc_score

from ..OEA_model import OEAModelInterface, ModelType, ExplanationType
from ..modeling_utils import log_metrics

class sklearn_basic(OEAModelInterface):

    def __init__(self, modelname):
        """
        Initialize Basic SKLearn Model utilities (base class)

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
                stratify=stratify,
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
                stratify=stratify,
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
        predictions = self.predictor.predict(data)
        return predictions

    def train(self):
        """
        Trains model based on data originally loaded using load_split_data. Logs training metrics.
                
        Returns
        -------
        self.predictor: sklearn Predictor
            Trained predictor model object
        """

        X_train_val = pd.concat([self.X_train, self.X_val], axis=0)
        y_train_val = np.concatenate([self.y_train, self.y_val], axis=0)

        self.predictor.fit(X_train_val, y_train_val)

        if self.model_type != ModelType.regression:
            preds_prob = self.predictor.predict_proba(X_train_val)[:, 1]
            score_auc = roc_auc_score(y_train_val, preds_prob)

            mlflow.log_metric("train_auc", score_auc)

        return self.predictor

    def test(self):
        """
        Evaluates model on the test set originally loaded using load_split_data. Logs testing metrics and returns predictions on test set.
                
        Returns
        -------
        preds: pandas.DataFrame OR numpy array
            Results of running inference of the predictor
        """
        mlflow.sklearn.eval_and_log_metrics(self.predictor, self.X_test, self.y_test, prefix="test_")
        preds = self.predictor.predict(self.X_test)

        if self.model_type != ModelType.regression:
            preds_prob = self.predictor.predict_proba(self.X_test)[:, 1]
            score_auc = roc_auc_score(self.y_test, preds_prob)
            mlflow.log_metric("test_auc", score_auc)

        return preds
        
    def save_model(self, foldername):
        """
        Save SKLearn Model to a Path
        
        Parameters
        ----------
        foldername: String
            Name of intermediate folder to save model to using mlflow utilities.
        """
        mlflow.sklearn.save_model(self.predictor, foldername)

    def register_model(self, foldername):
        """
        Register Model to repository attached to mlflow instance
        
        Parameters
        ----------
        foldername: String
            Path of folder to upload to model repository

        """
        mlflow.sklearn.log_model(self.predictor, foldername, registered_model_name=self.modelname)

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
        self.predictor: SKLearn Predictor
            Returns the predictor loaded from the registered endpoint
        """
        model_version_uri = "models:/{model_name}/{version}".format(model_name=modelname,version=version)
        self.predictor = mlflow.sklearn.load_model(model_version_uri)

        return self.predictor

class classification_logisticreg(sklearn_basic):
    """
    Model Class for logistic regression. Inherits from base sklearn class (OEA Interface Type)

    Binary Classification type with standard explanation
    """
    model_type = ModelType.binary_classification
    explanation_type = ExplanationType.normal

    def init_model(self):
        """Initialize Logistic Regression Model"""
        mlflow.sklearn.autolog()
        self.predictor = LogisticRegression()
        

class multi_classification_logisticreg(sklearn_basic):
    """
    Model Class for logistic regression. Inherits from base sklearn class (OEA Interface Type)

    Multi-Class Classification type with standard explanation
    """
    model_type = ModelType.multiclass_classification
    explanation_type = ExplanationType.normal

    def init_model(self):
        """Initialize Logistic Regression Model for multi-class classification"""
        mlflow.sklearn.autolog()
        self.predictor = LogisticRegression()

class regression_linearreg(sklearn_basic):
    """
    Model Class for linear regression. Inherits from base sklearn class (OEA Interface Type)

    Regression type with standard explanation
    """
    model_type = ModelType.regression
    explanation_type = ExplanationType.normal

    def init_model(self):
        """Initialize Linear Regression Model for regression problems"""
        mlflow.sklearn.autolog()
        self.predictor = LinearRegression()
