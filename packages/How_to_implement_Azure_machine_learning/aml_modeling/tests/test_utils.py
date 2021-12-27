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
from project import utils as utils
from project.modeling.OEA_model import OEAModelInterface, ModelType, ExplanationType

interpret_list = [cls_obj for cls_name, cls_obj in inspect.getmembers(utils) if cls_name.startswith("interpret_")]

@pytest.fixture(scope="module", params=interpret_list)
def get_interpret(request):
    return request.param

def test_interpret(get_interpret):
    get_interpret
    assert get_interpret