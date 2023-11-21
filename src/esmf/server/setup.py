# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "esmf_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==3.0.2",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.1",
    "flask==2.3.3",
    "aiohttp_cors>=0.7.0",
    "werkzeug>=2.2.3",
    "token-bucket>=0.3.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="ESMF",
    author_email="",
    url="",
    keywords=["OpenAPI", "ESMF"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['esmf_server=esmf_server.__main__:main']},
    long_description="""\
    A simple API to interact with the Edge Slice Management Function. Supports creating and removing slices across domains. Synchronises itself with other ESMFs to achieve a common goal. Please refer to the topology drawings for further information about the network structures.
    """
)

