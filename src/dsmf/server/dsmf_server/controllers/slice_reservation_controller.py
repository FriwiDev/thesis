from typing import List, Dict
from aiohttp import web

from dsmf_server.controllers.authentication_controller import check_auth
from dsmf_server.impl.domain_state import DomainState
from dsmf_server.models.slice import Slice
from dsmf_server import util


async def slice_reservation_delete(request: web.Request, auth, slice_id) -> web.Response:
    """slice_reservation_delete

    Deletes a slice reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice_id: The id of the slice reservation to be deleted.
    :type slice_id: int

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    if slice_id not in DomainState.slice_reservations.keys():
        return web.Response(status=404, reason="The slice reservation could not be found")
    del DomainState.slice_reservations[slice_id]
    return web.Response(status=200, reason="The slice reservation was successfully deleted")


async def slice_reservation_get(request: web.Request, auth) -> web.Response:
    """slice_reservation_get

    Lists all current slice reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    return web.Response(status=200, body=DomainState.slice_reservations.values())


async def slice_reservation_put(request: web.Request, auth, body=None) -> web.Response:
    """slice_reservation_put

    Creates a new slice reservation

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The slice to reserve. Will check for issues.
    :type body: dict | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "DSMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    body = Slice.from_dict(body)
    # TODO-Thesis Validation
    if body.slice_id in DomainState.slice_reservations.keys() or body.slice_id in DomainState.slice_deployments.keys():
        return web.Response(status=409, reason="A slice with this id is already known")
    # TODO-Thesis Resource validation (do we have enough resources?)
    DomainState.slice_reservations[body.slice_id] = body
    return web.Response(status=200, reason="The slice has been reserved")
