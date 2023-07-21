#!/usr/bin/python3
"""Iam the module rectangle"""
__import__("base.py") 


class Rectangle(Base) :
  """Iam class Rectangle"""

  def __init__(self, width, height, x=0, y=0, id=None) :
    """Iam init method"""

    super().__init__(self, id)
    self.width = width
    self.height = height
    self.x = x
    sefl.y = y
  @property
  def width(self) :
    """Iam the setter and getter"""
    return (self.__width)
  @width.setter
  def width(self, w) :
    self.__width = w
  @property
  def height(self) :
    """Iam the setter and getter"""
    return (self.__height)
  @height.setter
  def height(self, h) :
    self.__height = h
  @property
  def x(self) :
    """Iam the setter and getter"""
    return (self.__x)
  @x.setter
  def x(self, x) :
    self.__x = x
  @property
  def y(self) :
    """Iam the setter and getter"""
    return (self.__y)
  @y.setter
  def y(self, y) :
    self.__y = y
