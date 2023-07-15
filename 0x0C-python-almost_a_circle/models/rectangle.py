#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defining Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing Rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
