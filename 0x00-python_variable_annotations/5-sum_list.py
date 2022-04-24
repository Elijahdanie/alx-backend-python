#!/usr/bin/env python3
"""
This module demonstates the summation
of a list of floats expressed with
type annotation
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function returns the sum
    of a list of floats.
    """
    return sum(input_list)
