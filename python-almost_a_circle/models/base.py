#!/usr/bin/python3
"""Module Base"""
import json


class Base:
    """Attributes of the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that inicilizate the objects"""
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = value

    def to_json_string(list_dictionaries):
        """This method return the json string of the object"""
        return json.dumps(list_dictionaries)
