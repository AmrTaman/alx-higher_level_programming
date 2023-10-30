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

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return(a + b)
