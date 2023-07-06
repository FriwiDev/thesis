from aiohttp import web
from esmf_server.impl.domain_state import DomainState

import dsmf_client
from dsmf_client.apis.tags import authentication_api, slice_management_api, slice_reservation_api
from esmf_server.controllers.authentication_controller import check_auth
from esmf_server.models.slice import Slice


# TODO-FW Implement this not as a simple proxy - we currently trust other networks blindly which is not advisable

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
    if slice_id not in DomainState.slice_deployments.keys():
        return web.Response(status=404, reason="The slice could not be found.")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = slice_management_api.SliceManagementApi(api_client)

    query_params = {
        'auth': auth,
        'slice_id': slice_id
    }

    try:
        api_instance.slice_deployment_delete(
            query_params=query_params
        )
        del DomainState.slice_deployments[slice_id]
        return web.Response(status=200, reason="The slice was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_deployment_delete: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


async def slice_deployment_get(request: web.Request, auth) -> web.Response:
    """slice_deployment_get

    Lists all current slices

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
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
    # TODO-Thesis Validation
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = slice_management_api.SliceManagementApi(api_client)

    if slice_id not in DomainState.slice_reservations.keys():
        return web.Response(status=404, reason="The slice reservation could not be found.")

    if DomainState.slice_reservations[slice_id].tunnel_id not in DomainState.tunnel_deployments.keys():
        return web.Response(status=412, reason="The tunnel referenced by this slice has not been deployed yet")

    query_params = {
        'auth': auth,
        'slice_id': slice_id
    }

    try:
        api_instance.slice_deployment_put(
            query_params=query_params
        )
        DomainState.slice_deployments[slice_id] = DomainState.slice_reservations[slice_id]
        del DomainState.slice_reservations[slice_id]
        return web.Response(status=200, reason="The slice has been deployed.")
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceManagementApi->slice_deployment_put: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


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
    if slice_id not in DomainState.slice_reservations.keys():
        return web.Response(status=404, reason="The slice reservation could not be found.")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = slice_reservation_api.SliceReservationApi(api_client)

    query_params = {
        'auth': auth,
        'slice_id': slice_id
    }

    try:
        api_instance.slice_reservation_delete(
            query_params=query_params
        )
        del DomainState.slice_reservations[slice_id]
        return web.Response(status=200, reason="The slice reservation was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceReservationApi->slice_reservation_delete: %s\n" % e)
        return web.Response(status=e.status, reason=e.reason)


async def slice_reservation_get(request: web.Request, auth) -> web.Response:
    """slice_reservation_get

    Lists all current slice reservations

    :param auth: The authentication token issued by prior login
    :type auth: str

    """
    if not check_auth(auth):
        return web.Response(status=403, reason="Invalid authentication provided.")
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
    body = Slice.from_dict(body)
    # TODO-Thesis Validation
    if body.slice_id in DomainState.slice_reservations.keys() + DomainState.slice_deployments.keys():
        return web.Response(status=409, reason="A slice with this id is already known")
    # Forward to domain controller
    api_client, auth = get_controller_client()
    api_instance = slice_reservation_api.SliceReservationApi(api_client)

    query_params = {
        'auth': auth,
    }

    try:
        api_instance.slice_reservation_put(
            query_params=query_params,
            body=body
        )
        DomainState.slice_reservations[body.slice_id] = body
        return web.Response(status=200, reason="The slice reservation was successfully deleted.")
    except dsmf_client.ApiException as e:
        print("Exception when calling SliceReservationApi->slice_reservation_put: %s\n" % e)
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
