#!/env/bin/env python3
"""
This module provides utility functions for safely accessing values from
dictionaries.
"""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T', None, Any)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary-like object (Mapping).

    Args:
    - dct (Mapping): The dictionary or mapping object from which to retrieve the value.
    - key (Any): The key whose associated value is to be retrieved from the dictionary.
    - default (Union[Any, None]): The default value to return if the key is not found in the dictionary.

    Returns:
    - Union[Any, Any]: The value associated with the given key if found in the dictionary, 
                       otherwise returns the provided default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
