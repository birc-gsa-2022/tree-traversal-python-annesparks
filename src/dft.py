"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T
from collections import deque

# Recursion practice
# def in_order(t: T | None) -> Iterable[int]:
#     """In-order traversal of a tree.

#     >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
#     >>> list(in_order(tree))
#     [1, 2, 3, 4, 5]
#     """
#     if not t:
#         return
    
#     yield from in_order(t.left)
#     yield t.val
#     yield from in_order(t.right)

def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    d = deque()
    while t or d:
        if t:
            d.append(t)
            t = t.left
        elif d:
            t = d.pop()
            yield t.val
            t = t.right