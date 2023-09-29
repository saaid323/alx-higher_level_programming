#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the
body of the response."""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code: ", e.status_code)
