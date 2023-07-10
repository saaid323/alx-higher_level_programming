#!/usr/bin/python3
"""
function that adds a new attribute to an object
if it’s possible
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if isinstance(obj, (str, int)):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
