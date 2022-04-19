#!/usr/bin/env python3
"""
This module measures execution time for
async operations spawned in wait_n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This functions returns time it takes to run
    n async operations in wait_b

        Args: n -> this is number of async operations
                    spawned in wait_n
              max_delay: this is the maximum time operation
                    would take in wait_n
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time: float = time.time()
    return (stop_time - start_time) / n
