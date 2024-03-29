#!/usr/bin/python3

"""
module Shapes for efining shapes
"""


class Rectangle:
    """
    class Rectangle for defining properties of a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
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
        return (self.__height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        str = ""
        if self.width == 0 or self.height == 0:
            return (str)
        for x in range(self.height):
            for y in range(self.width):
                str += "#"
            str += "\n"
        str = str[0:len(str) - 1]
        return (str)

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        return "Rectangle({}, {})".format(self.width, self.height)
