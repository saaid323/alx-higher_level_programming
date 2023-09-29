#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            data = response.read()
            print(data.decode())
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
