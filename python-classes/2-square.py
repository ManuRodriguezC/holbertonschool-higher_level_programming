#!/usr/bin/python3
"""Create square class"""


class Square:
    """Create and initialize size attribute"""
    def __init__(self, size=0):
        """
        This comprobate is for determinet if size is
        type int or if size is less taht zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
