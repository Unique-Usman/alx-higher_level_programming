#!/usr/bin/python3

"""
Write a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

arg = ""
if len(sys.argv) == 1:
    arg = ""
else:
    arg = sys.argv[1]

req = requests.post("http://0.0.0.0:5000/search_user", data={"q": f"{arg}"})
try:
    res = req.json()
    if len(res) != 0:
        iid = res["id"]
        name = res["name"]
        print(f"[{iid}] {name}]")
    else:
        print("No result")
except Exception as e:
    print("Not a valid JSON")
