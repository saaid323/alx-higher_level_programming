#!/usr/bin/python3
"""
A square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """print in stdout the Rectangle instance
        with the character # by taking care of x and y"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        """assigns an argument to each attribute"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
