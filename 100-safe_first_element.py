#!/usr/bin/env python3
"""
This module defines a function `safe_first_element` that returns the first 
element of a sequence if it exists, or None if the sequence is empty. The 
function uses duck typing with annotations to handle sequences of any type.
"""

from typing import Sequence, Union, Any

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence, or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple, or other iterable) 
    of elements with unknown types.

    Returns:
    Union[Any, None]: The first element of the sequence, or None if the 
    sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
