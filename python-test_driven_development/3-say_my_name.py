#!/usr/bin/python3
"""Module: 3-say_my_name.py"""


def say_my_name(first_name, last_name=""):
    """
    Checks if first and last name is strings
    if first and las name is string print with:
    My name is {first_name} {last_name}
    """
    error_first = "first_name must be a string"
    error_last = "last_name must be a string"
    if type(first_name) != str:
        raise TypeError(error_first)

    if type(last_name) != str:
        raise TypeError(error_last)

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
