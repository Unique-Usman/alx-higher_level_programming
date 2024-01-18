#!/usr/bin/python3

"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the X-Request-Id variable found in
the header of the response.
"""

from urllib import request, parse
import sys

value = {
    "email": sys.argv[2]
}
data = parse.urlencode(value)
data = data.encode("ascii")
req = request.Request(f"{sys.argv[1]}", data)

with request.urlopen(req) as response:
    content = response.read()
    print(content.decode("utf8"))
