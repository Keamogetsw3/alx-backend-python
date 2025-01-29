#!/usr/bin/env python3
"""
This module defines a function `safely_get_value` that safely retrieves 
a value from a dictionary. If the key is not found, it returns a default 
value instead.
"""

from typing import Mapping, Any, Union, TypeVar

# Type variable to handle any type for default value
T = TypeVar('T')

def safely_get_value(
        dct: Mapping[Any, Any], key: Any,
        default: Union[T, None]) -> Union[Any, T]:
    """
    Retrieve the value for a given key from a dictionary. If the key is not 
    found, return the provided default value.

    Parameters:
    dct (Mapping[Any, Any]): A dictionary with keys and values of any type.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None]): The value to return if the key is not found. 
    Can be any type (specified by T) or None.

    Returns:
    Union[Any, T]: The value corresponding to the key if found, 
    or the default value (which can be any type or None) if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
