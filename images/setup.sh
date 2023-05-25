#!/bin/bash

#cd to script dir
cd "$( dirname "$0" )" || exit 1

echo "::Checking for LXC/LXD"
if ! command -v lxc &> /dev/null
then
    echo "::LCX/LXD=>not found=>prompting installation"
    if command -v pacman &> /dev/null
    then
        pacman -Sy lxd
    else
        apt-get install lxd
    fi
    # Add to lxd group
    usermod -a -G lxd "$USER"
    # Add uids & gids for current user
    touch /etc/subuid
    touch /etc/subgid
    usermod --add-subuids 100000-1001000000 "$USER"
    usermod --add-subgids 100000-1001000000 "$USER"
    # Initialize lxd
    systemctl enable lxd --now
    lxd init --preseed < lxd_preseed.yml
    # Create macvlan profile
    lxc profile create macvlan
    lxc profile device add macvlan eth0 nic nictype=macvlan parent="$(route | grep '^default' | grep -o '[^ ]*$')"
else
    echo "::LXC/LXD=>found"
fi

if ! systemctl is-enabled --quiet lxd; then
    echo "::LXD not running=>enabling & starting service"
    systemctl enable lxd --now
fi

echo "Checking permissions for lxc"
if ! lxc info &> /dev/null; then
  echo "Could not connect to lxc daemon. Is it running and do you have permissions? Check with \"systemctl status lxd\" and \"lxc info\""
  exit 1
fi
echo "::Permissions ok"