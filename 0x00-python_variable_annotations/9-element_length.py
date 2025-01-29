#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterable of
sequences and returns a list of tuples, where each tuple contains a sequence
and its corresponding length.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Create a list of tuples, where each tuple contains an element from the
    input iterable and the length of that element.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences (like lists,
    strings, or other iterable types).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence
    from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
