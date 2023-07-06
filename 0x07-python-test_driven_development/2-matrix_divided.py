#!/usr/bin/python3
"""
divides all elements of a matrix
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    result = []
    msg_0 = "div must be a number"
    msg_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    msg_2 = 'Each row of the matrix must have the same size'
    first_row = matrix[0]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(msg_1)
    if not isinstance(div, int):
        raise TypeError(msg_0)
    for i in matrix:
        if len(i) == len(first_row):
            continue
        else:
            raise TypeError(msg_2)
    for i in matrix:
        for x in i:
            if not isinstance(x, (float, int)):
                raise TypeError(msg_1)
        else:
            result.append([round((x / div), 2) for x in i])

    return result
