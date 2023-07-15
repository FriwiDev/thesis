from typing import List, Dict
from aiohttp import web

from dsmf_server.controllers.authentication_controller import check_auth
from dsmf_server.impl.domain_state import DomainState
from dsmf_server.models.tunnel import Tunnel
from dsmf_server import util


async def tunnel_reservation_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_reservation_delete

    Deletes a tunnel reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel reservation to be deleted.
    :type tunnel_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if tunnel_id not in DomainState.tunnel_reservations.keys():
        return web.Response(status=404, reason="The tunnel reservation could not be found")
    del DomainState.tunnel_reservations[tunnel_id]
    return web.Response(status=200, reason="The tunnel reservation was successfully deleted")


async def tunnel_reservation_get(request: web.Request, auth) -> web.Response:
    """tunnel_reservation_get

    Lists all current tunnel reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200, body=DomainState.tunnel_reservations.values())


async def tunnel_reservation_put(request: web.Request, auth, body=None) -> web.Response:
    """tunnel_reservation_put

    Creates a new tunnel reservation or stages changes to an existing deployed tunnel, as long as source and target of the tunnel match.

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The tunnel to reserve. Will check for issues.
    :type body: dict | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    body = Tunnel.from_dict(body)
    # TODO-Thesis Validation
    if body.tunnel_id in DomainState.tunnel_deployments.keys():
        old_tunnel = DomainState.tunnel_deployments[body.tunnel_id]
        if old_tunnel.fr != body.fr or old_tunnel.to != body.to:
            return web.Response(status=409, reason="A tunnel with this id is already known "
                                                   "and does not match current source and target")
        body.private_key = old_tunnel.private_key
        body.public_key = old_tunnel.public_key
    # TODO-Thesis Resource validation (do we have enough resources?)
    DomainState.tunnel_reservations[body.tunnel_id] = body
    return web.Response(status=200, reason="The tunnel has been reserved")
