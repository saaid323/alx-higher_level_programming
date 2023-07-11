#!/usr/bin/python3
"""
reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode="r") as f:
        f = f.readlines()
    for i in f:
        print(i)
