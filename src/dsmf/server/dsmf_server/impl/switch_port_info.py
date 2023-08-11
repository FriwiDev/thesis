import pprint
from typing import List

import pprint
from typing import List

import controller_client
from controller_client.apis.tags import port_management_api
from controller_client.model.switch_port_description import SwitchPortDescription
from dsmf_server.impl.domain_state import DomainState
from dsmf_server.models import DeviceConfiguration


class SwitchPortInfo(object):

    @classmethod
    def get_portdesc(cls, switch: DeviceConfiguration) -> List[SwitchPortDescription] or None:
        # Create an instance of the API class
        api_client = cls.controller_api_client(switch)
        api_instance = port_management_api.PortManagementApi(api_client)

        # Build params
        params = {
            'dpid': switch.dpid
        }

        print("Switch portdesc get " + pprint.pformat(params))

        # Perform request
        try:
            return api_instance.portdesc_dpid_get(
                path_params=params
            ).body[str(switch.dpid)]
        except controller_client.ApiException as e:
            print("Exception when calling PortManagementApi->portdesc_dpid_get: %s\n" % e)
            return None

    @classmethod
    def controller_api_client(cls, switch: DeviceConfiguration) -> controller_client.ApiClient:
        # TODO-FW: Support for multiple controllers could be added here, depending on the switch
        configuration = controller_client.Configuration(
            host="http://" + DomainState.config.controllers[0].ip + ":" + str(
                DomainState.config.controllers[0].port) + "/stats"
        )

        # Enter a context with an instance of the API client
        with controller_client.ApiClient(configuration) as api_client:
            return api_client
