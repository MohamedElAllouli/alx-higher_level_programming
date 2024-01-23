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
            raise print("size must be an integer")
        elif size < 0:
            raise print("size must be >= 0")
