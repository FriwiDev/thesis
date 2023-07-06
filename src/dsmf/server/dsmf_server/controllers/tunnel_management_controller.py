from typing import List, Dict
from aiohttp import web

from dsmf_server.controllers.authentication_controller import check_auth
from dsmf_server.impl.domain_state import DomainState
from dsmf_server.impl.tunnel_deployment import TunnelDeployment
from dsmf_server.models.tunnel import Tunnel
from dsmf_server import util


async def tunnel_deployment_delete(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_delete

    Deletes a tunnel

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The id of the tunnel to be deleted.
    :type tunnel_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if tunnel_id not in DomainState.tunnel_deployments.keys():
        return web.Response(status=404, reason="The tunnel deployment could not be found")
    for sl in DomainState.slice_deployments.values():
        if sl.tunnel_id == tunnel_id:
            return web.Response(status=412, reason="The tunnel is still being referenced by a deployed slice")
    try:
        TunnelDeployment.remove_tunnel(DomainState.tunnel_deployments[tunnel_id],
                                       DomainState.tunnel_queue_pools[tunnel_id])
    except Exception as e:
        print(e)
        return web.Response(status=500, reason="The deployment to the network failed")
    finally:
        del DomainState.tunnel_deployments[tunnel_id]
        del DomainState.tunnel_queue_pools[tunnel_id]
    return web.Response(status=200, reason="The tunnel was successfully deleted")


async def tunnel_deployment_get(request: web.Request, auth) -> web.Response:
    """tunnel_deployment_get

    Lists all current tunnels

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200, body=DomainState.tunnel_deployments.values())


async def tunnel_deployment_put(request: web.Request, auth, tunnel_id) -> web.Response:
    """tunnel_deployment_put

    Creates a new tunnel or modifies a tunnel from a reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param tunnel_id: The tunnel to create from the corresponding reservation id
    :type tunnel_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if tunnel_id not in DomainState.tunnel_reservations.keys():
        return web.Response(status=404, reason="The tunnel reservation could not be found")
    body = DomainState.tunnel_reservations[tunnel_id]
    DomainState.tunnel_deployments[tunnel_id] = body
    del DomainState.tunnel_reservations[tunnel_id]
    try:
        DomainState.tunnel_queue_pools[tunnel_id] = \
            TunnelDeployment.deploy_tunnel(body,
                                           DomainState.tunnel_queue_pools[
                                               tunnel_id] if tunnel_id in DomainState.tunnel_queue_pools else {}
                                           )
    except Exception as e:
        print(e)
        del DomainState.tunnel_deployments[tunnel_id]
        return web.Response(status=500, reason="The deployment to the network failed")
    return web.Response(status=200, reason="The tunnel has been created")
