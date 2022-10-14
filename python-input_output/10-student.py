#!/usr/bin/python3
"""Module Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """This method inicializate the atribbutes of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method return a json representation of a class"""
        if attrs is not None:
            return ({item: self.__dict__[item] for item
                     in attrs if item in self.__dict__})
        return self.__dict__
