#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for lst in matrix:
        new.append([elem**2 for elem in lst])
    return (new)
