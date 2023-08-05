# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "host-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "token-bucket == 0.3.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Host",
    author="FriwiDev",
    author_email="friwidev@gmail.com",
    url="",
    keywords=["Edgeslicing", "Host"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    A slicing host to be used in our distributed edgeslicing environment.  # noqa: E501
    """
)
