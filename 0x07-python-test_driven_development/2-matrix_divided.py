#!/usr/bin/python3

"""
A module with for dividing all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides elements of the matrix.

    Arguments:
        matrix: The matrix to divide.
        div: The divisor.

    Returns:
        list: A matrix with all elements divided with the divisor.

    Raises:
        TypeError: When correct argument is not passed or
	when the size of any row in the row is inconsistent 
	with the others.
        ZeroDivision: When the divisor is zero.
    """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for i, row in enumerate(matrix):
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if i > 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    return list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix)
    )
