#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    q = None
    if len(sys.argv[1]) > 1:
        q = sys.argv[1]
    else:
        q = ''
    data = {"q": q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        result = r.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valiid JSON")
