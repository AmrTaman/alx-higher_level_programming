#!/usr/bin/python3
"""

Module
this module contains a function
that adds two integer (add_integer)

"""


def add_integer(a, b=98):
    """

    add_ingteger function
    adds two integers
    returns an integr

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
