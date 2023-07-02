#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    lst = []
    for elem in my_list:
        if elem not in lst:
            sum += elem
        lst.append(elem)
    return sum
