#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represent a class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the data"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get/set the current height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Gets Area"""
        return (self.__width * self.height)

    def perimeter(self):
        """Gets Perimeter"""
        if (self.__width == 0) or (self.height == 0):
            return 0
        return ((self.height + self.__width) * 2)

    def __repr__(self):
        """repr"""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __str__(self):
        """Sets the str"""
        m = ""
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        for i in range(self.__height):
            for x in range(self.__width):
                m += str(self.print_symbol)
            if i != self.__height - 1 and x:
                m += "\n"
        return (m)

    def __del__(self):
        """delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger"""
        if (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area > rect_2.area or rect_1.area == rect_2.area:
            return (rect_1)
        else:
            return (rect_2)
