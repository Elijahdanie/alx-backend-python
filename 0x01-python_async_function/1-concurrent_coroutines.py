#!/usr/bin/env python3
"""
This module demonstrates concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function spawns n numbers of coroutines and
    returns a list of the time taken for each routine
    in an ascending order
    """

    final_list: List[float] = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(final_list)
