#!/bin/bash

# Make sure the access token is provided
if [[ -z "$1" ]]; then
  echo "Usage: ${0} <apaleo Base64-encode clientId:clientSecret>"
  echo "For details, see README.md steps 3&4"
  exit 1
fi

# Print the argument if it is present.
echo "Retrieving access with parameter ${1}"

curl --location 'https://identity.apaleo.com/connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header "Authorization: Basic ${1}" \
--data-urlencode 'grant_type=client_credentials'