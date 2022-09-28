#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
            if x = 0:
                return 0
            for i in range(x):
                if i < x:
                    print(my_list[i], end="")
            print()
        except IndexError:
            print()
        finally:
            if x > i:
                return i
            else:
                return x + 1
