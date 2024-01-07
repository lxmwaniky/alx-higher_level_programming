#!/usr/bin/python3

"""
A function module that prints text with 2 new lines after-> ., ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 lines after each of '.', '?' and ':'.

    Args:
        text: The text to parse and print.

    Raises:
        TypeError: When the argument received is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i, char in enumerate(text, start=1):
        if char in (".", "?", ":"):
            print(f"{char}\n")

        elif text[i - 2] not in (".", "?", ":") or text[i - 1] != " ":
            print(char, end="")
