#!/usr/bin/python3
"""Create a square class"""


class Square:
    """This class contain one attribute"""
    def __init__(self, size=0):
        """
        Chack if the size is a integer type, if size is
        not integrer print a error with exception raise
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """This method calculate the square are if size is integer"""
    def area(self):
        a = self.__size * self.__size
        return a
