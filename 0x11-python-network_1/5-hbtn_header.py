#!/usr/bin/python3

"""
A python script that fetches data from https://alx-intranet.hbtn.io/status
"""
import requests

req = requests.get("https://alx-intranet.hbtn.io/status")
print(req.headers["X-Request-Id"])
