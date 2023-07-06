import ipaddress

from dsmf_server.impl.domain_state import DomainState, DeviceType
from dsmf_server.impl.domain_util import DomainUtil
from dsmf_server.impl.switch_deployment import SwitchDeployment
from dsmf_server.impl.vpn_deployment import VPNDeployment
from dsmf_server.models import Tunnel
from switch_client.model.queue import Queue
from vpn_gateway_client.model.tunnel_entry import TunnelEntry


class TunnelDeployment(object):
    @classmethod
    def deploy_tunnel(cls, tunnel: Tunnel, queue_pool: dict[str, (Queue, Queue or None)]) -> \
            dict[str, (Queue, Queue or None)]:
        # Build a route across networks
        # TODO-FW The ESMF/CTMF could also tell us this information to make this more robust for alternative routes
        networks = DomainUtil.route_network(tunnel.fr.network, tunnel.to.network)
        # Find our network in the list of networks
        i = 0
        for net in networks:
            if net == DomainState.config.network:
                break
            i += 1
        if i >= len(networks):
            raise Exception("We are not in route of networks " + str(networks))
        # Find the previous network and next network on our path
        # We return ourselves if we are the first or last network
        prev_net = DomainState.config.network if i == 0 else networks[i - 1]
        next_net = DomainState.config.network if i == len(networks) - 1 else networks[i + 1]
        # Build a local route
        devices, device_types = DomainUtil.route_tunnel(tunnel.fr.name, tunnel.to.name, prev_net, next_net)
        # Create return dict
        ret = {}
        # Set up all devices we know of
        for i in range(len(devices)):
            device = DomainState.get_device(devices[i])
            if device and device.network == DomainState.config.network:
                # We know this device and it is on our network
                device_type = device_types[i]
                if device_type == DeviceType.TUN_ENTRY:
                    # Build a list of all traffic that should traverse our tunnel
                    matches = []
                    for slice in DomainState.slice_deployments.values():
                        if slice.tunnel_id == tunnel.tunnel_id:
                            # A slice that uses our tunnel
                            matches.append({
                                "transport_protocol": "UDP",
                                "source_ip": slice.fr.ip,
                                "target_ip": slice.to.ip,
                                "target_port": slice.to.port
                            })
                    # Define the tunnel entry
                    entry = TunnelEntry(tunnel_entry_id=tunnel.tunnel_id,
                                        inner_subnet=DomainState.get_network(device.network).subnet,
                                        local_port=tunnel.fr.port,
                                        remote_end=tunnel.to.ip + ":" + str(tunnel.to.port),
                                        private_key=tunnel.private_key,
                                        public_key=tunnel.public_key,
                                        matches=matches)
                    # Send to vpn endpoint
                    ret = VPNDeployment.create_or_update_tunnel_entry(device, entry)
                    if not ret:
                        raise Exception("Error while deploying tunnel entry")
                elif device_type == DeviceType.TUN_EXIT:
                    # Build a list of all traffic that should traverse our tunnel
                    # (here nothing should be sent via tunnel)
                    matches = []
                    # Define the tunnel entry
                    entry = TunnelEntry(tunnel_entry_id=tunnel.tunnel_id,
                                        inner_subnet=DomainState.get_network(device.network).subnet,
                                        local_port=tunnel.to.port,
                                        remote_end=tunnel.fr.ip + ":" + str(tunnel.fr.port),
                                        private_key=tunnel.private_key,
                                        public_key=tunnel.public_key,
                                        matches=matches)
                    # Send to vpn endpoint
                    ret = VPNDeployment.create_or_update_tunnel_entry(device, entry)
                    if not ret:
                        raise Exception("Error while deploying tunnel exit")
                else:
                    # We set up a BN switch
                    queue = Queue(queue_id=0,  # Will be set by switch
                                  min_rate=tunnel.min_rate,
                                  max_rate=tunnel.max_rate,
                                  burst_rate=tunnel.burst_rate,
                                  priority=1,
                                  port=-1  # Will be set by setup_switch()
                                  )
                    old_queue = None
                    reverse_queue = None
                    if device.name in queue_pool:
                        old_queue, reverse_queue = queue_pool[device.name]
                    res = SwitchDeployment.setup_switch(switch=device,
                                                        switch_type=device_type,
                                                        prev_name=devices[i - 1],
                                                        next_name=devices[i + 1],
                                                        slice_id=tunnel.tunnel_id,
                                                        protocol="UDP",
                                                        src_ip=ipaddress.ip_address(tunnel.fr.ip),
                                                        src_port=tunnel.fr.port,
                                                        dst_ip=ipaddress.ip_address(tunnel.to.ip),
                                                        dst_port=tunnel.to.port,
                                                        queue=queue,
                                                        reverse_queue=reverse_queue
                                                        )
                    if old_queue:
                        if not SwitchDeployment.delete_queue(switch=device, queue=old_queue):
                            raise Exception("Error while removing queue")
                    ret[device.name] = res
        return ret

    @classmethod
    def remove_tunnel(cls, tunnel: Tunnel, queue_pool: dict[str, (Queue, Queue or None)]):
        # Remove switch infra
        for switch_name, queue_def in queue_pool:
            queue, reverse_queue = queue_def
            SwitchDeployment.uninstall_switch(switch=DomainState.get_device(switch_name),
                                              slice_id=tunnel.tunnel_id,
                                              queues=[queue],
                                              queues_reversed=[reverse_queue]
                                              )
        # Delete vpn entry if we manage it
        vpn = DomainState.get_device(tunnel.fr.name)
        if vpn and vpn.network == DomainState.config.network:
            VPNDeployment.delete_tunnel_entry(vpn=vpn,
                                              tunnel_entry_id=tunnel.tunnel_id
                                              )
        # Delete vpn exit if we manage it
        vpn = DomainState.get_device(tunnel.to.name)
        if vpn and vpn.network == DomainState.config.network:
            VPNDeployment.delete_tunnel_entry(vpn=vpn,
                                              tunnel_entry_id=tunnel.tunnel_id
                                              )
