#!/usr/bin/env python3
'''Module for measuring the execution time of multiple asynchronous tasks.

This module defines a function that runs `async_comprehension` four times 
concurrently and measures the total execution time for all executions.
'''

import asyncio
import time
from importlib import import_module as using

# Importing async_comprehension from the previous module
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total execution time for 4 concurrent executions of `async_comprehension`.

    This function runs `async_comprehension()` four times concurrently using `asyncio.gather()`, 
    and measures the total time taken to complete all executions.

    Returns:
        float: The total time (in seconds) taken for all 4 executions.
    '''
    start_time = time.time()
    # Run async_comprehension 4 times concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
