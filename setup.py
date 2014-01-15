#!/usr/bin/env python
import os
import sys

from utilities import __version__

# setup project
setup(
	
	name="utilities",
	version = __version__,
	description = "General python utilities for projects",
	url = "http://github.com/jonmorehouse/python-utilities",
	author = "Jon Morehouse",
	author_email = "morehousej09@gmail.com",
	keywords = ["Utilities"],
	license = "MIT",
	packages = ["redis"],

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
