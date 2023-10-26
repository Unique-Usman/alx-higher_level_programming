#!/usr/bin/python3
"""Divides all the element of a matrix"""


def matrix_divided(matrix, div):
    """divide each element of the matrix

    each element of the matrix must be int of float
    it raises TypeError if any element of the matrix
    is not int of float, the list insde of the list
    must have the same number also

    Args:
        matrix (list): the list
        div (int): divisor
    Raises:
        TypeError: Element must be int of float
        ZeroDivisionError: div must not be zero
    Returns:
        list: new list containing division
    """

    if not matrix or len(matrix) == 0 or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    for i in matrix:
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = []

    for i in range(len(matrix)):
        rest = []
        for j in range(size):
            rest.append(round(matrix[i][j] / div, 2))
        res.append(rest)

    return res
