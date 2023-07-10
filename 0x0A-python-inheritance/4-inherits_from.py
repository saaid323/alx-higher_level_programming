#!/usr/bin/python3
"""
returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified
class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    otherwise False
    """
    class_hierarchy = type(obj).__mro__
    return any(a_class in cls.__mro__ for cls in class_hierarchy[1:])
