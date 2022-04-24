#!/usr/bin/env python3
"""
This module expresses iterables
and tuples using type annotation
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This returns the contents of the iterable and their
    length
    """
    return [(i, len(i)) for i in lst]
