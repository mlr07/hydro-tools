import pytest

import dataretrieval
import hydrofunctions
import pygeohydro
import ulmo
import wellapplication

import importlib


# module missing error types: ImportError, ModuleNotFound

def test_hydrofunctions():
    '''
    confirm that all hydro tools will load as a modules.

    this implies that all packages have been installed. 

    '''
    
    assert importlib.util.find_spec("dataretrieval")
    assert importlib.util.find_spec("hydrofunctions")
    assert importlib.util.find_spec("pygeohydro")
    assert importlib.util.find_spec("ulmo")
    assert importlib.util.find_spec("wellapplication")

