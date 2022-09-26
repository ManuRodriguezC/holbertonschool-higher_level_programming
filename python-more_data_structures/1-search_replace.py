#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for value in range(len(new)):
        if new[value] == search:
            new[value] = replace
    return new
