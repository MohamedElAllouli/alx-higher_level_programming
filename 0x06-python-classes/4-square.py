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

    def area(self):
        """Returns the size of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def def size(self, value):
        """Property setter for size.
        Args:
        alue (int): size of a square (1 side).
        Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        """
        self.__size = value
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
