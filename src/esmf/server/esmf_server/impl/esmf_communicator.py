import esmf_client
from esmf_client.apis.tags import authentication_api, slice_synchronization_api, \
    tunnel_synchronization_api
from esmf_server.impl.domain_state import DomainState
from esmf_server.models import Tunnel, Slice


class ESMFCommunicator(object):
    @classmethod
    def reserve_tunnel(cls, body: Tunnel, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
        }

        try:
            api_instance.tunnel_reservation_put(
                query_params=query_params,
                body=body.to_dict()
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_put: %s\n" % e)
            return False

    @classmethod
    def delete_reserved_tunnel(cls, body: Tunnel, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_reservation_delete(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling TunnelSynchronizationApi->tunnel_reservation_delete: %s\n" % e)
            return False

    @classmethod
    def deploy_tunnel(cls, body: Tunnel, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_deployment_put(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling TunnelSynchronizationApi->tunnel_deployment_put: %s\n" % e)
            return False

    @classmethod
    def delete_deployed_tunnel(cls, body: Tunnel, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = tunnel_synchronization_api.TunnelSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_id': body.tunnel_id
        }

        try:
            api_instance.tunnel_deployment_delete(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling TunnelSynchronizationApi->tunnel_deployment_delete: %s\n" % e)
            return False

    @classmethod
    def reserve_slice(cls, body: Slice, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = slice_synchronization_api.SliceSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
        }

        try:
            api_instance.slice_reservation_put(
                query_params=query_params,
                body=body.to_dict()
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling SliceSynchronizationApi->slice_reservation_put: %s\n" % e)
            return False

    @classmethod
    def delete_reserved_slice(cls, body: Slice, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = slice_synchronization_api.SliceSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_reservation_delete(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling SliceSynchronizationApi->slice_reservation_delete: %s\n" % e)
            return False

    @classmethod
    def deploy_slice(cls, body: Slice, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = slice_synchronization_api.SliceSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_deployment_put(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling SliceSynchronizationApi->slice_deployment_put: %s\n" % e)
            return False

    @classmethod
    def delete_deployed_slice(cls, body: Slice, net: str) -> bool:
        api_client, auth = get_coordinator_client(net)
        # Support unmanaged networks
        if not api_client:
            return True
        api_instance = slice_synchronization_api.SliceSynchronizationApi(api_client)

        query_params = {
            'auth': auth,
            'slice_id': body.slice_id
        }

        try:
            api_instance.slice_deployment_delete(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling SliceSynchronizationApi->slice_deployment_delete: %s\n" % e)
            return False


def get_coordinator_client(net: str) -> (esmf_client.ApiClient or None, str):
    coord = DomainState.get_coordinator_by_network(net)
    if not coord:
        return (None, "")
    configuration = esmf_client.Configuration(
        host="http://" + coord.ip + ":" + str(coord.port) + "/v1"
    )

    # Enter a context with an instance of the API client
    with esmf_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = authentication_api.AuthenticationApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            api_response = api_instance.auth_post()
            return api_client, api_response.body
        except esmf_client.ApiException as e:
            print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
            raise e
