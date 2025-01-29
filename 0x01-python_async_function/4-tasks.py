#!/usr/bin/env python3
'''Module for creating an asynchronous task.

This module defines a function that creates and returns an asyncio Task 
for executing `wait_random` asynchronously.
'''

import asyncio
from typing import List


# Importing wait_random from the previous module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Creates and returns an asyncio Task for `wait_random`.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
