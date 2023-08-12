# Local Edgeslicing scenario

Uses 3 domains (2 edges, 1 black network) with two switches each.
Between the domains there are 2 VPN gateways.
The 2 adversaries are in the two edges and can communicate via a bypass line around the VPN gateways to and from the black network.
The adversaries have 2G link speed to the switches, while everything else uses 1G.

The adversaries have more capacity to simulate multiple malicious nodes flooding parts of our path that also our
clean traffic has to take (the link between the two switches of each domain).

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
$switch1a> ovs-ofctl add-flow switch1a ip,nw_src=10.0.0.12,nw_dst=10.0.0.13,in_port="testnode-eth1",actions=set_queue:<queue_id>,output:"testnode-eth2"
$switch1a> ovs-ofctl add-flow switch1a ip,nw_src=10.0.0.13,nw_dst=10.0.0.12,in_port="testnode-eth2",actions=output:"testnode-eth1"
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
# Test reachability
$adv1> hping3 --flood --udp -p 5432 10.0.0.13 -d 12000
$adv2> ifstat
# To remove all flows again
$switch1a> ovs-ofctl del-flows switch1a cookie=0/-1
$switch1b> ovs-ofctl del-flows switch1b cookie=0/-1
$switchbna> ovs-ofctl del-flows switchbna cookie=0/-1
$switchbnb> ovs-ofctl del-flows switchbnb cookie=0/-1
$switch2a> ovs-ofctl del-flows switch2a cookie=0/-1
$switch2b> ovs-ofctl del-flows switch2b cookie=0/-1
```
Hping3 will send about 3Gbit/s over a 2Gbit/s link and leave the first switch with ~300Mbit/s.

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
  "min_rate": 8000000,
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
  "min_rate": 8000000,
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
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec   935 KBytes  7.66 Mbits/sec  0.058 ms  0/767 (0%)  
[  5]   1.00-2.00   sec   977 KBytes  8.01 Mbits/sec  0.012 ms  0/802 (0%)  
[  5]   2.00-3.00   sec   976 KBytes  8.00 Mbits/sec  0.089 ms  0/801 (0%)  
[  5]   3.00-4.00   sec   976 KBytes  8.00 Mbits/sec  0.140 ms  0/801 (0%)  
[  5]   4.00-5.00   sec   976 KBytes  8.00 Mbits/sec  0.018 ms  0/801 (0%)  
[  5]   5.00-6.00   sec   976 KBytes  8.00 Mbits/sec  0.068 ms  0/801 (0%)  
[  5]   6.00-7.00   sec   977 KBytes  8.01 Mbits/sec  0.018 ms  0/802 (0%)  
[  5]   7.00-8.00   sec   976 KBytes  8.00 Mbits/sec  0.033 ms  0/801 (0%)  
[  5]   8.00-9.00   sec   973 KBytes  7.97 Mbits/sec  0.213 ms  4/802 (0.5%)  
[  5]   9.00-10.00  sec   976 KBytes  8.00 Mbits/sec  0.017 ms  0/801 (0%)  
[  5]  10.00-10.04  sec  41.4 KBytes  7.93 Mbits/sec  0.016 ms  0/34 (0%)  
- - - - - - - - - - - - - - - - - - - - - - - - -
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5] (sender statistics not available)
[SUM]  0.0-10.0 sec  9 datagrams received out-of-order
[  5]   0.00-10.04  sec  9.53 MBytes  7.96 Mbits/sec  0.016 ms  4/8013 (0.05%)  receiver

[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec   930 KBytes  7.62 Mbits/sec  0.032 ms  2/765 (0.26%)  
[  5]   1.00-2.00   sec   976 KBytes  8.00 Mbits/sec  0.120 ms  0/801 (0%)  
[  5]   2.00-3.00   sec   952 KBytes  7.80 Mbits/sec  0.034 ms  20/801 (2.5%)  
[  5]   3.00-4.00   sec   963 KBytes  7.89 Mbits/sec  0.066 ms  11/801 (1.4%)  
[  5]   4.00-5.00   sec   976 KBytes  8.00 Mbits/sec  0.030 ms  0/801 (0%)  
[  5]   5.00-6.00   sec   966 KBytes  7.92 Mbits/sec  0.025 ms  9/802 (1.1%)  
[  5]   6.00-7.00   sec   976 KBytes  8.00 Mbits/sec  0.122 ms  1/802 (0.12%)  
[  5]   7.00-8.00   sec   976 KBytes  8.00 Mbits/sec  0.192 ms  0/801 (0%)  
[  5]   8.00-9.00   sec   976 KBytes  8.00 Mbits/sec  0.046 ms  0/801 (0%)  
[  5]   9.00-10.00  sec   957 KBytes  7.84 Mbits/sec  0.026 ms  17/802 (2.1%)  
[  5]  10.00-10.05  sec  43.9 KBytes  7.81 Mbits/sec  0.159 ms  0/36 (0%)  
- - - - - - - - - - - - - - - - - - - - - - - - -
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5] (sender statistics not available)
[SUM]  0.0-10.0 sec  38 datagrams received out-of-order
[  5]   0.00-10.05  sec  9.47 MBytes  7.90 Mbits/sec  0.159 ms  60/8013 (0.75%)  receiver

```
Without ou background traffic running we observe similar results, but without packet drops. Sometimes short spikes (`<1s`)
can be observed of up to 4% packet loss - but over a time of 10 seconds we always observed `<1%` packet loss for this
example media slice.

#### Raw output from ping

There is no output from ping, as ICMP is not supported. Please see results below from UDP ping.

#### Test suite output

```
$> lxc file push config_h1.json h1/root/
$> lxc file push config_h2.json h2/root/
$h2> python3 -m host_client config_h2.json <IPERF|SOCKPERF|UDP_PING>
$h1> python3 -m host_client config_h1.json <IPERF|SOCKPERF|UDP_PING>
```
The configurations and outputs can be viewed in this directory in json format.

### Result
To be continued...

### Topology Implementation
Please refer to the `local_edgeslicing.py` file. The testbed was deployed to a single compute node.