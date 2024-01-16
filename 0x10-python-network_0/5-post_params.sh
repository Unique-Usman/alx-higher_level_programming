#!/usr/bin/env bash
# send a post request to the passed usr
# display the body of the response
# variable email
# subject

curl -d email="test@gmail.com" -d subject="I will always be here for PLD" "$1"
