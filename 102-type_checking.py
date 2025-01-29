#!/usr/bin/env python3
"""
This module defines a function `zoom_array` that takes a tuple and an optional 
factor to expand its elements into a list, repeated by the factor value.
The code is validated using `mypy` to ensure type correctness.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Expand the elements of a tuple into a list, each repeated by the given 
    factor. The default factor is 2.

    Parameters:
    lst (Tuple[int, ...]): A tuple of integers.
    factor (int): The number of times each element should be repeated 
    (default is 2).

    Returns:
    List[int]: A list where each element from the tuple is repeated 
    by the specified factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
