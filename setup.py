#!/usr/bin/env python
import os
import sys

with open("config/version", "r") as f:

  version = f.read().strip()

# import setuptool requirements
try:
    
  from setuptools import setup
  from setuptools.command.test import test as TestCommand

except ImportError:

  from distutils.core import setup


# generate readme as needed before moving forward with anything
with open("readme.rst", "r") as f:

  long_description = f.read()

# load in all requirements for this project as needed
with open("requirements.txt", "r") as f:
  
  requirements = f.read().splitlines()

with open("test-requirements.txt", "r") as f:

  test_requirements = f.read().splitlines()

setup(
    name = "py-config",
    version = version,
    description = "Configuration manager for python projects",
    long_description = long_description,
    url = "http://github.com/jonmorehouse/py-config",
    author = "Jon Morehouse",
    author_email = "morehousej09@gmail.com",
    keywords = ["configuration", "management"],
    license = "MIT",
    packages = ["config",],
    package_data = {"config": ["version"], "": ["requirements.txt", "test-requirements.txt"]},
    install_requires = requirements,
    tests_require = test_requirements,
    test_suite = "nose.collector",
    classifiers=[
            'Development Status :: 4 - Beta',
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



