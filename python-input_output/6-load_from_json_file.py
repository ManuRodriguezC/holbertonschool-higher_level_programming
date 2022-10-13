#!/usr/bin/python3
"""Module: json"""
import json


def load_from_json_file(filename):
    """This method create the object of the string in the file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())
