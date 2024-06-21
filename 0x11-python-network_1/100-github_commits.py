#!/usr/bin/python3
"""Fetches the 10 most recent commits of a given repository by a specific user"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i]['sha']
            author_name = commits[i]['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
