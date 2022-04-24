#!/usr/bin/env python3
"""
This module expresses Duck typing
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns first element of the sequence
    """
    if lst:
        return lst[0]
    else:
        return None
