#!/usr/bin/env python3
"""
A module to provide asynchronous waiting functionality with a random delay.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10 seconds.

    Returns:
        float: The actual random delay in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
