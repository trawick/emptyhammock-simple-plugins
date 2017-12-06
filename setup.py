#!/usr/bin/env python3

import os
import sys

from setuptools import find_packages, setup

import simple_plugins

VERSION = simple_plugins.__version__

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

setup(
    name='emptyhammock_simple_plugins',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0 License',
    version=VERSION,
    description='A Django app providing simple plugins for Django CMS',
    author='Emptyhammock Software and Services LLC',
    author_email='info@emptyhammock.com',
    url='https://github.com/trawick/emptyhammock-simple-plugins',
    keywords=['django', 'cms'],
    classifiers=[
        'License :: OSI Approved :: Apache 2.0 License',
        'Development Status :: 3 - Alpha',
    ],
)
