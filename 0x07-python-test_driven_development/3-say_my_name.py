#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
"""

msg = "first_name must be a string"
msg1 = "last_name must be a string"


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError(msg)
    if not isinstance(last_name, str):
        raise TypeError(msg1)
    print(f"My name is {first_name} {last_name}")
