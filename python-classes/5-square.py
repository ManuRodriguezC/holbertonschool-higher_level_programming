#!/usr/bin/python3
"""This programe create the square class wich received the size of the square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Square class, this class conteint the attributes and methods"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """This method return the value of the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method modify the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This methond calculate the area of the square"""
        a = self.__size * self.__size
        return a

    def my_print(self):
        """This method print to the square with the size"""
        if self.__size > 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        elif self.__size == 0:
            print()
