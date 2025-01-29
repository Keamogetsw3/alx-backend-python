#!/usr/bin/env python3
'''Module for executing multiple asynchronous delays.

This module defines a function that runs multiple instances of `wait_random`
concurrently and returns their wait times in ascending order.
'''

import asyncio
from typing import List

# Importing wait_random from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs `wait_random` concurrently `n` times and returns sorted wait times.

    This function concurrently executes `wait_random` `n` times with the specified
    `max_delay` and collects the results. The wait times are then sorted in 
    ascending order.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum possible delay for each `wait_random` call.

    Returns:
        List[float]: A list of wait times in ascending order.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
