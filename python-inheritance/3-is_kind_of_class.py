#!/usr/bin/python3
"""This module check the instance"""


def is_kind_of_class(obj, a_class):
    """This function return if obj is intance of the class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
