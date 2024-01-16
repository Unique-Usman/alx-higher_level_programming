#!/usr/bin/env bash
# post the content of a json file

curl -H "Content-Type: application/json" -d @"$2" "$1"
