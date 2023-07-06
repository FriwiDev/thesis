from dsmf_server.impl.domain_state import DomainState
from dsmf_server.impl.domain_util import DomainUtil
from dsmf_server.impl.switch_deployment import SwitchDeployment
from dsmf_server.models import Tunnel, Slice
from switch_client.model.queue import Queue


class SliceDeployment(object):
    @classmethod
    def deploy_slice(cls, slice_value: Slice, tunnel: Tunnel) -> \
            dict[str, Queue]:
        from_device = DomainState.get_device(slice_value.fr.name)
        to_device = DomainState.get_device(slice_value.to.name)
        begin = None
        if from_device and from_device.network == DomainState.config.network:
            begin = True
        elif to_device and to_device.network == DomainState.config.network:
            begin = False
        if begin is None:
            raise Exception("Could not find source and target of slice")
        # Build a local route
        devices, device_types = DomainUtil.route_slice(slice_value.fr.name if begin else slice_value.to.name,
                                                       tunnel.fr.name if begin else tunnel.to.name,
                                                       begin)
        # Create return dict
        ret = {}
        # Set up all devices we know of (except first and last device, those are host and vpn gateway)
        for i in range(1, len(devices) - 1):
            device = DomainState.get_device(devices[i])
            if device and device.network == DomainState.config.network:
                # We know this device and it is on our network
                device_type = device_types[i]
                queue = Queue(queue_id=0,  # Will be set by switch
                              min_rate=tunnel.min_rate,
                              max_rate=tunnel.max_rate,
                              burst_rate=tunnel.burst_rate,
                              priority=1,
                              port=-1  # Will be set by setup_switch()
                              )
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
        return ret

    @classmethod
    def remove_slice(cls, slice_value: Slice, queue_pool: dict[str, Queue]):
        # Remove switch infra
        for switch_name, queue in queue_pool:
            SwitchDeployment.uninstall_switch(switch=DomainState.get_device(switch_name),
                                              slice_id=slice_value.slice_id,
                                              queues=[queue],
                                              queues_reversed=[]
                                              )
