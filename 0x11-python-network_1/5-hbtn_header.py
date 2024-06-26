#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id variable in the response header"""

import sys
import requests

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))
