#!/bin/bash

lxc stop "$1"
lxc profile remove "$1" macvlan
lxc start "$1"
lxc stop "$1"
lxc snapshot "$1" snap1
lxc publish "$1"/snap1 --alias "$1" --public
mkdir -p export
lxc image export "$1" "export/$1"
lxc rm "$1"