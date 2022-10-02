#!/usr/bin/python3
import sys
from typing import Type

def safe_print_integer_err(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError) as exc:
        sys.stderr.write("Exception: " + str(exc) + "\n")
        return False
