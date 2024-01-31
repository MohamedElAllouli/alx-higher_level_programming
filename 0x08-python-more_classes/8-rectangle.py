#!/usr/bin/python3
"""empty class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle
    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        number_of_instances : public atribute
        print_symbol: public atribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width : width of rectangle. Defaults to 0.
            height: height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width retriver.
        Returns:
        int: width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """height retriver.
        Returns:
        int: the width of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        Args:
        value (int): width of the rectangle.
        Raises:
        TypeError: if width is not an integer.
        ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        setter for height of recyangle.
        value (int): height of the rectangle.
        Raises:
        TypeError: if height is not an integer.
        ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area of rectangle
        return:
        value of area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ return perimeter of rectangle
        return:
        value of perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Prints the rectangle with the character #.
        Returns:
        str: the rectangle
        """
        rec = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append(str(self.print_symbol))
            rec.append("\n")
        rec.pop()
        return "".join(rec)

    def __repr__(self):
        """
        return a string representation of the
        rectangle to be able to recreate a new instance
        return :
        str: string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance class
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """ 
        compare tow rectangle

        args:
        rect_1: first rectangle
        rect_2: second reactangle
        
        Return: 
        the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
