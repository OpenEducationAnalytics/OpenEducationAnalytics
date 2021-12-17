from typing import List, Tuple

import mlflow

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from interpret.glassbox import ExplainableBoostingClassifier, ExplainableBoostingRegressor

from ..OEA_model import OEAModelInterface, ModelType, ExplanationType
from ..modeling_utils import log_metrics

class mlflow_pyfunc_wrapper(mlflow.pyfunc.PythonModel):
    """
    Wrapper class that allows us to use generic predictors in the mlflow pyfunc format. 
    Used to wrap predictor types that are not already in the mlflow.* setup.
    In order to work with this class, needs to have generic: predict, fit, score, predict_proba functions
    """
    def __init__(self, model):  
        """
        Initialized Wrapped python model

        Parameters
        ----------
        model: Python Object
            A model that implements the predict, fit, score, and predict_proba functions
        """        
        self.model = model

    def predict(self, *args):
        """
        Use Predict function of wrapped model

        Parameters
        ----------
        *args : 
            Arguments needed for wrapped predict function 

        Returns
        -------
        predictions: pandas.DataFrame or numpy.ndarray
            Predictions of wrapped model on passed arguments
        """
        predictions = self.model.predict(*args)
        return predictions

    def fit(self, *args):
        """
        Train/Fit Wrapped model on passed arguments

        Parameters
        ----------
        *args : 
            Arguments needed for wrapped fit(train) function 

        Returns
        -------
            Wrapped model after being fit on passed arguments

        """    
        return self.model.fit(*args)

    def score(self, *args):
        """
        Predicts and Scores the wrapped model on passed arguments

        Parameters
        ----------
        *args : 
            Arguments needed for wrapped score function 

        Returns
        -------
        score: Float
            Resulting score of wrapped model score function. (Generally accuracy)

        """ 
        score = self.model.score(*args)
        return score

    def predict_proba(self,*args):
        """
        Generate prediction probabilities of the wrapped model on passed arguments

        Parameters
        ----------
        *args : 
            Arguments needed for wrapped prediction probability functin

        Returns
        -------
        probabilities: pandas.DataFrame or numpy.ndarray
            Predicted output probabilities

        """
        probabilities = self.model.predict_proba(*args)
        return probabilities

class wrapped_basic(OEAModelInterface):
    def __init__(self, modelname):
        """
        Initialize Basic Wrapped Pyfunc Model utilities (base class)

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
        return self.predictor.predict(data)

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

        log_metrics(self, dataset="training_val")
        
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
        Save Wrapped Pyfunc Model to a Path
        
        Parameters
        ----------
        foldername: String
            Name of intermediate folder to save model to using mlflow utilities.
        """
        mlflow.pyfunc.save_model(foldername, python_model=self.predictor)

    def register_model(self, foldername):
        """
        Register Model to repository attached to mlflow instance
        
        Parameters
        ----------
        foldername: String
            Path of folder to upload to model repository

        """
        mlflow.pyfunc.log_model(foldername, python_model=self.predictor, registered_model_name=self.modelname)

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
        self.predictor: Wrapped PyFunc Predictor
            Returns the predictor loaded from the registered endpoint
        """
        model_version_uri = "models:/{model_name}/{version}".format(model_name=modelname,version=version)
        self.predictor = mlflow.pyfunc.load_model(model_version_uri)

        return self.predictor

class classification_EBM(wrapped_basic):
    """
    Model Class for EBM used for Binary CLassification. Inherits from base wrapped model class (OEA Interface Type)

    Classification type with Eplainable Boosting Machine special explanation type
    """
    model_type = ModelType.binary_classification
    explanation_type = ExplanationType.ebm

    def init_model(self, seed=5):
        """Initialize Model"""
        self.predictor = mlflow_pyfunc_wrapper(ExplainableBoostingClassifier(random_state=seed))

class multi_classification_EBM(wrapped_basic):
    """
    Model Class for EBM used for Multiclass CLassification. Inherits from base wrapped model class (OEA Interface Type)

    Multiclass Classification type with Eplainable Boosting Machine special explanation type
    """
    model_type = ModelType.multiclass_classification
    explanation_type = ExplanationType.ebm

    def init_model(self, seed=5):
        """Initialize Model"""
        self.predictor = mlflow_pyfunc_wrapper(ExplainableBoostingClassifier(random_state=seed))

class regression_EBM(wrapped_basic):
    """
    Model Class for EBM used for Regression. Inherits from base wrapped model class (OEA Interface Type)

    Regression type with Eplainable Boosting Machine special explanation type
    """
    model_type = ModelType.regression
    explanation_type = ExplanationType.ebm

    def init_model(self, seed=5):
        """Initialize Model"""
        self.predictor = mlflow_pyfunc_wrapper(ExplainableBoostingRegressor(random_state=seed))
