'''
This module contains test cases for apy.py
'''


# hasattr(Dynamo, key) and callable(getattr(Dynamo, key))
# https://stackoverflow.com/questions/7580532/how-to-check-whether-a-method-exists-in-python

import api


def test_get_method():

    # GET method
    assert hasattr(api.Titanic, 'get')
    assert callable(getattr(api.Titanic, 'get'))


def test_options_method():

    # OPTIONS method
    assert hasattr(api.Titanic, 'options')
    assert callable(getattr(api.Titanic, 'options'))
