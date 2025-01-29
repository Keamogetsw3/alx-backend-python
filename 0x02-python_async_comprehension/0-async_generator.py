#!/usr/bin/env python3
'''Module for asynchronous number generation.

This module defines an asynchronous generator that yields random
floating-point numbers between 0 and 10,
with a delay of 1 second between each value.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Asynchronously generates a sequence of 10 random numbers.

    This coroutine yields 10 random floating-point numbers between 0 and 10,
    pausing for 1 second between each yield.

    Yields:
        float: A random floating-point number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
