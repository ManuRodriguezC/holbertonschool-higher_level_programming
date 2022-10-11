#!/usr/bin/python3
"""This method check if object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Function that return True if obj is instance and different class"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
