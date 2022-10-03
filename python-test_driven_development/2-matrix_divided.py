#!/usr/bin/python3
"""Modulo"""

def matrix_divided(matrix, div):
    """this function"""
    if type(matrix) != list and (type(matrix[0]) != list) and (type(matrix[1]) != list):
        raise TypeError(" must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    new_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of list) of integers/floats")
            new.append(round(matrix[i][j] / div, 2))
        new_list.append(new)
        new = []
    return new_list
"""check doctest to module"""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-amtrix_divided.txt")