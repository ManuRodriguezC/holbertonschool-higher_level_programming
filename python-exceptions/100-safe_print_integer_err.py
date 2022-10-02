#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except TypeError:
        return False
