#!/usr/bin/python3

"""
This module gets the sum of two arguments that must be integers
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b

    Arguments:
    	a: first number
	b: second number(Default value of 98)

    Raises:
    	TypeError: When Operands given are not valid -> Integers
    
    Returns:
    	int: Sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    try:
       int(a)
       int(b)
    except Exception as e:
       raise e

    return int(a) + int(b)
