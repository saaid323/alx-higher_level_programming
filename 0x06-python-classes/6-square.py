#!/usr/bin/python3
"""A Square"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initiating size of Square"""
        self.__position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) for coord in value) or \
                any(coord < 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of square"""
        return self.size * self.size

    def my_print(self):
        """Prints the Square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
