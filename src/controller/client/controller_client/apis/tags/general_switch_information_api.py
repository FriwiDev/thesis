# coding: utf-8

"""
    Controller

    The API used by the DSMF/DTMF to contact the controller. This API is a subset of the API provided by the ryu controller and modelled strictly according to their specification. Currently we only support OpenFlow 1.2 or higher. Please refer to the specification here: <a href=\"https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html\">https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html</a>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from controller_client.paths.desc_dpid.get import DescDpidGet
from controller_client.paths.switches.get import SwitchesGet


class GeneralSwitchInformationApi(
    DescDpidGet,
    SwitchesGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass