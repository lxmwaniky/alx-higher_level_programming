#!/usr/bin/python3

"""
A function module that prints a square with the character '#'
"""


def print_square(size):
    """
    Prints square with the symbol '#'.

    Args:
        size: The size of the square.

    Raises:
        TypeError: When the value is less than zero or is not an integer.
        err: Raised when all other errors not checked.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    try:
        size = int(size)
    except Exception as err:
        raise err
    else:
        for _ in range(size):
            print("#" * size)
