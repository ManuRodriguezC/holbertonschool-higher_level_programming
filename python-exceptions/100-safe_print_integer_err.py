#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
