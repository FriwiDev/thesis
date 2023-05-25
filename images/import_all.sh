#!/bin/bash

# cd to script dir
cd "$( dirname "$0" )" || exit 1
# Check setup
bash setup.sh

import_img() {
  if test -f "export/$1.tar.gz"; then
    echo "Importing export/$1.tar.gz"
    lxc image rm "$1"
    lxc image import export/"$1".tar.gz --alias "$1" --public
  else
    echo "Skipping import of export/$1.tar.gz because the file does not exist"
  fi
}

import_img slicing-ctmf
import_img slicing-dsmf
import_img slicing-dtmf
import_img slicing-esmf
import_img slicing-host
import_img slicing-ovs
