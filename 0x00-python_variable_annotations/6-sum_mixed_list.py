#!/usr/bin/env python3
"""
A module that provides a function to sum a list containing both integers
and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats
                                           to be summed.

    Returns:
        float: The sum of the elements in the list as a float.
    """
    return sum(mxd_lst)
