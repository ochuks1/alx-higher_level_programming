#!/usr/bin/python3
"""Uses the GitHub API to display the user's ID"""

import sys
import requests
from requests.auth import HTTPBasicAuth

username = sys.argv[1]
token = sys.argv[2]

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, token))
print(response.json().get('id'))
