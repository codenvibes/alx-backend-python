#!/usr/bin/env python3
"""
This script defines an asynchronous function `wait_n` that executes a specified
number of coroutines concurrently and returns a list of their execution delays
in ascending order.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Execute `n` instances of `wait_random` with a maximum delay of `max_delay`
    and return a list of their delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
