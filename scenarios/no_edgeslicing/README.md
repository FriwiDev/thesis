# No Edgeslicing scenario

Uses two switches with two hosts and two adversaries.
The adversaries have 2G link speed to the switches, while the hosts have 1G.
The switches are connected via a 1G link.

The adversaries have more capacity to simulate multiple malicious nodes flooding the egress of our domain
(the connection between the two switches).

### Used adversary commands

```bash
$> hping3 --flood --udp -p 5432 <other_adversary_ip> -d 12000
```

### Observation

#### Raw output from iperf3
When sending 8M of UDP packets from h1 to h2 via iperf3, we get an output similar to this:

```
$> iperf3 -c 10.0.0.6 --udp -b 8M -t 10000
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
...
[  5]   6.00-7.00   sec  60.8 KBytes   498 Kbits/sec  5.358 ms  87/130 (67%)  
[  5]   7.00-8.00   sec  53.7 KBytes   440 Kbits/sec  1.120 ms  194/232 (84%)  
[  5]   8.00-9.00   sec  63.6 KBytes   522 Kbits/sec  2.136 ms  168/213 (79%)  
[  5]   9.00-10.00  sec  59.4 KBytes   486 Kbits/sec  2.313 ms  146/188 (78%)  
[  5]  10.00-11.00  sec  66.5 KBytes   544 Kbits/sec  1.113 ms  102/149 (68%)  
[  5]  11.00-12.00  sec  66.5 KBytes   545 Kbits/sec  0.109 ms  148/195 (76%)  
[  5]  12.00-13.00  sec  65.0 KBytes   533 Kbits/sec  0.013 ms  190/236 (81%)
...
```

#### Raw output from ping

```
$> ping 10.0.0.6
PING 10.0.0.6 (10.0.0.6) 56(84) bytes of data.
64 bytes from 10.0.0.6: icmp_seq=2 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=4 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=6 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=7 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=8 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=9 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=10 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=12 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=13 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=14 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=15 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=17 ttl=64 time=1978 ms
64 bytes from 10.0.0.6: icmp_seq=18 ttl=64 time=1997 ms
64 bytes from 10.0.0.6: icmp_seq=19 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=20 ttl=64 time=2000 ms
64 bytes from 10.0.0.6: icmp_seq=22 ttl=64 time=1984 ms
```

#### Test suite output

```
$> lxc file push config_h1.json host1/root/
$> lxc file push config_h2.json host2/root/
$host1> python3 -m host_client config_h1.json <IPERF|SOCKPERF|UDP_PING>
$host2> python3 -m host_client config_h2.json <IPERF|SOCKPERF|UDP_PING>
```
The configurations and outputs can be viewed in this directory in json format.

### Result
The network traffic congestion causes about 75% of traffic to be dropped from our 8M media slice.
Latency on the network increases to up to 2 seconds (according to ping, but it seems to be capped).
The bandwidth shrinks to ~500Kbits/sec where 8M are the required minimum.

### Topology Implementation
Please refer to the `no_edgeslicing.py` file. The testbed was deployed to a single compute node.