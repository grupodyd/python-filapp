#!/usr/bin/env python
#
# Copyright 2015 DyD Dinámica y Desarrollo SAS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''The setup and build script for the python-filapp library.'''

import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='python-filapp',
    version='0.1',
    author='DyD Dinamica y Desarrollo SAS',
    author_email='filapp@filapp.co',
    license='Apache License 2.0',
    url='https://github.com/grupodyd/python-filapp',
    keywords='filapp api',
    description='A Python wrapper around the Filapp API',
    long_description=(read('CHANGES')),
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
