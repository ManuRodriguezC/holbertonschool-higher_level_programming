#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except ValueError as exc:
        sys.stderr.write("Exception: " + str(exc) + "\n")
        return False
    except TypeError as exc:
        sys.stderr.write("Exception: " + str(exc) + "\n")
        return False
    
