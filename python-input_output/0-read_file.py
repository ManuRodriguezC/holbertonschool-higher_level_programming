#!/usr/bin/python3
"""Module.read"""


def read_file(filename=""):
    """This methos open and read a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
