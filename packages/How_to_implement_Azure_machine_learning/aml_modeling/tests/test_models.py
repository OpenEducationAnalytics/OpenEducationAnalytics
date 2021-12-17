'''
RUN 'Python -m pytest' from parent directory
'''

import sys
import inspect
import unittest
import importlib

import pytest   
from _pytest.mark import param

import pandas as pd
import numpy as np
from project.modeling import models as oea_models
from project.modeling.OEA_model import OEAModelInterface, ModelType, ExplanationType

class_list = [cls_obj for cls_name, cls_obj in inspect.getmembers(oea_models) if inspect.isclass(cls_obj)]

'''
Setup Scripts (Parametrized to All new Classes)
'''
@pytest.fixture(scope="module", params=class_list)
def get_class(request):
    return request.param

@pytest.fixture
def initialize_model(get_class):
    example_model = get_class(modelname = "tests")
    example_model.init_model()
    return example_model

@pytest.fixture
def load_test_data():
    import sklearn.datasets

    iris_dataset_X, iris_dataset_Y = sklearn.datasets.load_iris(as_frame=True, return_X_y=True)
    iris_dataset_X.insert(0, 'MockKey', '')
    iris_dataset_Y = iris_dataset_Y.to_frame()
    iris_dataset_Y.insert(0, 'MockKey', '')

    return iris_dataset_X, iris_dataset_Y

'''
Class Structure Tests
'''
def test_subclass_status(get_class):
    truth = issubclass(get_class, OEAModelInterface)
    assert True == truth

def test_has_modeltype(initialize_model):
    assert initialize_model.model_type in ModelType

def test_has_explanationtype(initialize_model):
    assert initialize_model.explanation_type in ExplanationType

'''
Data Loading Tests
'''
def test_can_load_with_no_A(initialize_model, load_test_data):
    X, Y = load_test_data
    X_train, X_val, X_test, y_train, y_val, y_test, A_train, A_val, A_test, classes = initialize_model.load_split_data(X, Y, None, key="MockKey")

    #Ensure Type Matching
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_val, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_val, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)

    #Ensure Nulls
    assert A_train == None
    assert A_val == None
    assert A_test == None

    #Ensure Type Matching
    assert isinstance(initialize_model.X_train, pd.DataFrame)
    assert isinstance(initialize_model.X_val, pd.DataFrame)
    assert isinstance(initialize_model.X_test, pd.DataFrame)

    #Check Reshape
    assert isinstance(initialize_model.y_train, np.ndarray)
    assert isinstance(initialize_model.y_val, np.ndarray)
    assert isinstance(initialize_model.y_test, np.ndarray)

    #Ensure Nulls
    assert initialize_model.A_train == None
    assert initialize_model.A_val == None
    assert initialize_model.A_test == None


def test_can_load_with_A(initialize_model, load_test_data):
    X, Y = load_test_data
    initialize_model.load_split_data(X, Y, X, key="MockKey")

    X_train, X_val, X_test, y_train, y_val, y_test, A_train, A_val, A_test, classes = initialize_model.load_split_data(X, Y, X, key="MockKey")

    #Ensure Type Matching
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_val, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_val, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)

    #Ensure Type Matching for Sensitive Data
    assert isinstance(A_train, pd.DataFrame)
    assert isinstance(A_val, pd.DataFrame)
    assert isinstance(A_test, pd.DataFrame)

    #Ensure Type Matching
    assert isinstance(initialize_model.X_train, pd.DataFrame)
    assert isinstance(initialize_model.X_val, pd.DataFrame)
    assert isinstance(initialize_model.X_test, pd.DataFrame)

    #Check Reshape
    assert isinstance(initialize_model.y_train, np.ndarray)
    assert isinstance(initialize_model.y_val, np.ndarray)
    assert isinstance(initialize_model.y_test, np.ndarray)

    #Ensure Type Matching for Sensitive Data
    assert isinstance(initialize_model.A_train, pd.DataFrame)
    assert isinstance(initialize_model.A_val, pd.DataFrame)
    assert isinstance(initialize_model.A_test, pd.DataFrame)

    assert initialize_model
