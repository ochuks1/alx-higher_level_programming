#!/usr/bin/python3
"""Sends a POST request to a URL with an email as a parameter and displays the response"""

import sys
from urllib import request, parse

url = sys.argv[1]
email = sys.argv[2]
data = parse.urlencode({'email': email}).encode()

with request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))
