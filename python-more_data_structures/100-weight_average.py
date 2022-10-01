#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    div = 0
    mul = 0
    for position in range(len(my_list)):
        mul += my_list[position][0] * my_list[position][0]
        div += my_list[position][1]
    return mul / div
