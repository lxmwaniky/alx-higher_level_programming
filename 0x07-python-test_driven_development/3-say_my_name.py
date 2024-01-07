#!/usr/bin/python3

"""
This module consists of a function that prints the
first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name of a person.

    Args:
        first_name: The first name of the person.
        last_name: The person's surname. Defaults to "" or empty.

    Raises:
        TypeError: When the first name or last name is a non-string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
