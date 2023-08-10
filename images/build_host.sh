#!/bin/bash

IMAGE_NAME="slicing-host"

# cd to script dir
cd "$( dirname "$0" )" || exit 1
# Check setup
bash setup.sh

# Build normal testbed container
bash build_steps/init_img.sh "$IMAGE_NAME"

# Install dependencies
lxc exec "$IMAGE_NAME" -- apt install -y iputils-ping net-tools iperf3 wireguard tcpdump ifstat python3 python3-pip hping3

# Install sockperf
lxc exec "$IMAGE_NAME" -- apt install -y perl make automake autoconf m4 libtool-bin g++ git
lxc exec "$IMAGE_NAME" -- git clone https://github.com/Mellanox/sockperf.git
lxc exec "$IMAGE_NAME" -- bash -c "echo \$(cd sockperf; bash autogen.sh; bash configure; make; make install)"
lxc exec "$IMAGE_NAME" -- rm -rf sockperf

# Cleanup
lxc exec "$IMAGE_NAME" -- apt clean
lxc exec "$IMAGE_NAME" -- apt autoremove -y

# Install our service components
bash build_steps/install_pkg.sh "$IMAGE_NAME" ../src/esmf/client
bash build_steps/install_pkg.sh "$IMAGE_NAME" ../src/host/client
bash build_steps/install_pkg.sh "$IMAGE_NAME" ../src/host/adversary

# Finalize normal testbed container
bash build_steps/finalize_img.sh "$IMAGE_NAME"