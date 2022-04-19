#!/usr/bin/env python3
"""
This module returns a list of task
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    This function returns list of tasks
    that returns time for running async
    operations.
    """
    final_list: List[asyncio.Task] = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)])
    return sorted(final_list)
