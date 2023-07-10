#!/bin/bash

IMAGE_NAME="slicing-controller"

# cd to script dir
cd "$( dirname "$0" )" || exit 1
# Check setup
bash setup.sh

# Build normal testbed container
bash build_steps/init_img.sh "$IMAGE_NAME"

# Install ryu and other dependencies
lxc exec "$IMAGE_NAME" -- apt install -y iputils-ping net-tools iperf3 wireguard tcpdump ifstat python3 python3-pip python3-ryu
lxc exec "$IMAGE_NAME" -- apt clean
lxc exec "$IMAGE_NAME" -- apt autoremove -y

# Install our service components
pip install requests

# Finalize normal testbed container
bash build_steps/finalize_img.sh "$IMAGE_NAME"