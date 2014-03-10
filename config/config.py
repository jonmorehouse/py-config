from os import environ
import json
import yaml
import logging

# grab the current logger
logger = logging.getLogger()

# handle missing key
def error_handler(key):

  logger.warning("Config variable %s not set." % key) 

# set any weird config settings here / defaults as needed
class Config(object):

  @staticmethod
  def load_from_list(variables):
    
    # now for each of the config_variables - set the class attribute
    # note that we want this to throw errors if the environment variable isn't set
    for variable in variables:

      # set the attribute on the class 
      value = environ.get(variable)

      if  value:
        value = setattr(Config, variable, value)

      # if we don't have a default attribute in place and no config - then go ahead and throw an error
      elif not hasattr(Config, variable):
        error_handler(variable)

  @staticmethod
  def load_from_file(path): 
  
    # first find out the extension of the file as needed 
    # then loop through and set the various values as needed in different manners
    extension = path.split(".")[-1]
    with open(path) as f:
      contents = f.read()
  
      if extension == "json":
        Config._load_json(contents)

      elif extension == "yml":
        Config._load_yaml(contents)

      elif extensions == "exports":
        Config._load_exports(contents)

      else:
        logger.warning("Not a known file extension." % path) 
                
  @classmethod
  def _load_exports(self, contents):

    # grab all the lines that aren't blank and don't start with a #
    for line in [line.strip() for line in contents.split("\n") if len(line) > 0 and line.strip()[0] != "#"]:
      key = line.split("=")[0]
      value = environ.get(key)

      if value:
        setattr(self, key, value)
      else:
        error_handler(key)

  @classmethod
  def _load_yaml(self, contents):

    config = yaml.load(contents)

    for key, value in config.iteritems():
      setattr(self, key, value)

  @classmethod
  def _load_json(self, contents):

    config = json.loads(contents)

    for key, value in config.iteritems():
      setattr(self, key, value)
    

