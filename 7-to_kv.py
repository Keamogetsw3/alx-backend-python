#!/usr/bin/env python3
"""
This module defines a type-annotated function `to_kv` that takes a string 
and a numerical value (integer or float) and returns a tuple. 

The first element of the tuple is the input string, and the second element 
is the square of the numerical value, returned as a float.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string and the second 
    element is the square of a given number (converted to float).

    Parameters:
    k (str): The key, represented as a string.
    v (Union[int, float]): A numerical value (integer or float).

    Returns:
    Tuple[str, float]: A tuple containing the input string and the square 
    of the number as a float.
    """
    return (k, float(v ** 2))
