#!/usr/bin/python3
"""A Square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """Initiating size of Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
