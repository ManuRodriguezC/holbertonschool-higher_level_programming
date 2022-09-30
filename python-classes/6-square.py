#!/usr/bin/python3
"""
This programe create the square class wich received
the size of the square
"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0,0)):
        """Square class, this class conteint the attributes and methods"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """This method return the position value of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method modify and check the value of the position"""
        if type(self.__position[0]) != int and type(self.position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 and self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This methond calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """This method print to the square with the size"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for k in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
