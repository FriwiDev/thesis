# coding: utf-8

"""
    DSMF

    A simple API to interact with the Domain Slice Management Function. Supports reserving, creating and removing slices and tunnels from one external domain to another external domain or host. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import dsmf_client
from dsmf_client.model.controller_configuration import ControllerConfiguration
from dsmf_client import configuration


class TestControllerConfiguration(unittest.TestCase):
    """ControllerConfiguration unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
