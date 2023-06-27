# coding: utf-8

# flake8: noqa

"""
    Switch QoS API

    A simple API to manage QoS queues and traffic shaping on arbitrary OpenFlow switches. Does not support listing queues (GET) because this is already part of OpenFlow.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import ApiClient
from switch_client.api_client import ApiClient

# import Configuration
from switch_client.configuration import Configuration

# import exceptions
from switch_client.exceptions import OpenApiException
from switch_client.exceptions import ApiAttributeError
from switch_client.exceptions import ApiTypeError
from switch_client.exceptions import ApiValueError
from switch_client.exceptions import ApiKeyError
from switch_client.exceptions import ApiException