#!/usr/bin/env python3
"""
A module to provide asynchronous waiting functionality with a random delay.
"""
import random


async def wait_random(max_delay: int = 10):
    """
    Asynchronously wait for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10 seconds.

    Returns:
        float: The actual random delay in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    return random_delay
