#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Define Square
"""


class Square(Rectangle):
    """
    Square that inherits from Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
