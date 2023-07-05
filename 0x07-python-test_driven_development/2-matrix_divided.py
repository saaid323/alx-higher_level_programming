#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = []
    for i in matrix:
        result.append([round(x / div, 2) for x in i])

    return result
