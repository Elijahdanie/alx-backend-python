#!/usr/bin/env python3
"""
This module demonstrate floor rounding up
of a float paramater expressed with
type annotations
"""


def floor(n: float) -> int:
    """
    Returns the floor of n
    """
    return int(n) if n >= 0 else int(n) - 1
