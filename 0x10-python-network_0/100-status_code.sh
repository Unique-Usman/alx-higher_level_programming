#!/usr/bin/env bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response

curl -o /dev/null -w '%{http_code}' -sLI "$1"
