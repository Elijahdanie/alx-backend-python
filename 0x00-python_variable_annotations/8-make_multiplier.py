#!/usr/bin/env python3
"""
this module demonstrates the manipulation
of complex types
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float.
    """
    return lambda x: x * multiplier
