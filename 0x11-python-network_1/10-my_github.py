#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    auth = (user, password)
    r = requests.get('https://api.github.com/user', auth=auth)
    user = r.json()
    try:
        user_id = user['id']
        print(user['id'])
    except KeyError:
        print('None')
