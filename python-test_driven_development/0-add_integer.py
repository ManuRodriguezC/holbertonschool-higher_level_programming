#!/usr/bin/python3
"""Module"""


def add_integer(a, b=98):
    """
    This function return add of a and b, where a
    and b need to int or floats numbers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    else:
        return a + b
"""Check doctest of the module"""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
