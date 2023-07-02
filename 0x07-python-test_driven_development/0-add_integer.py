#!/usr/bin/python3
"""
function that adds 2 integers.
The two arguments must be int or float
The function will return TypeError is they are not int or float
"""
def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
