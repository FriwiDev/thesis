# coding: utf-8

"""
    Controller

    The API used by the DSMF/DTMF to contact the controller. This API is a subset of the API provided by the ryu controller and modelled strictly according to their specification. Currently we only support OpenFlow 1.2 or higher. Please refer to the specification here: <a href=\"https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html\">https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html</a>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from controller_client.paths.flow_dpid.get import FlowDpidGet
from controller_client.paths.flow_dpid.post import FlowDpidPost
from controller_client.paths.flowentry_add.post import FlowentryAddPost
from controller_client.paths.flowentry_clear_dpid.delete import FlowentryClearDpidDelete
from controller_client.paths.flowentry_delete.post import FlowentryDeletePost
from controller_client.paths.flowentry_delete_strict.post import FlowentryDeleteStrictPost


class FlowManagementApi(
    FlowDpidGet,
    FlowDpidPost,
    FlowentryAddPost,
    FlowentryClearDpidDelete,
    FlowentryDeletePost,
    FlowentryDeleteStrictPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
