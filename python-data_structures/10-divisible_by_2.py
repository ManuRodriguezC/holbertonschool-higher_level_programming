#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for pos in range(len(my_list)):
        if my_list[pos] % 2 == 0:
            return True
        return False
