#!/usr/bin/python3
"""a class Square"""


class Square:
    """properties of square.
    """
    def __init__(self, size=0):
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
