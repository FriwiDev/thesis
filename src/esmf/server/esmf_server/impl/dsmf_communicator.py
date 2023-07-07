import dsmf_client
from dsmf_client.apis.tags import slice_reservation_api, authentication_api, slice_management_api, \
    tunnel_reservation_api, tunnel_management_api
from esmf_server.impl.domain_state import DomainState
from esmf_server.models import Tunnel, Slice


class DSMFCommunicator(object):
    @classmethod
    def reserve_tunnel(cls, body: Tunnel) -> bool:
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
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling TunnelReservationApi->tunnel_reservation_put: %s\n" % e)
            return False

    @classmethod
    def delete_reserved_tunnel(cls, body: Tunnel) -> bool:
        api_client, auth = get_controller_client()
        api_instance = tunnel_reservation_api.TunnelReservationApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_reservation_delete(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling TunnelReservationApi->tunnel_reservation_delete: %s\n" % e)
            return False

    @classmethod
    def deploy_tunnel(cls, body: Tunnel) -> bool:
        api_client, auth = get_controller_client()
        api_instance = tunnel_management_api.TunnelManagementApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_deployment_put(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling TunnelManagementApi->tunnel_deployment_put: %s\n" % e)
            return False

    @classmethod
    def delete_deployed_tunnel(cls, body: Tunnel) -> bool:
        api_client, auth = get_controller_client()
        api_instance = tunnel_management_api.TunnelManagementApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_deployment_delete(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling TunnelManagementApi->tunnel_deployment_delete: %s\n" % e)
            return False

    @classmethod
    def reserve_slice(cls, body: Slice) -> bool:
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
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling SliceReservationApi->slice_reservation_put: %s\n" % e)
            return False

    @classmethod
    def delete_reserved_slice(cls, body: Slice) -> bool:
        api_client, auth = get_controller_client()
        api_instance = slice_reservation_api.SliceReservationApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_reservation_delete(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling SliceReservationApi->slice_reservation_delete: %s\n" % e)
            return False

    @classmethod
    def deploy_slice(cls, body: Slice) -> bool:
        api_client, auth = get_controller_client()
        api_instance = slice_management_api.SliceManagementApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_deployment_put(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling SliceManagementApi->slice_deployment_put: %s\n" % e)
            return False

    @classmethod
    def delete_deployed_slice(cls, body: Slice) -> bool:
        api_client, auth = get_controller_client()
        api_instance = slice_management_api.SliceManagementApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_deployment_delete(
                query_params=query_params
            )
            return True
        except dsmf_client.ApiException as e:
            print("Exception when calling SliceManagementApi->slice_deployment_delete: %s\n" % e)
            return False


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
