import importlib.util
import pytest

#import dataretrieval
#import hydrofunctions
#import pastas
#import pygeohydro
#import ulmo
#import wellapplication


def test_hydrofunctions():
    '''
    confirm that hydro tools can be found for import.
    '''
    
    assert importlib.util.find_spec("dataretrieval")
    assert importlib.util.find_spec("hydrofunctions")
    assert importlib.util.find_spec("pastas")
    #assert importlib.util.find_spec("pygeohydro")
    #assert importlib.util.find_spec("ulmo")
    #assert importlib.util.find_spec("wellapplication")
