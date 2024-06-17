#!/usr/bin/env python3
"""
This script contains a function to safely retrieve the first element of a
sequence. If the sequence is empty, the function returns None.
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists, otherwise returns
    None.

    Parameters:
    lst (Sequence[Any]): The sequence from which to retrieve the first
    element.

    Returns:
    Union[Any, None]: The first element of the sequence if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
