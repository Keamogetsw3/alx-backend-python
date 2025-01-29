#!/usr/bin/env python3
'''Module for measuring execution time of asynchronous tasks.

This module defines a function to compute the average execution time 
of `wait_n`, which runs multiple asynchronous delays concurrently.
'''

import asyncio
import time

# Importing wait_n from the previous module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the average execution time of `wait_n`.

    This function records the start time, executes `wait_n(n, max_delay)`,
    and computes the average time taken per function call.

    Args:
        n (int): The number of times to call `wait_random` concurrently.
        max_delay (int): The maximum possible delay for each `wait_random` call.

    Returns:
        float: The average execution time per function call.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
