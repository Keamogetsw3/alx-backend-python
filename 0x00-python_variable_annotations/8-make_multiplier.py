#!/usr/bin/env python3
"""
This module defines a type-annotated function `make_multiplier` that takes a
floating-point number as an argument and returns a function.

The returned function takes a float as input and multiplies it by the
original multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given float by a specified multiplier.

    Parameters:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """ Multiplies the input value by the predefined multiplier. """
        return value * multiplier

    return multiplier_function
