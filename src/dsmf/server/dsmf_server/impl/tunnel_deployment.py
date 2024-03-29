import ipaddress
from typing import Dict, Tuple

from dsmf_server.impl.domain_state import DomainState, DeviceType
from dsmf_server.impl.domain_util import DomainUtil
from dsmf_server.impl.switch_deployment import SwitchDeployment
from dsmf_server.impl.vpn_deployment import VPNDeployment
from dsmf_server.models import Tunnel
from switch_client.model.queue import Queue
from vpn_gateway_client.model.tunnel_entry import TunnelEntry


class TunnelDeployment(object):
    @classmethod
    def deploy_tunnel(cls, tunnel: Tunnel, queue_pool: Dict[str, Tuple[Queue, Queue or None]]) -> \
            Dict[str, Tuple[Queue, Queue or None]]:
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
                    ingress_matches = []
                    for slice in DomainState.slice_deployments.values():
                        # Does the slice use our tunnel?
                        if slice.tunnel_id == tunnel.tunnel_id:
                            # Find all possible ingress interfaces for this slice
                            slice_devs, _ = DomainUtil.route_slice(slice.fr.name, tunnel.fr.name, True)
                            prev_hop = slice_devs[len(slice_devs)-2]
                            for connection in DomainState.get_device(tunnel.fr.name).connections:
                                if connection.other_end == prev_hop:
                                    # We found a valid interface that traffic could come from
                                    ingress_matches.append({
                                        "slice_id": slice.slice_id,
                                        "intf_name": connection.intf_name
                                    })

                    # Define the tunnel entry
                    entry = TunnelEntry(tunnel_entry_id=tunnel.tunnel_id,
                                        inner_subnet="0.0.0.0/0",  # Only our tc matches get redirected anyway
                                        local_port=tunnel.fr.port,
                                        remote_end=tunnel.to.ip + ":" + str(tunnel.to.port),
                                        private_key=tunnel.private_key,
                                        public_key=tunnel.public_key,
                                        ingress_matches=ingress_matches,
                                        egress_matches=[],
                                        # TODO Make these internal ip addresses configurable (currently we just try a
                                        # scheme to make them unique)
                                        local_tunnel_ip=str(ipaddress.ip_address(
                                            int(ipaddress.ip_address(tunnel.fr.ip))
                                            + pow(2, 32 - ipaddress.ip_network(  # TODO-FW Assumes ipv4, addr should be specified by coordinator
                                                DomainState.get_network(
                                                    DomainState.get_device(tunnel.fr.name).network
                                                ).subnet
                                            ).prefixlen)
                                            + tunnel.tunnel_id)),
                                        remote_tunnel_ip=str(ipaddress.ip_address(
                                            int(ipaddress.ip_address(tunnel.to.ip))
                                            + pow(2, 32 - ipaddress.ip_network(  # TODO-FW Assumes ipv4, addr should be specified by coordinator
                                                DomainState.get_network(
                                                    DomainState.get_device(tunnel.to.name).network
                                                ).subnet
                                            ).prefixlen) * 4
                                            + tunnel.tunnel_id))
                                        )
                    # Send to vpn endpoint
                    if not VPNDeployment.create_or_update_tunnel_entry(device, entry):
                        raise Exception("Error while deploying tunnel entry")
                elif device_type == DeviceType.TUN_EXIT:
                    # Build a list of all traffic that should traverse our tunnel
                    # (here nothing should be sent via tunnel)
                    egress_matches = []
                    for slice in DomainState.slice_deployments.values():
                        # Does the slice use our tunnel?
                        if slice.tunnel_id == tunnel.tunnel_id:
                            # Find one possible egress interface for this slice
                            slice_devs, _ = DomainUtil.route_slice(slice.to.name, tunnel.to.name, False)
                            next_hop = slice_devs[1]
                            for connection in DomainState.get_device(tunnel.to.name).connections:
                                if connection.other_end == next_hop:
                                    # We found a valid interface that traffic could come from
                                    egress_matches.append({
                                        "slice_id": slice.slice_id,
                                        "intf_name": connection.intf_name
                                    })
                                    break

                    # Define the tunnel entry
                    entry = TunnelEntry(tunnel_entry_id=tunnel.tunnel_id,
                                        inner_subnet="0.0.0.0/0",  # Only our tc matches get redirected anyway
                                        local_port=tunnel.to.port,
                                        remote_end=tunnel.fr.ip + ":" + str(tunnel.fr.port),
                                        private_key=tunnel.private_key,
                                        public_key=tunnel.public_key,
                                        ingress_matches=[],
                                        egress_matches=egress_matches,
                                        # TODO Make these internal ip addresses configurable (currently we just try a
                                        # scheme to make them unique)
                                        local_tunnel_ip=str(ipaddress.ip_address(
                                            int(ipaddress.ip_address(tunnel.to.ip))
                                            + pow(2, 32 - ipaddress.ip_network(  # TODO-FW Assumes ipv4, addr should be specified by coordinator
                                                DomainState.get_network(
                                                    DomainState.get_device(tunnel.to.name).network
                                                ).subnet
                                            ).prefixlen) * 4
                                            + tunnel.tunnel_id)),
                                        remote_tunnel_ip=str(ipaddress.ip_address(
                                            int(ipaddress.ip_address(tunnel.fr.ip))
                                            + pow(2, 32 - ipaddress.ip_network(  # TODO-FW Assumes ipv4, addr should be specified by coordinator
                                                DomainState.get_network(
                                                    DomainState.get_device(tunnel.fr.name).network
                                                ).subnet
                                            ).prefixlen)
                                            + tunnel.tunnel_id))
                                        )
                    # Send to vpn endpoint
                    if not VPNDeployment.create_or_update_tunnel_entry(device, entry):
                        raise Exception("Error while deploying tunnel exit")
                else:
                    # We set up a BN switch
                    queue = Queue(queue_id=0,  # Will be set by switch
                                  min_rate=tunnel.min_rate,
                                  max_rate=tunnel.max_rate,
                                  burst_rate=tunnel.burst_rate,
                                  priority=10000,
                                  port=DomainUtil.port_name_of_switch(device, devices[i + 1])
                                  )
                    old_queue = None
                    reverse_queue = None
                    if device.name in queue_pool.keys():
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
    def remove_tunnel(cls, tunnel: Tunnel, queue_pool: Dict[str, Tuple[Queue, Queue or None]]):
        # Remove switch infra
        for switch_name, queue_def in queue_pool.items():
            queue, reverse_queue = queue_def
            SwitchDeployment.uninstall_switch(switch=DomainState.get_device(switch_name),
                                              slice_id=tunnel.tunnel_id,
                                              queues=[queue],
                                              queues_reversed=[reverse_queue] if reverse_queue else []
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
