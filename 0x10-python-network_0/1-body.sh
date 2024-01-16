#!/usr/bin/env bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response

status_code=$(curl -sI "$1" | grep HTTP/1.1 | awk '{print $2}')

if [[ status_code -eq 200 ]]
then
  curl "$1";
fi
