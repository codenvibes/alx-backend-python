#!/usr/bin/env python3
"""
This script demonstrates asynchronous task creation using asyncio in Python.
It defines a function `task_wait_random` that wraps around an asynchronous
function `wait_random`.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task that asynchronously executes the `wait_random`
    function.

    Args:
        max_delay (int): Maximum delay value for `wait_random`.

    Returns:
        asyncio.Task: An asyncio task object representing the execution of
        `wait_random(max_delay)`.
    """
    return asyncio.create_task(wait_random(max_delay))
