#!/usr/bin/python3
"""A Square"""


class Square:
    """Square"""
    def __init__(self, size):
        """Initiating size of Square"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Calculates area of square"""
        return self.__size * self.__size
