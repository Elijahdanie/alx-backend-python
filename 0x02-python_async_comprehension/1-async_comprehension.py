#!/usr/bin/env python3
"""
This module demonstrates async comprehension
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """
    This function returns a list of 10 randome
    numbers gotten from async_generator
    """
    return [i async for i in async_generator()]
