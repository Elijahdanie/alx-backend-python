#!/usr/bin/env python3
"""
This module demonstates the computation
of a union type list of ints and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function returns the sum of the
    union type list
    """
    return sum(mxd_list)
