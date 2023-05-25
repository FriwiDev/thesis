# coding: utf-8

"""
    ESMF

    A simple API to interact with the Edge Slice Management Function. Supports creating and removing slices across domains. Synchronises itself with other ESMFs to achieve a common goal. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from esmf_client.paths.tunnel_deployment.delete import TunnelDeploymentDelete
from esmf_client.paths.tunnel_deployment.get import TunnelDeploymentGet
from esmf_client.paths.tunnel_deployment.put import TunnelDeploymentPut
from esmf_client.paths.tunnel_reservation.delete import TunnelReservationDelete
from esmf_client.paths.tunnel_reservation.get import TunnelReservationGet
from esmf_client.paths.tunnel_reservation.put import TunnelReservationPut


class TunnelSynchronizationApi(
    TunnelDeploymentDelete,
    TunnelDeploymentGet,
    TunnelDeploymentPut,
    TunnelReservationDelete,
    TunnelReservationGet,
    TunnelReservationPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
