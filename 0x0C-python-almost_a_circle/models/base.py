#!/usr/bin/python3
"""Iam the module"""


class Base:
  """This is class base"""

  __nb_objects = 0
  def __init__(self, id=None):
    """Iam method init"""

    if id != None :
      self.id = id
    else :
      __nb_objects += 1
      self.id = __nb_objects
