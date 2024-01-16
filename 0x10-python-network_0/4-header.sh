#!/usr/bin/env bash
# sent a get request and displays the body of the response
# also add X-School-User-Id with the value 98

curl -sH "X-School-User-Id: 98" "$1"
