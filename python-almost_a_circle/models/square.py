#!/usr/bin/python3
"""Module: Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherete of the Rectangle class"""
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
        """This method return the information about the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """This method assignet a value a any attribute"""
        if args is not None:
            count = 1
            for arg in args:
                if count == 1:
                    self.id = arg
                if count == 2:
                    self.size = arg
                if count == 3:
                    self.x = arg
                if count == 4:
                    self.y = arg
                count += 1
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "y":
                    self.y = value
                if key == "x":
                    self.x = value

    def to_dictionary(self):
        """This method return the dictionary of the square class"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
