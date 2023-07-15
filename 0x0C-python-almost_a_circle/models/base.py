#!/usr/bin/python3
"""
The base class
"""


class Base:
    """
    base classe
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
