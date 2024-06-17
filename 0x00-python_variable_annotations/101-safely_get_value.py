#!/env/bin/env python3
"""
This module provides utility functions for safely accessing values from
dictionaries.
"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] =
                     None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from the
    dictionary.

    Args:
        dct (Mapping): The dictionary or mapping-like object to retrieve the
        value from.
        key (Any): The key whose associated value is to be retrieved.
        default (Optional[T], optional): The default value to return if the
                                         key is not found in the dictionary.
                                         Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found; otherwise,
        the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
