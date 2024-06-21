#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id variable in the header"""

import sys
from urllib import request

url = sys.argv[1]

with request.urlopen(url) as response:
    header_value = response.headers.get('X-Request-Id')
    print(header_value)
