#!/usr/bin/env python3
"""
This module defines a type-annotated function `sum_mixed_list` that calculates
the sum of a list containing both integers and floating-point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]):
    A list of numerical values (integers and floats).

    Returns:
    float: The total sum of all numbers in the list.
    """
    total = 0.0
    for num in mxd_lst:
        total += num
    return total
