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
        """Initialize  Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ that prints in stdout the Rectangle instance with
        the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ print in stdout the Rectangle instance
        with the character # by taking care of x and y"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'width':
                self.__width = value
            if key == 'height':
                self.__height = value
            if key == 'x':
                self.__x = value
            if key == 'y':
                self.__y = value

    def to_dictionary(self):
        """ assigns an argument to each attribute"""
        return {"y": self.__y, "x": self.__x, "id": self.id,
                "width": self.__width, "height": self.__height}
