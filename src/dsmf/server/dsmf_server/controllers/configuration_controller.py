from typing import List, Dict
from aiohttp import web

from dsmf_server.models.service_configuration import ServiceConfiguration
from dsmf_server import util


async def configuration_get(request: web.Request, auth) -> web.Response:
    """configuration_get

    Fetch the current configuration of this service

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def configuration_put(request: web.Request, auth, body=None) -> web.Response:
    """configuration_put

    Installs a new configuration for this service

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The configuration to install. Will check for issues.
    :type body: dict | bytes

    """
    body = ServiceConfiguration.from_dict(body)
    return web.Response(status=200)
