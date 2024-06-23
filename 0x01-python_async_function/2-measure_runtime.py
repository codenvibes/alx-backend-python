#!/usr/bin/env python3
"""
This module defines a function to measure the execution time
of an asynchronous coroutine and calculates the average time per coroutine.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running `wait_n` and calculates
    the average time per coroutine.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """
    current_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - current_time
    return (elapsed_time) / n
