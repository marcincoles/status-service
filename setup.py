# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='status-service',
    version='0.1.0',
    description='A service that reports the status of other services'
    long_description=readme,
    author='Marcin Coles',
    author_email='tbd',
    url='https://github.com/marcincoles/status-service',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
) 
                                            )
