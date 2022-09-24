#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = my_list.copy()
    position = 0
    while position < len(new_list):
        if position == idx:
            new_list[position] = element
            return new_list
        position += 1
