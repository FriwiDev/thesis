# Local Edgeslicing scenario

Uses 3 domains (2 edges, 1 black network) with two switches each.
Between the domains there are 2 VPN gateways.
The 2 adversaries are in the two edges and can communicate via a bypass line around the VPN gateways to and from the black network.
The adversaries have 10G link speed to the switches, while everything else uses 1G.

The adversaries have more capacity to simulate multiple malicious nodes flooding parts of our path that also our
clean traffic has to take (the link between the two switches of each domain).

Furthermore, the adversaries are locked to specific CPU cores.
This is due to the impact from the attackers on the other services if this limit is not in place.
The adversaries would steal processing power from the other services, resulting in tx drops along the lines - mainly in the vpn gateways (that are not even under attack).
As the cpu time of containers is not traffic related and only relevant in our testbed, we can exclude it from the equation by locking cpu cores for attackers.

### Used adversary commands

```bash
# Assumption: Using our testbed script
IP adv1 = 10.0.0.12
IP adv2 = 10.0.0.13
# Create queue for egress and note the queue id (on both switches connected to adversary)
$switch1a> curl -X 'PUT' \
  'http://localhost:8082/v1/queue?auth=token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "queue_id": 0,
  "min_rate": 300000000,
  "max_rate": 300000000,
  "burst_rate": 375000,
  "priority": 55555,
  "port": "testnode-eth2"
}' -v
$switch2b> curl -X 'PUT' \
  'http://localhost:8082/v1/queue?auth=token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "queue_id": 0,
  "min_rate": 300000000,
  "max_rate": 300000000,
  "burst_rate": 375000,
  "priority": 55555,
  "port": "testnode-eth15"
}' -v
# Create flows through the network (we only add a queue on the first and last egress for simplicity)
$switch1a> ovs-ofctl add-flow switch1a ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth19",actions=set_queue:<queue_id>,output:"testnode-eth2"
$switch1a> ovs-ofctl add-flow switch1a ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth2",actions=output:"testnode-eth19"
$switch1b> ovs-ofctl add-flow switch1b ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth3",actions=output:"testnode-eth22"
$switch1b> ovs-ofctl add-flow switch1b ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth22",actions=output:"testnode-eth3"
$switchbna> ovs-ofctl add-flow switchbna ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth23",actions=output:"testnode-eth8"
$switchbna> ovs-ofctl add-flow switchbna ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth8",actions=output:"testnode-eth23"
$switchbnb> ovs-ofctl add-flow switchbnb ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth9",actions=output:"testnode-eth25"
$switchbnb> ovs-ofctl add-flow switchbnb ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth25",actions=output:"testnode-eth9"
$switch2a> ovs-ofctl add-flow switch2a ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth24",actions=output:"testnode-eth14"
$switch2a> ovs-ofctl add-flow switch2a ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth14",actions=output:"testnode-eth24"
$switch2b> ovs-ofctl add-flow switch2b ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth15",actions=output:"testnode-eth21"
$switch2b> ovs-ofctl add-flow switch2b ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth21",actions=set_queue:<queue_id>,output:"testnode-eth15"
# Activate icmp for h1 and h2
$switch1a> ovs-ofctl add-flow switch1a icmp,in_port="testnode-eth1",actions=set_queue:<slice_queue_id>,output:"testnode-eth2"
$switch1a> ovs-ofctl add-flow switch1a icmp,in_port="testnode-eth2",actions=output:"testnode-eth1"
$switch1b> ovs-ofctl add-flow switch1b icmp,in_port="testnode-eth3",actions=output:"testnode-eth22"
$switch1b> ovs-ofctl add-flow switch1b icmp,in_port="testnode-eth22",actions=output:"testnode-eth3"
$switchbna> ovs-ofctl add-flow switchbna icmp,in_port="testnode-eth23",actions=output:"testnode-eth8"
$switchbna> ovs-ofctl add-flow switchbna icmp,in_port="testnode-eth8",actions=output:"testnode-eth23"
$switchbnb> ovs-ofctl add-flow switchbnb icmp,in_port="testnode-eth9",actions=output:"testnode-eth25"
$switchbnb> ovs-ofctl add-flow switchbnb icmp,in_port="testnode-eth25",actions=output:"testnode-eth9"
$switch2a> ovs-ofctl add-flow switch2a icmp,in_port="testnode-eth24",actions=output:"testnode-eth14"
$switch2a> ovs-ofctl add-flow switch2a icmp,in_port="testnode-eth14",actions=output:"testnode-eth24"
$switch2b> ovs-ofctl add-flow switch2b icmp,in_port="testnode-eth15",actions=output:"testnode-eth16"
$switch2b> ovs-ofctl add-flow switch2b icmp,in_port="testnode-eth16",actions=set_queue:<slice_queue_id>,output:"testnode-eth15"
# Test reachability
$adv1> hping3 --flood --udp -p 5432 10.0.0.13 -d 1200000
$adv2> ifstat
# To remove all flows again
$switch1a> ovs-ofctl del-flows switch1a cookie=0/-1
$switch1b> ovs-ofctl del-flows switch1b cookie=0/-1
$switchbna> ovs-ofctl del-flows switchbna cookie=0/-1
$switchbnb> ovs-ofctl del-flows switchbnb cookie=0/-1
$switch2a> ovs-ofctl del-flows switch2a cookie=0/-1
$switch2b> ovs-ofctl del-flows switch2b cookie=0/-1
```
Hping3 will send about 3Gbit/s over a 10Gbit/s link and leave the first switch with ~300Mbit/s 
(due to our bypass configuration of allowing 300Mbit/s per switch of other traffic).
Due to CPU limitation more than 3Gbit/s are not possible per adversary.
Even when allocating 30 threads of our CPU resources (32 threads) to multiple adversaries connected similar to adv1,
we can not achieve an increase in loss rate or latency, nor a decrease in bandwidth. More on this below.

