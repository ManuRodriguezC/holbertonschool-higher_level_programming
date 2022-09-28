#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num, pos = 0, 0
    while pos < x:
        try:
            print("{:d}".format(my_list[pos]), end="")
            num += 1
            pos += 1
        except (TypeError, ValueError):
            pos += 1
            continue
    print()
    return num
