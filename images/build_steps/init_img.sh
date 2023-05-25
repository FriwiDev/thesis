#!/bin/bash

rm -f "export/$1.tar.gz"
lxc rm -f "$1"
lxc remote add --protocol simplestreams ubuntu-minimal https://cloud-images.ubuntu.com/minimal/releases/ || true
lxc init ubuntu-minimal:focal "$1" --profile default --profile macvlan
lxc start "$1"
sleep 3 #Allow container to perform dhcp and establish a connection
lxc exec "$1" -- apt update
lxc exec "$1" -- apt upgrade -y