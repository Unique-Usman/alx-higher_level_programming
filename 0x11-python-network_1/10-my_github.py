#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    passwd = sys.argv[2]
    basic = HTTPBasicAuth(sys.argv[1], passwd)
    res = requests.get("https://api.github.com/user", auth=basic)
    try:
        res = res.json()
        print(res["id"])
    except Exception as e:
        print(e) 
