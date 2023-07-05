import ipaddress

import controller_client
import switch_client
from controller_client.apis.tags import flow_management_api
from dsmf_server.impl.domain_state import DeviceType, DomainState
from dsmf_server.impl.domain_util import DomainUtil
from dsmf_server.models import DeviceConfiguration
from switch_client.apis.tags import queue_management_api, authentication_api, traffic_shaping_api
from switch_server.models import Queue


class SwitchDeployment(object):
    @classmethod
    def setup_switch(cls, switch: DeviceConfiguration, switch_type: DeviceType,  # Switch and type to set up
                     prev_name: str, next_name: str,  # Previous and next hop
                     slice_id: int, protocol: str,  # Or tunnel_id, "UDP"
                     src_ip: ipaddress.ip_address, src_port: int,
                     dst_ip: ipaddress.ip_address, dst_port: int,
                     queue: Queue,  # The queue to deploy
                     reverse_queue: Queue = None  # An already cached reverse queue
                     ) -> (Queue, Queue or None):  # Returns the queue and the potential reverse queue
        # One of the ports will be 0, indicating our direction (we only know the port on one side)
        # TODO: Traffic shaping
        if switch_type == DeviceType.SRC_ENTRY or switch_type == DeviceType.SRC_TP \
                or switch_type == DeviceType.SRC_EXIT or switch_type == DeviceType.SRC_ALL:
            intf_out = DomainUtil.port_name_of_switch(switch, next_name)
            # Add our slice queue
            queue.port = intf_out
            queue.queue_id = SwitchDeployment.create_queue(switch, queue)
            if queue.queue_id == -1:
                raise Exception("Error while installing queue")
            port_out = DomainUtil.port_index_of_switch(switch, next_name)
            # Remove old flows
            if not SwitchDeployment.delete_flows(switch, cookie=slice_id):
                raise Exception("Error while removing old flows")
            if switch_type == DeviceType.SRC_ENTRY or switch_type == DeviceType.SRC_ALL:
                port_in = DomainUtil.port_index_of_switch(switch, prev_name)
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id, protocol=protocol,
                                                    in_port=port_in,
                                                    src_ip=src_ip, src_port=src_port, dst_ip=dst_ip, dst_port=dst_port,
                                                    mpls=slice_id, push_mpls=True,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
            elif switch_type == DeviceType.SRC_TP or switch_type == DeviceType.SRC_EXIT:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
            return queue, None
        elif switch_type == DeviceType.BN_ENTRY or switch_type == DeviceType.BN_TP \
                or switch_type == DeviceType.BN_EXIT or switch_type == DeviceType.BN_ALL:
            intf_out = DomainUtil.port_name_of_switch(switch, next_name)
            intf_in = DomainUtil.port_name_of_switch(switch, prev_name)
            # Add our tunnel queue
            queue.port = intf_out
            queue.queue_id = SwitchDeployment.create_queue(switch, queue)
            if queue.queue_id == -1:
                raise Exception("Error while installing queue")
            if not reverse_queue:
                reverse_queue = Queue(0, 10000, 10000, 10000, 1, intf_in)
                reverse_queue.queue_id = SwitchDeployment.create_queue(switch, reverse_queue)
                if reverse_queue.queue_id == -1:
                    raise Exception("Error while installing queue")
            port_out = DomainUtil.port_index_of_switch(switch, next_name)
            port_in = DomainUtil.port_index_of_switch(switch, prev_name)
            # Remove old flows
            if not SwitchDeployment.delete_flows(switch, cookie=slice_id):
                raise Exception("Error while removing old flows")
            if switch_type == DeviceType.BN_ENTRY:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id, protocol=protocol,
                                                    in_port=port_in,
                                                    src_ip=src_ip, dst_ip=dst_ip, dst_port=dst_port,
                                                    mpls=slice_id * 2, push_mpls=True,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
                # And our reverse flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id * 2 + 1,
                                                    mpls=slice_id * 2 + 1, pop_mpls=True,
                                                    queue_id=reverse_queue.queue_id, out_port=port_in):
                    raise Exception("Error while installing flow")
            elif switch_type == DeviceType.BN_TP:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id * 2,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
                # And our reverse flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id * 2 + 1,
                                                    queue_id=reverse_queue.queue_id, out_port=port_in):
                    raise Exception("Error while installing flow")
            elif switch_type == DeviceType.BN_EXIT:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id * 2,
                                                    mpls=slice_id * 2, pop_mpls=True,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
                # And our reverse flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id, protocol=protocol,
                                                    in_port=port_out,
                                                    src_ip=dst_ip, dst_ip=src_ip, dst_port=src_port,
                                                    # TODO Verify if this is correct - might need another 2 flows for other combinations
                                                    mpls=slice_id * 2 + 1, push_mpls=True,
                                                    queue_id=reverse_queue.queue_id, out_port=port_in):
                    raise Exception("Error while installing flow")
            elif switch_type == DeviceType.BN_ALL:
                port_in = DomainUtil.port_index_of_switch(switch, prev_name)
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id, protocol=protocol,
                                                    in_port=port_in,
                                                    src_ip=src_ip, dst_ip=dst_ip, dst_port=dst_port,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
                # And our reverse flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id, protocol=protocol,
                                                    in_port=port_out,
                                                    src_ip=dst_ip, dst_ip=src_ip, dst_port=src_port,
                                                    # TODO Verify if this is correct - might need another 2 flows for other combinations
                                                    queue_id=reverse_queue.queue_id, out_port=port_in):
                    raise Exception("Error while installing flow")
            return queue, reverse_queue
        if switch_type == DeviceType.DST_ENTRY or switch_type == DeviceType.DST_TP \
                or switch_type == DeviceType.DST_EXIT or switch_type == DeviceType.DST_ALL:
            intf_out = DomainUtil.port_name_of_switch(switch, next_name)
            # Add our slice queue
            queue.port = intf_out
            queue.queue_id = SwitchDeployment.create_queue(switch, queue)
            if queue.queue_id == -1:
                raise Exception("Error while installing queue")
            port_out = DomainUtil.port_index_of_switch(switch, next_name)
            # Remove old flows
            if not SwitchDeployment.delete_flows(switch, cookie=slice_id):
                raise Exception("Error while removing old flows")
            if switch_type == DeviceType.DST_ENTRY or switch_type == DeviceType.DST_TP:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
            elif switch_type == DeviceType.DST_EXIT or switch_type == DeviceType.DST_ALL:
                # Add our flow
                if not SwitchDeployment.create_flow(switch, cookie=slice_id,
                                                    mpls_match=slice_id,
                                                    mpls=slice_id, pop_mpls=True,
                                                    queue_id=queue.queue_id, out_port=port_out):
                    raise Exception("Error while installing flow")
            return queue, None

    @classmethod
    def uninstall_switch(cls, switch: DeviceConfiguration, slice_id: int, queues: [Queue], queues_reversed: [Queue]):
        if not SwitchDeployment.delete_flows(switch, cookie=slice_id):
            raise Exception("Error while removing flows")
        for queue in queues:
            if not SwitchDeployment.delete_queue(switch, queue=queue):
                raise Exception("Error while removing queue")
        for queue_reversed in queues_reversed:
            if not SwitchDeployment.delete_queue(switch, queue=queue_reversed):
                raise Exception("Error while removing queue")

    @classmethod
    def create_flow(cls, switch: DeviceConfiguration,
                    out_port: int,
                    protocol: str = None,
                    cookie: int = 0,
                    mpls_match: int = 0,
                    src_ip: ipaddress.ip_address = None,
                    dst_ip: ipaddress.ip_address = None,
                    src_port: int = 0,
                    dst_port: int = 0,
                    in_port: int = -1,
                    mpls: int = 0, push_mpls: bool = False, pop_mpls: bool = False,
                    queue_id: int = 0) -> bool:
        # Create an instance of the API class
        api_client, auth = SwitchDeployment.controller_api_client(switch)
        api_instance = flow_management_api.FlowManagementApi(api_client)

        # Build matches
        m = {}

        if mpls_match == 0:
            m['ipv4_src'] = str(src_ip)
            m['ipv4_dst'] = str(dst_ip)
            if src_port != 0:
                m[protocol.lower() + "_src"] = src_port
            if dst_port != 0:
                m[protocol.lower() + "_dst"] = dst_port
            if in_port != -1:
                m['in_port'] = in_port
        else:
            m['mpls_label'] = mpls_match

        # Build actions
        actions = []
        if pop_mpls:
            actions.append({"type": "POP_MPLS", "ethertype": mpls})
        if push_mpls:
            actions.append({"type": "PUSH_MPLS", "ethertype": mpls})
        if queue_id != 0:
            actions.append({"type": "SET_QUEUE", "queue_id": queue_id})
        actions.append({"type": "OUTPUT", "port": out_port})

        # Build body
        body = {
            'dpid': switch.dpid,
            'table_id': 0,
            'cookie': cookie,
            'match': m,
            'instructions': [
                {
                    "type": "APPLY_ACTIONS",
                    "actions": actions
                }
            ]
        }

        # Perform request
        try:
            api_instance.flowentry_add_post(
                body=body
            )
            return True
        except switch_client.ApiException as e:
            print("Exception when calling FlowManagementApi->flowentry_add_post: %s\n" % e)
            return False

    @classmethod
    def delete_flows(cls, switch: DeviceConfiguration,
                     cookie: int) -> bool:
        # Create an instance of the API class
        api_client, auth = SwitchDeployment.controller_api_client(switch)
        api_instance = flow_management_api.FlowManagementApi(api_client)

        # Build body
        body = {
            'dpid': switch.dpid,
            'table_id': 0,
            'cookie': cookie
        }

        # Perform request
        try:
            api_instance.flowentry_delete_post(
                body=body
            )
            return True
        except switch_client.ApiException as e:
            print("Exception when calling FlowManagementApi->flowentry_delete_post: %s\n" % e)
            return False

    @classmethod
    def create_queue(cls, switch: DeviceConfiguration, queue: Queue) -> int:
        # Create an instance of the API class
        api_client, auth = SwitchDeployment.switch_api_client(switch)
        api_instance = queue_management_api.QueueManagementApi(api_client)

        query_params = {
            'auth': auth
        }
        try:
            api_response = api_instance.queue_put(
                query_params=query_params,
                body=queue
            )
            return api_response.body.queue_id
        except switch_client.ApiException as e:
            print("Exception when calling QueueManagementApi->queue_put: %s\n" % e)
            return -1

    @classmethod
    def delete_queue(cls, switch: DeviceConfiguration, queue: Queue) -> bool:
        # Create an instance of the API class
        api_client, auth = SwitchDeployment.switch_api_client(switch)
        api_instance = queue_management_api.QueueManagementApi(api_client)

        query_params = {
            'auth': auth,
            'queue_id': queue.queue_id,
            'port': queue.port
        }
        try:
            api_instance.queue_delete(
                query_params=query_params
            )
            return True
        except switch_client.ApiException as e:
            print("Exception when calling QueueManagementApi->queue_delete: %s\n" % e)
            return False

    @classmethod
    def traffic_policy(cls, switch: DeviceConfiguration, port: str, ingress_policing_rate: int = 0,
                       ingress_policing_burst: int = 0) -> bool:
        """
        Use 0 as rate and/or burst to remove limitation
        """

        # Create an instance of the API class
        api_client, auth = SwitchDeployment.switch_api_client(switch)
        api_instance = traffic_shaping_api.TrafficShapingApi(api_client)

        query_params = {
            'auth': auth,
            'port': port,
            'ingress_policing_rate': ingress_policing_rate,
            'ingress_policing_burst': ingress_policing_burst
        }
        try:
            api_instance.policy_put(
                query_params=query_params
            )
            return True
        except switch_client.ApiException as e:
            print("Exception when calling TrafficShapingApi->policy_put: %s\n" % e)
            return False

    @classmethod
    def controller_api_client(cls, switch: DeviceConfiguration) -> controller_client.ApiClient:
        # TODO: Support for multiple controllers could be added here, depending on the switch
        configuration = controller_client.Configuration(
            host="http://" + DomainState.config.controllers[0].ip + ":" + str(
                DomainState.config.controllers[0].port) + "/stats"
        )

        # Enter a context with an instance of the API client
        with controller_client.ApiClient(configuration) as api_client:
            return api_client

    @classmethod
    def switch_api_client(cls, switch: DeviceConfiguration) -> (switch_client.ApiClient, str):
        configuration = switch_client.Configuration(
            host="http://" + switch.ip + ":" + str(switch.port) + "/v1"
        )

        # Enter a context with an instance of the API client
        with switch_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = authentication_api.AuthenticationApi(api_client)

            # example, this endpoint has no required or optional parameters
            try:
                api_response = api_instance.auth_post()
                return api_client, api_response.body
            except switch_client.ApiException as e:
                print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
                raise e
