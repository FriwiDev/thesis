# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest

from ctmf_client import configuration, api_client
from ctmf_client.paths.tunnel_reservation import delete  # noqa: E501

from .. import ApiTestMixin


class TestTunnelReservation(ApiTestMixin, unittest.TestCase):
    """
    TunnelReservation unit test stubs
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
