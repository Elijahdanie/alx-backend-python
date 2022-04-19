#!/usr/bin/env python3
"""
This module demonstrates creating
an async generator
"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """
    This function yields a random
    number between 0 and 10
    10 times
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
