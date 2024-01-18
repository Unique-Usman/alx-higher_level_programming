#!/usr/bin/python3

"""
A python script that fetches data from https://alx-intranet.hbtn.io/status
"""
from urllib import request


req = request.Request("https://alx-intranet.hbtn.io/status")
with request.urlopen(req) as response:
    content = response.read()
    content_type = type(content)
    content_utf8 = content.decode("utf-8")

    print(f"""
Body response:
    - type: {content_type}
    - content: {content}
    - utf8 content: {content_utf8}
""")
