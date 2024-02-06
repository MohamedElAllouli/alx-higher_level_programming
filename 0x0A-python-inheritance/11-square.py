#!/usr/bin/python3
"""" class Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class 9-rectangle.py """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self__size, self__size)
