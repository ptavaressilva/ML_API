'''
This module contains test cases for api.py
'''

import api
from pathlib import Path


def test_get_method():

    # GET method
    assert hasattr(api.Titanic, 'get')
    assert callable(getattr(api.Titanic, 'get'))


def test_options_method():

    # OPTIONS method
    assert hasattr(api.Titanic, 'options')
    assert callable(getattr(api.Titanic, 'options'))


def test_ML_files_exist():
    assert Path("ML/DecisionTreeClassifier.pkl").is_file()
    assert Path("ML/encoder.pkl").is_file()
    assert Path("ML/scaler.pkl").is_file()
