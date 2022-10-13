#!/usr/bin/python3
"""Module: json"""
import json


def save_to_json_file(my_obj, filename):
    """Method that write to json representation in a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
