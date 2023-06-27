# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import controller_client
from controller_client.paths.desc_dpid import get  # noqa: E501
from controller_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDescDpid(ApiTestMixin, unittest.TestCase):
    """
    DescDpid unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
