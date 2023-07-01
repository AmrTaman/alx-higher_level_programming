#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    sum = [0, 0]
    length = 2
    if (length > len(tuple_a)):
        length = len(tuple_a)
    for x in range(length):
        a[x] = tuple_a[x]
    length = 2
    if (length > len(tuple_b)):
        length = len(tuple_b)
    for x in range(length):
        b[x] = tuple_b[x]
    sum[0] = a[0] + b[0]
    sum[1] = a[1] + b[1]

    return (sum[0], sum[1])
