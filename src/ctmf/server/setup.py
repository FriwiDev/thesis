# coding: utf-8

from setuptools import setup, find_packages

NAME = "ctmf_server"
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
    description="CTMF",
    author_email="",
    url="",
    keywords=["OpenAPI", "CTMF"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['ctmf_server=ctmf_server.__main__:main']},
    long_description="""\
    A simple API to interact with the Core Tunnel Management Function. Supports creating and removing tunnels on this domains. Is advised to allocate resources by external ESMFs. The CTMF is a subset of the ESMF. Please refer to the topology drawings for further information about the network structures.
    """
)
