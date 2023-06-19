#!/bin/bash

IMAGE_NAME="slicing-jump-host"

# cd to script dir
cd "$( dirname "$0" )" || exit 1
# Check setup
bash setup.sh

# Build normal testbed container
bash build_steps/init_img.sh "$IMAGE_NAME"

# Install dependencies
lxc exec "$IMAGE_NAME" -- apt install -y iputils-ping net-tools iperf3 wireguard tcpdump ifstat python3 python3-pip
lxc exec "$IMAGE_NAME" -- apt clean
lxc exec "$IMAGE_NAME" -- apt autoremove -y

# Install our service components
bash build_steps/install_pkg.sh "$IMAGE_NAME" ../src/jump_host/server

# Finalize normal testbed container
bash build_steps/finalize_img.sh "$IMAGE_NAME"