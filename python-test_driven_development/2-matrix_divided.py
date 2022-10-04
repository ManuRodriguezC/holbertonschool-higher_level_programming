#!/usr/bin/python3
"""Modulo"""


def matrix_divided(matrix, div):
    """this function"""

    zero = "division by zero"
    num = "div must be a number"
    size = "Each row of the matrix must have the same size"
    not_list = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError(zero)
    
    if type(div) != int and type(div) != float:
        raise TypeError(num)
    
    if type(matrix) != list:
        raise TypeError(not_list)

    new = []
    new_list = []
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(not_list)
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError(size)
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j](int, float)):
                raise TypeError(not_list)
            new.append(round(matrix[i][j] / div, 2))
        new_list.append(new)
        new = []
    return new_list

"""check doctest to module"""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-amtrix_divided.txt")
