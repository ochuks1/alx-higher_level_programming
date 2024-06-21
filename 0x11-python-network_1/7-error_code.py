#!/usr/bin/python3
"""Sends a request to a URL and handles HTTP status codes"""

import sys
import requests

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
