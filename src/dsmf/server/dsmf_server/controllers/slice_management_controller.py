from typing import List, Dict
from aiohttp import web

from dsmf_server.controllers.authentication_controller import check_auth
from dsmf_server.impl.domain_state import DomainState
from dsmf_server.impl.slice_deployment import SliceDeployment
from dsmf_server.models.slice import Slice
from dsmf_server import util


async def slice_deployment_delete(request: web.Request, auth, slice_id) -> web.Response:
    """slice_deployment_delete

    Deletes a slice

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice_id: The id of the slice to be deleted.
    :type slice_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    if slice_id not in DomainState.slice_deployments.keys():
        return web.Response(status=404, reason="The slice deployment could not be found")
    try:
        SliceDeployment.remove_slice(DomainState.slice_deployments[slice_id], DomainState.slice_queue_pools[slice_id])
    except Exception as e:
        print(e)
        return web.Response(status=500, reason="The deployment to the network failed")
    finally:
        del DomainState.slice_deployments[slice_id]
        del DomainState.slice_queue_pools[slice_id]
    return web.Response(status=200, reason="The slice was successfully deleted")


async def slice_deployment_get(request: web.Request, auth) -> web.Response:
    """slice_deployment_get

    Lists all current slices

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    return web.Response(status=200, body=DomainState.slice_deployments.values())


async def slice_deployment_put(request: web.Request, auth, slice_id) -> web.Response:
    """slice_deployment_put

    Creates a new slice from a reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice_id: The slice to create from the corresponding reservation id
    :type slice_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    if slice_id not in DomainState.slice_reservations.keys():
        return web.Response(status=404, reason="The slice reservation could not be found")
    body = DomainState.slice_reservations[slice_id]
    # TODO Check tunnel existence
    DomainState.slice_deployments[slice_id] = body
    del DomainState.slice_reservations[slice_id]
    try:
        DomainState.slice_queue_pools[slice_id] = \
            SliceDeployment.deploy_slice(body,
                                         DomainState.tunnel_deployments[body.tunnel_id]
                                         )
    except Exception as e:
        print(e)
        del DomainState.slice_deployments[slice_id]
        return web.Response(status=500, reason="The deployment to the network failed")
    return web.Response(status=200, reason="The slice has been created")
