# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "vpn_gateway_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==3.0.3",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.1",
    "flask==2.3.3",
    "aiohttp_cors>=0.7.0",
    "werkzeug>=2.2.3"
]

setup(
    name=NAME,
    version=VERSION,
    description="VPN Gateway API",
    author_email="",
    url="",
    keywords=["OpenAPI", "VPN Gateway API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['vpn_gateway_server=vpn_gateway_server.__main__:main']},
    long_description="""\
    A simple API to manage tunnel entries on a dedicated host within the edges. The VPN Gateway is used to encrypt traffic before it enters the first black network.
    """
)

