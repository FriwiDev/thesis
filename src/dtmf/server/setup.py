# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "dtmf_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="DTMF",
    author_email="",
    url="",
    keywords=["OpenAPI", "DTMF"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['dtmf_server=dtmf_server.__main__:main']},
    long_description="""\
    A simple API to interact with the Domain Tunnel Management Function. Supports reserving, creating and removing tunnels from one external domain to another external domain. This service does not create tunnel endpoints, but reserves resources instead in the current domain instead. The DTMF is a subset of the DSMF. Please refer to the topology drawings for further information about the network structures.
    """
)

