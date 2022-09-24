#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for out in range(len(matrix)):
        for inside in range(len(matrix[out])):
            print("{:d}".format(matrix[out][inside]), end="")
            if inside < len(matrix[out]):
                print(" ", end="")
        print()
