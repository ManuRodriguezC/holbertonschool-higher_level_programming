#!/usr/bin/python3
"""Method that contain the Base-Geometry class"""


class BaseGeometry:
    """BaseGometry class"""
    def area(self):
        """Return the area of error if area is not implement"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This methos check if value is integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
