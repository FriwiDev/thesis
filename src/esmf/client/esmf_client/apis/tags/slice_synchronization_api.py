# coding: utf-8

"""
    ESMF

    A simple API to interact with the Edge Slice Management Function. Supports creating and removing slices across domains. Synchronises itself with other ESMFs to achieve a common goal. Please refer to the topology drawings for further information about the network structures.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from esmf_client.paths.slice_deployment.delete import SliceDeploymentDelete
from esmf_client.paths.slice_deployment.get import SliceDeploymentGet
from esmf_client.paths.slice_deployment.put import SliceDeploymentPut
from esmf_client.paths.slice_reservation.delete import SliceReservationDelete
from esmf_client.paths.slice_reservation.get import SliceReservationGet
from esmf_client.paths.slice_reservation.put import SliceReservationPut


class SliceSynchronizationApi(
    SliceDeploymentDelete,
    SliceDeploymentGet,
    SliceDeploymentPut,
    SliceReservationDelete,
    SliceReservationGet,
    SliceReservationPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
