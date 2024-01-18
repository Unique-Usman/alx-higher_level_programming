#!/usr/bin/python3

"""Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
import requests
import sys

req = requests.post(f"{sys.argv[1]}",
                    data={"email": f"{sys.argv[2]}"})
print(req.text)
