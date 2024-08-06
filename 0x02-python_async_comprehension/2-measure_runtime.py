#!/usr/bin/env python3
"""
This script defines an asynchronous function to measure the runtime of
multiple calls to `async_comprehension`.

Imports:
    - asyncio: For asynchronous programming.
    - time: For measuring execution time.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing the `async_comprehension` function
    four times concurrently using asyncio.gather.

    Returns:
        float: The total time in seconds taken to complete all the async
        operations.
    """
    time_started = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - time_started
