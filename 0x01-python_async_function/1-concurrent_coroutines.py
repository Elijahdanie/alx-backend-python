#!/usr/bin/env python3

"""
Docs...
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> list:
    """
    Docs ...
    """
    final_list:list = []
    for index in range(n):
        return_val:float = await wait_random(max_delay)
        final_list.append(return_val)
    return final_list
