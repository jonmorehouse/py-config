from os import environ
import logging

# grab the current logger
logger = logging.getLogger()

# set any weird config settings here / defaults as needed
class Config(object):

	@staticmethod
	def load(variables):
		
		# now for each of the config_variables - set the class attribute
		# note that we want this to throw errors if the environment variable isn't set
		for variable in variables:

			# set the attribute on the class 
			value = environ.get(variable)

			# if the value exists - set it as a class attribute
			if  value:

				value = setattr(Config, variable, value)

			# if we don't have a default attribute in place and no config - then go ahead and throw an error
			elif not hasattr(Config, variable):

				# log a warning here
				logger.warning("Config variable %s not set." % variable) 


