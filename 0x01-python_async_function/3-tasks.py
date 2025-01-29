#!/usr/bin/env python3
'''Module for creating an asynchronous task.

This module defines a function that creates and returns an asyncio Task
for executing `wait_random` asynchronously.
'''

import asyncio

# Importing wait_random from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asyncio Task for `wait_random`.

    This function wraps `wait_random(max_delay)` inside an `asyncio.Task`,
    which allows it to run concurrently with other asynchronous tasks.

    Args:
        max_delay (int): The maximum delay for the `wait_random` coroutine.

    Returns:
        A task object representing the execution of `wait_random`.
    '''
    return asyncio.create_task(wait_random(max_delay))
