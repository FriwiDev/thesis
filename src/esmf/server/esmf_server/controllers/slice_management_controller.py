import json
from typing import List, Dict
from aiohttp import web

from esmf_server.controllers.authentication_controller import check_auth
from esmf_server.impl.domain_state import DomainState

from esmf_server.impl.edge_state import EdgeState
from esmf_server.models.slice import Slice

def get_owner(auth: str):
    # TODO-FW real authentication system
    return "default"

async def slice_delete(request: web.Request, auth, slice_ids) -> web.Response:
    """slice_delete

    Deletes one or multiple slices

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param slice_ids: The ids of the slices to be deleted.
    :type slice_ids: List[int]

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "ESMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    if len(slice_ids) == 0:
        return web.Response(status=417, reason="No slice ids were provided.")
    ret = EdgeState.handle_slice_revoke(slice_ids, get_owner(auth))
    if ret == 404:
        return web.Response(status=404, reason="One or multiple of the slices could not be found.")
    elif ret == 500:
        return web.Response(status=500, reason="Internal error")
    else:
        return web.Response(status=200, reason="The slices were successfully deleted.")


async def slice_get(request: web.Request, auth) -> web.Response:
    """slice_get

    Lists all current slices by this requester

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "ESMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    return web.Response(status=200, content_type="application/json", body=json.dumps([x.to_dict() for x in EdgeState.get_slices_by_owner(get_owner(auth))]))


async def slice_put(request: web.Request, auth, body=None) -> web.Response:
    """slice_put

    Creates one or multiple new slices from one host to another. Will either create all slices if feasible or none at all.

    :param auth: The authentication token issued by prior login
    :type auth: str
    :param body: The slices to reserve. The service will set the slice ids.
    :type body: list | bytes

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    if DomainState.config.type.upper() != "ESMF":
        return web.Response(status=421, reason="Slice management is not supported by this service")
    slices = [Slice.from_dict(d) for d in body]
    if len(slices) == 0:
        return web.Response(status=417, reason="No slices were requested")
    # TODO-Thesis validation
    ret = EdgeState.handle_slice_request(slices, get_owner(auth))
    if ret == 404:
        return web.Response(status=404, reason="The input or output of one or multiple of the slices could not be found")
    elif ret == 500:
        return web.Response(status=500, reason="Internal error")
    elif ret == 507:
        return web.Response(status=507, reason="Insufficient resources by participating domain or requester")
    else:
        return web.Response(status=200, content_type="application/json", body=json.dumps([x.to_dict() for x in ret]))
