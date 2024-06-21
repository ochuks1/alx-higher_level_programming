#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
