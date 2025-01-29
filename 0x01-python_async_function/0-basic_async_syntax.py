#!/usr/bin/env python3
'''Module for asynchronous delay handling.

This module defines an asynchronous
function that waits for a random delay
between 0 and a given maximum number of
seconds before returning the actual delay time.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronously waits for a random duration and returns the wait time.

    The function generates a random floating-point 
    number between 0 and `max_delay`,
    then awaits for that duration before returning the value.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait.
        Defaults to 10.
    Returns:
        float: The actual time waited.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
