from typing import Dict

from dsmf_server.impl.domain_state import DomainState
from dsmf_server.impl.domain_util import DomainUtil
from dsmf_server.impl.switch_deployment import SwitchDeployment
from dsmf_server.impl.tunnel_deployment import TunnelDeployment
from dsmf_server.models import Tunnel, Slice
from switch_client.model.queue import Queue


class SliceDeployment(object):
    @classmethod
    def deploy_slice(cls, slice_value: Slice, tunnel: Tunnel) -> \
            Dict[str, Queue]:
        print("Get from device")
        from_device = DomainState.get_device(slice_value.fr.name)
        print("Get to device")
        to_device = DomainState.get_device(slice_value.to.name)
        print("Search for our side")
        begin = None
        if from_device and from_device.network == DomainState.config.network:
            begin = True
        elif to_device and to_device.network == DomainState.config.network:
            begin = False
        print("Begin?")
        if begin is None:
            raise Exception("Could not find source and target of slice")
        # Build a local route
        print("Building route...")
        devices, device_types = DomainUtil.route_slice(slice_value.fr.name if begin else slice_value.to.name,
                                                       tunnel.fr.name if begin else tunnel.to.name,
                                                       begin)
        print("Route: "+" ".join([x for x in devices]))
        print("Types: " + " ".join([x.name for x in device_types]))
        # Create return dict
        ret = {}
        # Set up all devices we know of (except first and last device, those are host and vpn gateway)
        for i in range(1, len(devices) - 1):
            device = DomainState.get_device(devices[i])
            print("Deploying "+device.name)
            if device and device.network == DomainState.config.network:
                # We know this device and it is on our network
                device_type = device_types[i]
                queue = Queue(queue_id=0,  # Will be set by switch
                              min_rate=tunnel.min_rate,
                              max_rate=tunnel.max_rate,
                              burst_rate=tunnel.burst_rate,
                              priority=1,
                              port=DomainUtil.port_name_of_switch(device, devices[i + 1])
                              )
                print("Queue initialized")
                queue, _ = SwitchDeployment.setup_switch(switch=device,
                                                         switch_type=device_type,
                                                         prev_name=devices[i - 1],
                                                         next_name=devices[i + 1],
                                                         slice_id=slice_value.slice_id,
                                                         protocol=slice_value.transport_protocol,
                                                         src_ip=slice_value.fr.ip,
                                                         src_port=0,  # No enforcement
                                                         dst_ip=slice_value.to.ip,
                                                         dst_port=slice_value.to.port,
                                                         queue=queue
                                                         )
                ret[device.name] = queue
            print("Deployed "+device.name)

        # Update tunnel matches
        DomainState.tunnel_queue_pools[tunnel.tunnel_id] = \
            TunnelDeployment.deploy_tunnel(tunnel,
                                           DomainState.tunnel_queue_pools[
                                               tunnel.tunnel_id] if tunnel.tunnel_id in DomainState.tunnel_queue_pools.keys() else {}
                                           )

        return ret

    @classmethod
    def remove_slice(cls, slice_value: Slice, queue_pool: Dict[str, Queue]):
        # Remove switch infra
        for switch_name, queue in queue_pool.items():
            SwitchDeployment.uninstall_switch(switch=DomainState.get_device(switch_name),
                                              slice_id=slice_value.slice_id,
                                              queues=[queue],
                                              queues_reversed=[]
                                              )
