#!/usr/bin/env python3

"""
Module to demonstrate asynchronous comprehension using an async generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects float values from an async generator into a list.

    Returns:
        List[float]: A list of float values generated asynchronously.
    """
    return [i async for i in async_generator()]
