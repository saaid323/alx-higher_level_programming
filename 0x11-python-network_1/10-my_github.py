#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pat = sys.argv[2]
    url = f"https://api.github.com/user"
    auth = (username, pat)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info['id']
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print("None")
