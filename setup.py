#!/usr/bin/env python
import os
import sys

# import utilities version etc
from utilities import __version__

# import setuptools as needed
try:
	from setuptools import setup
	from setuptools.command.test import test as TestCommand
	
except ImportError:

	from distutils.core import setup

# grab our readme generated rst for this project
with open("readme.rst", "r") as _file:

	long_description = _file.read()

# setup project 
setup(
	
	name="py-config",
	version = __version__,
	description = "General python utilities for projects",
	long_description = long_description,
	url = "http://github.com/jonmorehouse/pyconfig",
	author = "Jon Morehouse",
	author_email = "morehousej09@gmail.com",
	keywords = ["py-config"],
	license = "MIT",
	packages = ["config"],

	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
	]
)