### Used slice commands (for initial iperf test)
```bash
# To create
$ESMF1> curl -X 'PUT' \
  'http://localhost:8080/v1/slice?auth=token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
{      
  "slice_id": 0,
  "min_rate": 8388608,
  "max_rate": 12000000,
  "burst_rate": 120000000,
  "latency": 3,    
  "tunnel_id": 0,
  "transport_protocol": "UDP",
  "fr": {
    "ip": "10.0.0.2",
    "port": 0,  
    "name": "h1",
    "network": "net1"
  },     
  "to": {       
    "ip": "10.0.0.11",
    "port": 8888,
    "name": "h2",
    "network": "net2"
  }
},
{      
  "slice_id": 0,
  "min_rate": 8388608,
  "max_rate": 12000000,
  "burst_rate": 120000000,
  "latency": 3,    
  "tunnel_id": 0,
  "transport_protocol": "UDP",
  "fr": {
    "ip": "10.0.0.11",
    "port": 8888,
    "name": "h2",
    "network": "net2"
  },     
  "to": {       
    "ip": "10.0.0.2",
    "port": 0,  
    "name": "h1",
    "network": "net1"
  }
}
]' -v

# To delete
$ESMF1> -- curl -X 'DELETE' \
  'http://localhost:8080/v1/slice?auth=token&slice_ids=1000&slice_ids=1001' \
  -H 'accept: */*' -v
```

### Observation

#### Raw output from iperf3
When sending 8M of UDP packets from h1 to h2 via iperf3, we get an output similar to this:

```
$> iperf3 -c 10.0.0.11 --udp --port 8888 -b 8M -t 10
[  5] local 10.0.0.11 port 8888 connected to 10.0.0.2 port 38726
Starting Test: protocol: UDP, 1 streams, 1248 byte blocks, omitting 0 seconds, 10 second test, tos 0
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec   931 KBytes  7.63 Mbits/sec  0.014 ms  0/764 (0%)  
[  5]   1.00-2.00   sec   976 KBytes  8.00 Mbits/sec  0.010 ms  0/801 (0%)  
[  5]   2.00-3.00   sec   977 KBytes  8.01 Mbits/sec  0.015 ms  0/802 (0%)  
[  5]   3.00-4.00   sec   976 KBytes  8.00 Mbits/sec  0.020 ms  0/801 (0%)  
[  5]   4.00-5.00   sec   976 KBytes  8.00 Mbits/sec  0.012 ms  0/801 (0%)  
[  5]   5.00-6.00   sec   977 KBytes  8.01 Mbits/sec  0.015 ms  0/802 (0%)  
[  5]   6.00-7.00   sec   976 KBytes  8.00 Mbits/sec  0.009 ms  0/801 (0%)  
[  5]   7.00-8.00   sec   976 KBytes  8.00 Mbits/sec  0.042 ms  0/801 (0%)  
[  5]   8.00-9.00   sec   976 KBytes  8.00 Mbits/sec  0.015 ms  0/801 (0%)  
[  5]   9.00-10.00  sec   977 KBytes  8.01 Mbits/sec  0.034 ms  0/802 (0%)  
[  5]  10.00-10.05  sec  45.1 KBytes  7.98 Mbits/sec  0.013 ms  0/37 (0%)  
- - - - - - - - - - - - - - - - - - - - - - - - -
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5] (sender statistics not available)
[  5]   0.00-10.05  sec  9.54 MBytes  7.96 Mbits/sec  0.013 ms  0/8013 (0%)  receiver

```
Initially we observed small packet drops even when not letting any traffic flow to the first switches (switch1a and switch2b).
This was really suspicious. After investigating it appeared that because the adversaries could max the cpu in spikes,
the TX queue on vpn1 would overflow with our clean traffic, dropping data (most likely due to having the shortest queue length).
We thus pinned the adversaries to individual cores (for isolation purposes that are similar to a real world case),
improving our results to no packet drops, even with ~25Gbit/s of traffic on one switch, using half our cpu power (16 cores pinned to the attacker).
To increase our test to the limit, we started hping3 30 times on 30 threads, assigning almost all of our 32 threads.
Even in this example, we reached traffic rates of ~30Gbit/s, indicating our cpu bottleneck being reached on
our adversary containers, but not on our initial switch. We still observed no packet loss proving to us, that our
slice is fully isolated as long as the computational capacity of the switch is not being overloaded.

