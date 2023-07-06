from typing import List, Dict
from aiohttp import web

from dsmf_server.controllers.authentication_controller import check_auth
from dsmf_server.models.domain_configuration import DomainConfiguration
from dsmf_server import util


async def configuration_get(request: web.Request, auth) -> web.Response:
    """configuration_get

    Fetch the current configuration of this service

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200)


async def configuration_put(request: web.Request, auth, body=None) -> web.Response:
    """configuration_put

    Installs a new configuration for this service

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The configuration to install. Will check for issues.
    :type body: dict | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    body = DomainConfiguration.from_dict(body)
    return web.Response(status=200)
