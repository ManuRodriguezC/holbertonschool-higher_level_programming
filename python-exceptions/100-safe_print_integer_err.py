#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except:
        if value + "":
            sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        elif value + 1.1111:
            sys.stderr.write("Exception: Unknown format code 'd' for object of type 'float'\n")
        return False
