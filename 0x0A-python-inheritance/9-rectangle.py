#!/usr/bin/python3
"""" class Rectangle """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
