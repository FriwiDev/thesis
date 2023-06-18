# OVS QoS commands

Small sidenote on QoS commands for OpenVSwitch. All units are in Bits/s.

## Queue management

### Listing queues on a port

```bash
ovs-appctl -t ovs-vswitchd qos/show {interface}
```

### Removing all queues on a port

```bash
ovs-vsctl set port {interface} qos=@newqos -- --id=@newqos create qos type=linux-htb
```

### Setting one or multiple queues
This will remove all other queues not specified in this command (keep state in application).
Can set from 1 to N queues.

```bash
ovs-vsctl set port {interface} qos=@newqos -- --id=@newqos create qos type=linux-htb queues:1=@queue1 ... queues:N=@queueN -- --id=@queue1 create queue other-config:min-rate={rate} other-config:burst={rate} other_config:max-rate={rate} other_config:priority={priority} -- ... -- --id=@queueN create queue other-config:min-rate={rate} other-config:burst={rate} other_config:max-rate={rate} other_config:priority={rate}
```

## Ingress shaping

### Showing ingress parameters on a port

```bash
ovs-vsctl list interface {interface}
```

### Setting ingress parameters on a port

```bash
ovs-vsctl set interface {interface} ingress_policing_rate={rate} ingress_policing_burst={rate}
```
Default for each rate is 0.

## Sources
- https://ovs-dpdk-1808-merge.readthedocs.io/en/latest/topics/dpdk/qos.html (Last checked 18.06.2023)
- https://docs.openvswitch.org/en/latest/faq/qos/ (Last checked 18.06.2023)