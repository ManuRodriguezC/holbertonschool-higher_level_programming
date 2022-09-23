#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    position = 0
    while position < size:
        if position == idx:
            return my_list[position]
        if idx < 0 or idx > size:
            None
        position += 1
