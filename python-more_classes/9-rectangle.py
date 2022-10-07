#!/usr/bin/python3
"""Cteated the Rectangle class"""


class Rectangle:
    """Attribut of the class"""
    number_of_instances = 0
    print_symbol = "#"

    """This class contein the attributes wedth and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

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
        return self.__height * self.__width

    """This method calculates the perimeter of a rectangle"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    """Method that print a rectangle"""
    def __str__(self):
        rect = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)
                if i != (self.__height - 1):
                    rect += "\n"
            return rect
        else:
            return rect

    """Method that representation to the object"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ This method del the object of the class"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """Return that instants is more bigger, rect_1 or rect_2"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    """
    This classmethod receives the arguments
    and createa new instance call square
    """
    @classmethod
    def square(cls, size=0):
        new_rectangle = cls(size, size)
        return new_rectangle
