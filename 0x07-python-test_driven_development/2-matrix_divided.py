#!/usr/bin/python3
"""
divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    for i in matrix:
        m = ("matrix must be a matrix (list of lists) of integers/floats")
        if not (isinstance(x, (float, int)) for x in matrix):
            raise TypeError(m)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for i in matrix:
        result.append([round(x / div, 2) for x in i])

    return result
