#!/usr/bin/python3
"""a class Square"""


class Square:
    """
    Class that defines properties of square

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size: size of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @property
    def position(self):
        """ return the position value
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value: size of a square (

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Property setter for position.

        Args:
            value: size of a square (

        Raises:
            TypeError: position  must be a tuple of 2 positive integers
        """
        self.__position = value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) and n > 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ print squqre
        """
        if self.__size == 0:
            print("")
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
