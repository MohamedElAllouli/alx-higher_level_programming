#!/usr/bin/python3
"""" class Rectangle """


class Rectangle(BaseGeometry):
    """ class Rectangle """
    def __int__(self, width, height):
        super.integer_validator(self, width, "width")
        super.integer_validator(self, height, "height")
        self.__width = width
        self.__height = height
