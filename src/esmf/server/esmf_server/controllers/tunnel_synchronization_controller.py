from aiohttp import web
from esmf_server.impl.domain_state import DomainState

import dsmf_client
from dsmf_client.apis.tags import authentication_api, tunnel_reservation_api, tunnel_management_api
from esmf_server.controllers.authentication_controller import check_auth
from esmf_server.models.tunnel import Tunnel


# TODO-FW Implement this not as a simple proxy - we currently trust other networks blindly which is not advisable

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
        return web.Response(status=404, reason="The tunnel could not be found.")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = tunnel_management_api.TunnelManagementApi(api_client)

    query_params = {
        'auth': auth,
        'tunnel_id': tunnel_id
    }

    try:
        api_instance.tunnel_deployment_delete(
            query_params=query_params
        )
        del DomainState.tunnel_deployments[tunnel_id]
        return web.Response(status=200, reason="The tunnel was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling TunnelManagementApi->tunnel_deployment_delete: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


async def tunnel_deployment_get(request: web.Request, auth) -> web.Response:
    """tunnel_deployment_get

    Lists all current tunnels

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200, content_type="application/json", body=DomainState.tunnel_deployments.values())


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
    # TODO-Thesis Validation
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = tunnel_management_api.TunnelManagementApi(api_client)

    if tunnel_id not in DomainState.tunnel_reservations.keys():
        return web.Response(status=404, reason="The tunnel reservation could not be found.")

    query_params = {
        'auth': auth,
        'tunnel_id': tunnel_id
    }

    try:
        api_instance.tunnel_deployment_put(
            query_params=query_params
        )
        DomainState.tunnel_deployments[tunnel_id] = DomainState.tunnel_reservations[tunnel_id]
        del DomainState.tunnel_reservations[tunnel_id]
        return web.Response(status=200, reason="The tunnel has been deployed.")
    except dsmf_client.ApiException as e:
        print("Exception when calling TunnelManagementApi->tunnel_deployment_put: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


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
        return web.Response(status=404, reason="The tunnel reservation could not be found.")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = tunnel_reservation_api.TunnelReservationApi(api_client)

    query_params = {
        'auth': auth,
        'tunnel_id': tunnel_id
    }

    try:
        api_instance.tunnel_reservation_delete(
            query_params=query_params
        )
        del DomainState.tunnel_reservations[tunnel_id]
        return web.Response(status=200, reason="The tunnel reservation was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling TunnelReservationApi->tunnel_reservation_delete: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


async def tunnel_reservation_get(request: web.Request, auth) -> web.Response:
    """tunnel_reservation_get

    Lists all current tunnel reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
    return web.Response(status=200, content_type="application/json", body=DomainState.tunnel_reservations.values())


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
        if old_tunnel.fr != body.fr or old_tunnel.to != body.to \
                or old_tunnel.private_key != body.private_key or old_tunnel.public_key != body.public_key:
            return web.Response(status=409, reason="A tunnel with this id is already known "
                                                   "and does not match current source and target")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = tunnel_reservation_api.TunnelReservationApi(api_client)

    query_params = {
        'auth': auth,
    }

    try:
        api_instance.tunnel_reservation_put(
            query_params=query_params,
            body=body
        )
        DomainState.tunnel_reservations[body.tunnel_id] = body
        return web.Response(status=200, reason="The tunnel reservation was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling TunnelReservationApi->tunnel_reservation_put: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


def get_controller_client() -> (dsmf_client.ApiClient, str):
    configuration = dsmf_client.Configuration(
        host="http://" + DomainState.domain_controller.ip + ":" + str(DomainState.domain_controller.port) + "/v1"
    )

    # Enter a context with an instance of the API client
    with dsmf_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = authentication_api.AuthenticationApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            api_response = api_instance.auth_post()
            return api_client, api_response.body
        except dsmf_client.ApiException as e:
            print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
            raise e
