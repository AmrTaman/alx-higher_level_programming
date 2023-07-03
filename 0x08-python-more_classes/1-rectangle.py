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
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