As a next test we hoped to observe packet loss when removing our ingress limit on the switches for the adversaries.
It appears though, that in our situation, this additional layer of security is not even needed. We still observed no
packet loss on our slices.

We then spammed the first switch with additional flows (which would even be difficult for a not in-path attacker).
With 32 flows that were placed on the switch additionally, still no change could be observed.

In all tests our delay was mostly under 0.3ms, while an occasional spike smaller than 2ms could be observed every other minute.
The guaranteed bandwidth of our slices never dropped below our configured guaranteed rate, apart from within one second after negotiation where slight decreases (<10%) could be observed.
Maybe this can be explained due to the implementation of our test suite, as this could also be observed when the adversaries were not active.
We thus conclude that our isolation was indeed successful.

#### Raw output from ping

Not under attack:
```
$h1> ping 10.0.0.11
PING 10.0.0.11 (10.0.0.11) 56(84) bytes of data.
64 bytes from 10.0.0.11: icmp_seq=1 ttl=64 time=0.904 ms
64 bytes from 10.0.0.11: icmp_seq=2 ttl=64 time=0.162 ms
64 bytes from 10.0.0.11: icmp_seq=3 ttl=64 time=0.130 ms
64 bytes from 10.0.0.11: icmp_seq=4 ttl=64 time=0.153 ms
64 bytes from 10.0.0.11: icmp_seq=5 ttl=64 time=0.172 ms
64 bytes from 10.0.0.11: icmp_seq=6 ttl=64 time=0.156 ms
64 bytes from 10.0.0.11: icmp_seq=7 ttl=64 time=0.166 ms
64 bytes from 10.0.0.11: icmp_seq=8 ttl=64 time=0.156 ms
64 bytes from 10.0.0.11: icmp_seq=9 ttl=64 time=0.154 ms
64 bytes from 10.0.0.11: icmp_seq=10 ttl=64 time=0.163 ms
--- 10.0.0.11 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9131ms
rtt min/avg/max/mdev = 0.130/0.231/0.904/0.224 ms
```

Under attack:
```
$h1> ping 10.0.0.11
PING 10.0.0.11 (10.0.0.11) 56(84) bytes of data.
64 bytes from 10.0.0.11: icmp_seq=1 ttl=64 time=0.980 ms
64 bytes from 10.0.0.11: icmp_seq=2 ttl=64 time=0.119 ms
64 bytes from 10.0.0.11: icmp_seq=3 ttl=64 time=0.109 ms
64 bytes from 10.0.0.11: icmp_seq=4 ttl=64 time=0.122 ms
64 bytes from 10.0.0.11: icmp_seq=5 ttl=64 time=0.113 ms
64 bytes from 10.0.0.11: icmp_seq=6 ttl=64 time=0.126 ms
64 bytes from 10.0.0.11: icmp_seq=7 ttl=64 time=0.100 ms
64 bytes from 10.0.0.11: icmp_seq=8 ttl=64 time=0.100 ms
64 bytes from 10.0.0.11: icmp_seq=9 ttl=64 time=0.118 ms
64 bytes from 10.0.0.11: icmp_seq=10 ttl=64 time=0.119 ms
--- 10.0.0.11 ping statistics ---
22 packets transmitted, 22 received, 0% packet loss, time 21268ms
rtt min/avg/max/mdev = 0.096/0.153/0.980/0.180 ms
```

There seems to be no difference, so our slicing was successful.
Test scenario was the scenario from above with 30Gbit/s of traffic from multiple adversaries.

#### Test suite output

```
$> lxc file push config_h1.json h1/root/
$> lxc file push config_h2.json h2/root/
$h2> python3 -m host_client config_h2.json <IPERF|SOCKPERF|UDP_PING>
$h1> python3 -m host_client config_h1.json <IPERF|SOCKPERF|UDP_PING>
```
The configurations and outputs can be viewed in this directory in json format.
Sadly udp_ping appears to be broken, as it returns bogus results compared to the other suites, even when idling.
If we still have time in the end, we might attempt to repair it.

Furthermore the latency reported from sockperf seems to be invalid as well, because we receive vastly different results
from `ping` within the same scenario, and the jitter in `iperf3` would need to be higher.
We confirmed the bandwidth using `ifstat` as well and are thus confident that the tool (and also udp_ping) measures this accurately.
We will thus take the results from ping.

### Result
Even under heavy load and increased difficulty, the QoS guarantees remain intact and the slice is isolated.

### Topology Implementation
Please refer to the `local_edgeslicing.py` file. The testbed was deployed to a single compute node and altered to
include more or less attackers, depending on the test being run. An explanation on what was tested can be viewed above.