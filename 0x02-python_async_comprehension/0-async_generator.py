#!/usr/bin/env python3
"""
An asynchronous generator that yields random floating-point numbers.

This script defines an asynchronous generator function that yields random
floating-point numbers between 0 and 10, with a 1-second interval between
each yield.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random floating-point numbers.

    Yields:
        float: A random floating-point number between 0 and 10.

    This function asynchronously waits for 1 second before yielding each
    random number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
