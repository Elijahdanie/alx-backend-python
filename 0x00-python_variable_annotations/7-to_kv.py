#!/usr/bin/env python3
"""
This module demonstates type annotation
of a tuple
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns a tuple
    """
    return (k, v**2)
