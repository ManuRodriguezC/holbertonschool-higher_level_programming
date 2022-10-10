#!/usr/bin/python3
"""This module have a function is_same_class"""


def is_same_class(obj, a_class):
    """This function return True if obj is  a_class if not return False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
