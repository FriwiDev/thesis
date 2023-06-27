from typing import List, Dict
from aiohttp import web

from esmf_server.models.tunnel import Tunnel
from esmf_server import util


async def tunnel_deployment_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_delete

    Deletes a tunnel from this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel to be deleted.
    :type tunnel_id: int

    """
    return web.Response(status=200)


async def tunnel_deployment_get(request: web.Request, auth) -> web.Response:
    """tunnel_deployment_get

    Lists all current tunnels issued by the requesting ESMF. Used for synchronization purposes.

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_deployment_put(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_put

    Creates a new tunnel on this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel to be deployed.
    :type tunnel_id: int

    """
    return web.Response(status=200)


async def tunnel_reservation_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_reservation_delete

    Deletes a tunnel reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel reservation to be deleted.
    :type tunnel_id: int

    """
    return web.Response(status=200)


async def tunnel_reservation_get(request: web.Request, auth) -> web.Response:
    """tunnel_reservation_get

    Lists all current tunnel reservations issued by the requesting ESMF. Used for synchronization purposes.

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    return web.Response(status=200)


async def tunnel_reservation_put(request: web.Request, auth, body=None) -> web.Response:
    """tunnel_reservation_put

    Creates a new tunnel reservation on this domain

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The tunnel to reserve or alter.
    :type body: dict | bytes

    """
    body = Tunnel.from_dict(body)
    return web.Response(status=200)