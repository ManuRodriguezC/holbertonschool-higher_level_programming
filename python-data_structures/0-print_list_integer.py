#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = 0
    size = len(my_list)
    while count < size:
        print("{}".format(my_list[count]))
        count += 1
