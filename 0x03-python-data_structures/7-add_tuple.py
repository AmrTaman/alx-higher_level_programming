#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    sum = [0, 0]
    for x in range(len(tuple_a)):
        a[x] = tuple_a[x]
    for x in range(len(tuple_b)):
        b[x] = tuple_b[x]
    sum[0] = a[0] + b[0]
    sum[1] = a[1] + b[1]

    return (sum[0], sum[1])
