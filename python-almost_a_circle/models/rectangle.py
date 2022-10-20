#!/usr/bin/python3
"""Module: Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class rectagle that inherete of the base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method return the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """This method print a rectangle"""
        for y in range(self.__y):
            print()
        for higt in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for base in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This method return the information of the rectangle"""
        div_x_y = f"{self.__x}/{self.__y}"
        div_w_h = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {div_x_y} - {div_w_h}"

    def update(self, *args, **kwargs):
        """This method assigns an argument to each attibute"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                if key == "width":
                    self.__width = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        if args is not None:
            count = 0
            for arv in args:
                if count == 0:
                    self.id = arv
                if count == 1:
                    self.__width = arv
                if count == 2:
                    self.__height = arv
                if count == 3:
                    self.__x = arv
                if count == 4:
                    self.__y = arv
                count += 1

    def to_dictionary(self):
        """This method return the dictionary of class"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
