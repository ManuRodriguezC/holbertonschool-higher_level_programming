#!/usr/bin/python3
"""Module:write"""


def write_file(filename="", text=""):
    """This method write a text in a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
