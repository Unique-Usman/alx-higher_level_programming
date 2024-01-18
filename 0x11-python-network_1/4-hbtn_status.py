#!/usr/bin/python3

"""
A python script that fetches data from https://alx-intranet.hbtn.io/status
"""
import requests

req = requests.get("https://alx-intranet.hbtn.io/status")
content = req.text
content_type = type(content)
print(f"""\
Body response:
    - type: {content_type}
    - content: {content}
""")
