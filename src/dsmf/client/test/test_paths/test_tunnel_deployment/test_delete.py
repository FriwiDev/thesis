# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import dsmf_client
from dsmf_client.paths.tunnel_deployment import delete  # noqa: E501
from dsmf_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTunnelDeployment(ApiTestMixin, unittest.TestCase):
    """
    TunnelDeployment unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
