#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        print("School is not an integer")
        return False
    finally:
        return True
