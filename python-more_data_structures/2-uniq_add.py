#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = my_list[0]
    for pos in range(len(my_list)):
        if my_list[pos] > my_list[pos - 1]:
            add += my_list[pos]
    return add
