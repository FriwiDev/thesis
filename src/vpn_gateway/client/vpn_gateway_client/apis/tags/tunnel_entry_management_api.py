# coding: utf-8

"""
    VPN Gateway API

    A simple API to manage tunnel entries on a dedicated host within the edges. The VPN Gateway is used to encrypt traffic before it enters the first black network.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from vpn_gateway_client.paths.tunnel_entry.delete import TunnelEntryDelete
from vpn_gateway_client.paths.tunnel_entry.get import TunnelEntryGet
from vpn_gateway_client.paths.tunnel_entry.put import TunnelEntryPut


class TunnelEntryManagementApi(
    TunnelEntryDelete,
    TunnelEntryGet,
    TunnelEntryPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
