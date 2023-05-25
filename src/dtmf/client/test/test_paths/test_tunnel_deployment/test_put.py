# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest

from dtmf_client import configuration, api_client
from dtmf_client.paths.tunnel_deployment import put  # noqa: E501

from .. import ApiTestMixin


class TestTunnelDeployment(ApiTestMixin, unittest.TestCase):
    """
    TunnelDeployment unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
