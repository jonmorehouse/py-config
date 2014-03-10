import nose
import unittest
import json
import yaml
import os

# project includes
import fixtures
from config.config import Config

class TestConfig(unittest.TestCase):

  def test_load_from_list(self):
    
    Config.load_from_list(["PATH", "PWD", "DOESNT_EXIST"])
    assert hasattr(Config, "PATH")
    assert hasattr(Config, "PWD")
    assert hasattr(Config, "DOESNT_EXIST") == False
      
  def test_load_from_json(self): 

    # ensure that the json was parsed properly
    json_config = json.loads(fixtures.JSON)
    Config._load_json(fixtures.JSON)

    for key, value in json_config.iteritems():
      assert hasattr(Config, key)
      assert getattr(Config, key) == value

  def test_load_from_yaml(self):
  
    # parse the yaml file
    yaml_config = yaml.load(fixtures.YAML)
    Config._load_yaml(fixtures.YAML) 

    for key, value in yaml_config.iteritems():
      assert hasattr(Config, key)
      assert getattr(Config, key) == value
    
  def test_load_from_exports(self):

    # grab the file as needed
    Config._load_exports(fixtures.EXPORTS)

    assert hasattr(Config, "PATH")
    assert hasattr(Config, "UNDEFINED") == False
     

