#!/bin/bash

# Change working directory to our own directory to prevent files being written to arbitrary locations
cd "$(dirname "$0")" || exit 1

# Define a function to create a python client and server for our OpenAPI definitions
generate_component () {
  rm -rf "gen/$1"
  mkdir -p "gen/$1/client"
  _JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" ./openapi-generator-cli.sh generate -i "../$1.json" -g python -o "gen/$1/client"
  mkdir -p "gen/$1/server"
  ./openapi-generator-cli.sh generate -i "../$1.json" -g python-aiohttp -o "gen/$1/server"
}

# Fetch script
curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh > openapi-generator-cli.sh
chmod +x openapi-generator-cli.sh

# Perform the generation for every openapi definition
generate_component "ctmf"
generate_component "dsmf"
generate_component "dtmf"
generate_component "esmf"
generate_component "switch"