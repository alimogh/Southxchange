#!/usr/bin/python3.8

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='Southxchange',
   version='1.1',
   url='https://github.com/Zenitsudeck/Southxchange',
   long_description=long_description,
   description='Southxchange',
   author='Zenitsudeck',
   author_email='',
   packages=['Southxchange'],
   install_requires=['requests'],
)
