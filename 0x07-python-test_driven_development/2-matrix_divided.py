#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Args:
    matrix: List of lists containing int or float
    div: number to divide matrix by
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                "of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                    "of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for a in r:
            if not isinstance(a, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    return [[round(a / div, 2) for a in r] for r in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
