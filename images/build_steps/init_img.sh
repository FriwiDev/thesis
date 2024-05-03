#!/bin/bash

rm -f "export/$1.tar.gz"
lxc rm -f "$1"
lxc image delete "$1"
lxc remote add --protocol simplestreams ubuntu-minimal https://cloud-images.ubuntu.com/minimal/releases/ || true

lxc network create lxcbr0
lxc network set lxcbr0 ipv4.nat true
lxc network set lxcbr0 ipv4.nat.address 172.23.219.44

lxc init ubuntu-minimal:focal "$1" --profile default
lxc network attach lxcbr0 "$1" lxcbr0 eth0
lxc start "$1"
sleep 3 #Allow container to perform dhcp and establish a connection
lxc exec "$1" -- apt update
lxc exec "$1" -- apt upgrade -y