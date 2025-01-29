#!/usr/bin/env python3
"""
This module defines a type-annotated function `sum_list` that calculates
the sum of a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of all elements in a list of floats.

    Parameters:
    input_list (List[float]): A list containing floating-point numbers.

    Returns:
    float: The total sum of all numbers in the list.
    """
    total = 0.0
    for num in input_list:
        total += num
    return total
