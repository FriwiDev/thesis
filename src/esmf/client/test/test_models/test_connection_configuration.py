# coding: utf-8

"""
    ESMF

    A simple API to interact with the Edge Slice Management Function. Supports creating and removing slices across domains. Synchronises itself with other ESMFs to achieve a common goal. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import esmf_client
from esmf_client.model.connection_configuration import ConnectionConfiguration
from esmf_client import configuration


class TestConnectionConfiguration(unittest.TestCase):
    """ConnectionConfiguration unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
