#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError) as exc:
        print("Exception: {exc}".format(file=sys.stderr))
        return False
