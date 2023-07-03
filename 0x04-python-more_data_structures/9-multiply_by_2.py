#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dic = {}
    if a_dictionary:
        for k in a_dictionary:
            dic[k] = a_dictionary[k] * 2
    return (dic)
