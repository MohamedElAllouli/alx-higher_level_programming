#!/usr/bin/python3
"""" class geometry """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            ValueError("<name> must be greater than 0")
