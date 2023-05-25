# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest

from dsmf_client import configuration, api_client
from dsmf_client.paths.slice_reservation import get  # noqa: E501

from .. import ApiTestMixin


class TestSliceReservation(ApiTestMixin, unittest.TestCase):
    """
    SliceReservation unit test stubs
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
