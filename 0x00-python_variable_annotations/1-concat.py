#!/usr/bin/env python3
"""
This module defines a type-annotated function `concat` that takes two string 
arguments and returns their concatenated result.
"""

def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated string.
    """
    return str1 + str2
