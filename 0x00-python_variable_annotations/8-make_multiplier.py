#!/usr/bin/env python3
"""
This module provides a function to create multiplier functions.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that multiplies its input by a specified
    multiplier.

    Args:
        multiplier (float): The value by which the input of the returned
        function will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier specified in the outer
        function.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the
            multiplier.
        """
        return value * multiplier
    return multiplier_function
