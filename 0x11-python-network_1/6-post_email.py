#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
