#!/usr/bin/env python3

"""
Module contains function that demonstrates async
"""

import asyncio
import random


async def wait_random(maxdelay: int = 10) -> float:
    """`
    This function generates a random time in seconds
    and returns the value after waiting for the supposed time
    """
    rand_value: float = random.uniform(0, float(maxdelay))
    await asyncio.sleep(rand_value)
    return rand_value
