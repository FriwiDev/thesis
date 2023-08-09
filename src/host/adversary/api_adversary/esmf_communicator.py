import esmf_client
from esmf_client.apis.tags import authentication_api, slice_management_api
from esmf_client.model.slice import Slice


class ESMFCommunicator(object):
    @classmethod
    def request_slice(cls, body: [Slice], esmf_ip: str, esmf_port: int = 8080) -> list[Slice] or None:
        try:
            api_client, auth = get_esmf_client(esmf_ip, esmf_port)
        except Exception:
            return None

        api_instance = slice_management_api.SliceManagementApi(api_client)

        query_params = {
            'auth': auth,
        }

        try:
            return api_instance.slice_put(
                query_params=query_params,
                body=body
            ).body
        except esmf_client.ApiException as e:
            print("Exception when calling SliceManagementApi->slice_put: %s\n" % e)
            return None
        except Exception:
            return None

    @classmethod
    def delete_slice(cls, body: [Slice], esmf_ip: str, esmf_port: int = 8080) -> bool:
        api_client, auth = get_esmf_client(esmf_ip, esmf_port)
        api_instance = slice_management_api.SliceManagementApi(api_client)

        query_params = {
            'auth': auth,
            'slice_ids': [x.slice_id for x in body]
        }

        try:
            api_instance.slice_delete(
                query_params=query_params
            )
            return True
        except esmf_client.ApiException as e:
            print("Exception when calling SliceManagementApi->slice_delete: %s\n" % e)
            return False
        except Exception:
            return False


def get_esmf_client(esmf_ip: str, esmf_port: int = 8080) -> (esmf_client.ApiClient, str):
    configuration = esmf_client.Configuration(
        host="http://" + esmf_ip + ":" + str(esmf_port) + "/v1"
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
        except Exception as e:
            raise e
