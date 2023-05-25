#!/bin/bash

IMAGE_NAME="slicing-ovs"

# cd to script dir
cd "$( dirname "$0" )" || exit 1
# Check setup
bash setup.sh

# Build normal testbed container
bash build_steps/init_img.sh "$IMAGE_NAME"

# Install ovs and other dependencies
sysctl -w kernel.dmesg_restrict=0 # OVS installer uses dmesg in container
lxc exec "$IMAGE_NAME" -- apt install -y iputils-ping net-tools iperf3 wireguard tcpdump ifstat python3 python3-pip
lxc exec "$IMAGE_NAME" -- apt install -y openvswitch-switch || true # Installation will fail due to hostname service :/
lxc exec "$IMAGE_NAME" -- rm /etc/systemd/system/openvswitch-switch.service.requires/ovs-record-hostname.service # remove requirement
lxc exec "$IMAGE_NAME" -- systemctl disable openvswitch-switch.service
sysctl -w kernel.dmesg_restrict=1
lxc exec "$IMAGE_NAME" -- apt clean
lxc exec "$IMAGE_NAME" -- apt autoremove -y

# Install our service components
bash build_steps/install_pkg.sh "$IMAGE_NAME" ../src/switch/server

# Finalize normal testbed container
bash build_steps/finalize_img.sh "$IMAGE_NAME"