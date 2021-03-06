#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='localtunnel',
    version='0.4.0',
    author='Jeff Lindsay',
    author_email='jeff.lindsay@twilio.com',
    description='',
    packages=find_packages(),
    install_requires=['ginkgo', 'ws4py'],
    data_files=[],
    entry_points={
        'console_scripts': [
            'lt = localtunnel.client:main',]},
)
