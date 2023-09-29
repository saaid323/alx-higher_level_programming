#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the
response."""
import urllib.request
import sys

re = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(re) as data:
    if 'X-Request-Id' in data.headers:
        x = data.headers['X-Request-Id']
        print(x)
