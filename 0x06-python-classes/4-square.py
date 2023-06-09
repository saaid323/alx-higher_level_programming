#!/usr/bin/python3
"""A Square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """Initiating size of Square"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of square"""
        return self.size * self.size
