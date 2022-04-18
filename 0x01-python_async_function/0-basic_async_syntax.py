#!/usr/bin/python3

"""
Module contains function that demonstrates async
"""

import asyncio
import random


async def wait_random(maxdelay=10):
    """
    This function generates a random time in seconds
    and returns the value after waiting for the supposed time
    """
    rand_value = random.uniform(0, maxdelay)
    await asyncio.sleep(rand_value)
    return rand_value