#!/usr/bin/python3
"""This function return True if obj is same a_class if not return False"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
