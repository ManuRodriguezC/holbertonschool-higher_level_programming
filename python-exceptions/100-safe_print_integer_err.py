#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if type(value) == int:
            print("{:d}".format(value))
            return True
    except:
        return False
