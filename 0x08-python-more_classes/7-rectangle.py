#!/usr/bin/python3
"""
Define Rectangle
"""


class Rectangle:
    """
    Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        self.print_symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([self.print_symbol * self.__width
                          for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle{(self.__width, self.__height)}"