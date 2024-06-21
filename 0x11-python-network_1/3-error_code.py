#!/usr/bin/python3
"""Sends a request to a URL and handles HTTPError exceptions"""

import sys
from urllib import request, error

url = sys.argv[1]

try:
    with request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except error.HTTPError as e:
    print("Error code:", e.code)
