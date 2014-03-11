Python Utilities
================

Config Class
------------

-  a class for managing project variables based upon bash env variables
-  recommended to be used with .export files `Jon Morehouse
   Scripts <https://github.com/jonmorehouse/scripts>`__

Sample Usage
------------

::

    from config import Config

    # load variables from env
    Config.load_from_list(["PATH", "PWD", "ENV"])

    # load an exports file of the following format
    # ENV=PRODUCTION
    # MODULE=TEST
    Config.load_from_path(".test.exports")

    # load yaml/json file
    Config.load_from_path("config.json")
    Config.load_from_path("config.yml")

    # access config
    print Config.PATH 


