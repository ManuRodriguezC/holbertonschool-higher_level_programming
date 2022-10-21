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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method return the json string of the object"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of file"""
        if list_objs is None or list_objs == []:
            file = "[]"
        else:
            file = cls.to_json_string([x.to_dictionary() for x in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as fi:
            fi.write(file)

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the
        JSON string representation json_string
        """
        new_list = []
        if json_string is None:
            return new_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Retrurn a instance with all atributes already set"""
        new_instance = cls(**dictionary)
        new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances:"""
        list_instance = []
        try:
            with open(f"{cls.__name__}.json", "r", encoding='utf-8') as file:
                dictionary = cls.from_json_string(file.read())
                for element in dictionary:
                    list_instance.append(cls.create(**element))
                return list_instance
        except FileNotFoundError:
            return list_instance
