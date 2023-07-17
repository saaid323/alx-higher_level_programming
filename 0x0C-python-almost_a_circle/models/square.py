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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
