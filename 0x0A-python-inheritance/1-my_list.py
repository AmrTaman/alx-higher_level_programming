#!/usr/bin/python3
"""Module"""


class Mylist(list):
    """Class inherits the list class"""
    pass

    def print_sorted(self):
        """method for sorting a list"""

        print(sorted(list(self)))