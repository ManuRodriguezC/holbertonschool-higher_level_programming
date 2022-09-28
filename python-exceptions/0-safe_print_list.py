#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
            num = 0
            while num < x:
                print(my_list[num], end="")
                num += 1
            print()
        except IndexError:
            print()
        finally:
            return num
