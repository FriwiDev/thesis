import vpn_gateway_client
from dsmf_server.models import DeviceConfiguration
from vpn_gateway_client.apis.tags import authentication_api, tunnel_entry_management_api
from vpn_gateway_client.model.tunnel_entry import TunnelEntry


class VPNDeployment(object):

    @classmethod
    def create_or_update_tunnel_entry(cls, vpn: DeviceConfiguration, tunnel_entry: TunnelEntry) -> bool:
        print(tunnel_entry)
        # Create an instance of the API class
        api_client, auth = VPNDeployment.vpn_api_client(vpn)
        api_instance = tunnel_entry_management_api.TunnelEntryManagementApi(api_client)

        query_params = {
            'auth': auth
        }
        try:
            api_instance.tunnel_entry_put(
                query_params=query_params,
                body=tunnel_entry
            )
            return True
        except vpn_gateway_client.ApiException as e:
            print("Exception when calling TunnelEntryManagementApi->tunnel_entry_put: %s\n" % e)
            return False

    @classmethod
    def delete_tunnel_entry(cls, vpn: DeviceConfiguration, tunnel_entry_id: int) -> bool:
        # Create an instance of the API class
        api_client, auth = VPNDeployment.vpn_api_client(vpn)
        api_instance = tunnel_entry_management_api.TunnelEntryManagementApi(api_client)

        query_params = {
            'auth': auth,
            'tunnel_entry_id': tunnel_entry_id
        }

        try:
            api_instance.tunnel_entry_delete(
                query_params=query_params
            )
            return True
        except vpn_gateway_client.ApiException as e:
            print("Exception when calling TunnelEntryManagementApi->tunnel_entry_delete: %s\n" % e)
            return False

    @classmethod
    def vpn_api_client(cls, vpn: DeviceConfiguration) -> (vpn_gateway_client.ApiClient, str):
        configuration = vpn_gateway_client.Configuration(
            host="http://" + vpn.ip + ":" + str(vpn.port) + "/v1"
        )

        # Enter a context with an instance of the API client
        with vpn_gateway_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = authentication_api.AuthenticationApi(api_client)

            # example, this endpoint has no required or optional parameters
            try:
                api_response = api_instance.auth_post()
                return api_client, api_response.body
            except vpn_gateway_client.ApiException as e:
                print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
                raise e
