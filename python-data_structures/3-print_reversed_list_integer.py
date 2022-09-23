#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list = None:
        return None
    my_list.reverse()
    position = 0
    while position < len(my_list):
        print("{:d}".format(my_list[position]))
        position += 1
