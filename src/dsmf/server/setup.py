# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "dsmf_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.2",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.1",
    "flask==2.3.2",
    "aiohttp_cors>=0.7.0",
    "werkzeug>=2.2.3"
]

setup(
    name=NAME,
    version=VERSION,
    description="DSMF",
    author_email="",
    url="",
    keywords=["OpenAPI", "DSMF"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['dsmf_server=dsmf_server.__main__:main']},
    long_description="""\
    A simple API to interact with the Domain Slice Management Function. Supports reserving, creating and removing slices and tunnels from one external domain to another external domain or host. Please refer to the topology drawings for further information about the network structures.
    """
)

