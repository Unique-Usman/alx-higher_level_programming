#!/usr/bin/python3

"""
A python script that fetches data from https://alx-intranet.hbtn.io/status
"""
import requests
import sys
res = requests.get(sys.argv[1])

if res.status_code >= 400:
    print(f"Error code: {res.status_code}")
else:
    print(res.text)

# another way to do this is to use the Response.raise_for_status()
