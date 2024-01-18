#!/usr/bin/python3

"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""

from urllib import request, error
import sys

req = request.Request(f"{sys.argv[1]}")

try:
    with request.urlopen(req) as response:
        content = response.read()
        content_utf8 = content.decode("utf-8")
        print(content_utf8)
except error.HTTPError as e:
    print(f"Error code: {e.status}")
