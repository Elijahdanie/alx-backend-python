#!/usr/bin/env python3
"""
This module demonstrates concurrent coroutines
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    This function spawns n numbers of coroutines and
    returns a list of the time taken for each routine
    in an ascending order
    """
    final_list: list = []
    for index in range(n):
        return_val: float = await wait_random(max_delay)
        final_list.append(return_val)
    return final_list
