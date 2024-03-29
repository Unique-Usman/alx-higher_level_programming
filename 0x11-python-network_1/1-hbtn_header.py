#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

from urllib import request
import sys

req = request.Request(f"{sys.argv[1]}")

with request.urlopen(req) as response:
    print(response.getheader("X-Request-Id"))
