#!/usr/bin/python3
"""script that takes 2 arguments in order to list 10 commits"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    result = r.json()
    li = {}
    for commit in result[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
