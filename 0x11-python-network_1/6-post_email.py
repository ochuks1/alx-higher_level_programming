#!/usr/bin/python3
"""Sends a POST request to a URL with an email address and displays the response"""

import sys
import requests

url = sys.argv[1]
email = sys.argv[2]
response = requests.post(url, data={'email': email})
print(response.text)
