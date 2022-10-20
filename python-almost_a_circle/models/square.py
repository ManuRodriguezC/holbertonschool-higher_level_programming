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
