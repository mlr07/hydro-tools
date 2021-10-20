import pytest
import importlib

import hydrofunctions


# module missing error types: ImportError, ModuleNotFound

def test_hydrofunctions():
    '''
    confirm that hydrofunctions will load as a module
    '''
    assert importlib.util.find_spec("hydrofunctions")


# mark as xfail
def test_bokeh():
    assert importlib.util.find_spec("bokeh")
