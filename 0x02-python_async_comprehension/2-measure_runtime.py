#!/usr/bin/env python3
"""
This module measures time for running
async_comprehension
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function computes the time taken
    to run async_comprehension over 4 iterations
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = time.time()
    return end_time - start_time
