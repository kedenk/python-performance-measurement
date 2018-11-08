#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='python-performance-measurement',
    version='1.0',
    description='Performance measurement for methods',
    author='kedenk',
    url='https://github.com/kedenk/python-performance-measurement',
    license='MIT',
    packages=find_packages(exclude=["tests", "tests.*"]),
    )
