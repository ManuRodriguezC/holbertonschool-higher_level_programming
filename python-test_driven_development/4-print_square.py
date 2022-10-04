#!/usr/bin/python3
"""Module: 4-print_square"""


def print_square(size):
    """
    Checkd if size is int and if >= 0
    In the case taht size cumpled to required, print the square,
    wiht size = size.
    """
    error_type = "size must be an integer"
    error_size = "size must be >= 0"

    if type(size) == float and size < 0:
        raise TypeError(error_type)

    if type(size) != int:
        raise TypeError(error_type)

    if size < 0:
        raise ValueError(error_size)

    for base in range(size):
        for height in range(size):
            print("#", end="")
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
