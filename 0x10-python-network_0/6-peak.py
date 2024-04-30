#!/usr/bin/python3
"""
qasaa
"""


def find_peak(list_of_integers):
    """
    ssssss
    """
    peak = 0
    for i in range(len(list_of_integers)):
        if i == 0 and list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
        if i != len(list_of_integers) - 1 and list_of_integers[i] < list_of_integers[i + 1]  :
            peak = list_of_integers[i + 1]
            if list_of_integers[i + 1] > list_of_integers[i + 2]:
                return peak
        if i != len(list_of_integers) - 1 and list_of_integers[i] > list_of_integers[i + 1] :
            peak = list_of_integers[i + 1]
            if list_of_integers[i + 1] < list_of_integers[i + 2]:
                return peak
        if i == len(list_of_integers) - 1:
            return list_of_integers[i]
    return
