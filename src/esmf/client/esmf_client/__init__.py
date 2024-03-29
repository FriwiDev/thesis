# coding: utf-8

# flake8: noqa

"""
    ESMF

    A simple API to interact with the Edge Slice Management Function. Supports creating and removing slices across domains. Synchronises itself with other ESMFs to achieve a common goal. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import ApiClient
from esmf_client.api_client import ApiClient

# import Configuration
from esmf_client.configuration import Configuration

# import exceptions
from esmf_client.exceptions import OpenApiException
from esmf_client.exceptions import ApiAttributeError
from esmf_client.exceptions import ApiTypeError
from esmf_client.exceptions import ApiValueError
from esmf_client.exceptions import ApiKeyError
from esmf_client.exceptions import ApiException
