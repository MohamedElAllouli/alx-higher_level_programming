#!/usr/bin/python3
"""a class Square"""


class Square:
    """properties of square.
    Atrubute:
    size: size of square
    """
    def __init__(self, size=0):
        """creat new instance
        Args:
        size: size of square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def size(self):
        return self.__size

    def def size(self, value):
        self.__size = value
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
