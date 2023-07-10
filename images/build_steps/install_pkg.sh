#!/bin/bash

lxc exec "$1" -- mkdir -p "/opt/slicing_modules"
lxc file push --recursive "$2" "$1/opt/slicing_modules"
lxc exec "$1" -- mv "/opt/slicing_modules/$(basename "$2")" "/opt/slicing_modules/$(basename "$(realpath -s "$2/..")")_$(basename "$2")"
lxc exec "$1" -- pip install -e "/opt/slicing_modules/$(basename "$(realpath -s "$2/..")")_$(basename "$2")"


