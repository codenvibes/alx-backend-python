#!/usr/bin/env python3
"""
This module contains a function to calculate the length of elements in an
iterable of sequences.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples where each
    tuple contains a sequence and its corresponding length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequence elements (like
    list, tuple, string).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence
    from the input and its length.
    """
    return [(i, len(i)) for i in lst]
