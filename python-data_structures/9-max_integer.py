#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = my_list[0]
    pos = 0
    while pos < len(my_list):
        if my_list[pos] > maxi:
            maxi = my_list[pos]
        pos += 1
    return maxi
