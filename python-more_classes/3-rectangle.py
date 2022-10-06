#!/usr/bin/python3
"""Cteated the Rectangle class"""



class Rectangle:
    """This class contein the attributes wedth and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("eidth must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__heigh

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """This method calculates the area of a rectangle"""
    def area(self):
        return self.__width * self.__height

    """This method calculates the perimeter of a rectangle"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    """Method taht print a rectangle"""
    def __str__(self):
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i != (self.__height - 1):
                rect += "\n"
        return rect
