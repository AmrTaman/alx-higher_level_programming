#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        elem = -1
        for elem in range(x):
            print("{:d}".format(my_list[elem]), end="")
        print()
        return elem + 1
    except IndexError:
        print()
        return elem
