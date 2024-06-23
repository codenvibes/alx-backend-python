#!/usr/bin/env python3
"""
An async function `wait_n` to run multiple coroutines concurrently and return
sorted execution delays.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute `n` instances of `wait_random` with a maximum delay of `max_delay`
    and return a list of their delays in ascending order.
    """
    list_of_delays = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(list_of_delays)
