#!/usr/bin/python3
"""Module that print pascal triangle"""


def pascal_triangle(n):
    """
    This function created a list that format of
    pascal triangle with the size n
    """
    list_pascal = []

    if n <= 0:
        return list_pascal

    temp = []
    value = 0
    for x in range(n):
        for y in range(n):
            if x >= y:
                if x > 1 and y > 0 and y < x:
                    value = list_pascal[x - 1][y] + list_pascal[x - 1][y - 1]
                if x > 1 and y == x:
                    value = list_pascal[x - 1][y - 1]
                if x > 1 and y == 0:
                    value = list_pascal[x - 1][y]
                if x < 1:
                    value = 1
                temp.append(value)
        list_pascal.append(temp)
        temp = []
    return list_pascal
