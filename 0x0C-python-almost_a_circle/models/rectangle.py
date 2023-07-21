#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base


class Rectangle(Base):
    """I am class Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """I am init method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """I am the setter and getter."""
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        """I am the setter and getter."""
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def x(self):
        """I am the setter and getter."""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """I am the setter and getter."""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
