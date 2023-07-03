#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represent a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data"""

        self.height = height
        self.width = width

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
    def __repr(self):
      """repr"""
      return "Rectangle("+ str(self.__width) + ", " + str(self.__length) + ")"  
    def __str__(self):
        """Sets the str"""
        m = ""
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        for i in range(self.__height):
            for x in range(self.__width):
                m += "#"
            if i != self.__height - 1 and x:
                m += "\n"
        return (m)
