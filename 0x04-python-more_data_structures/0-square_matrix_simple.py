#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    j = []
    new = []
    for i in matrix:
        new.append([x * x for x in i])
    return new
