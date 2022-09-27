#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
            for i in range(len(my_list)):
                if i < x:
                    print(my_list[i], end="")
            print()
        except IndexError:
            print()
        finally:
            if x > len(my_list):
                return len(my_list)
            else:
                return x
