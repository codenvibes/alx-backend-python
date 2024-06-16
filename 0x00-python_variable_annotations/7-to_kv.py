#!/usr/bin/env python3
"""
This script contains a function `to_kv` that takes a string and a number,
and returns a tuple with the string and the square of the number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the given string and the square of the given
    number.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input number, which can be an integer
                               or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the input
                           string `k` and the second element is the
                           square of the input number `v`.
    """
    return k, (v ** 2)
