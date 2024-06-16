#!/usr/bin/env python3
"""
This script defines a function to sum the elements of a list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in a list.

    Args:
        input_list (list of floats): A list of floating point numbers.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
