"""Utility Functions."""

__author__ = "730481331"


def only_evens(even_list: list[int]) -> list[int]:
    """Given a list of intergers, only the even numbers will return."""
    sequence_length: list[int] = []
    i: int = 0 
    while (i < len(even_list)):
        if even_list[i] % 2 == 0:
            sequence_length.append(even_list[i])
        i = i + 1
    return sequence_length


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Generate a subset list of the given list."""
    subset = []
    if b < 0:
        b = 0
    if c > len(a):
        c = len(a)
    if b >= len(a):
        return []
    if c <= 0:
        return []
    if len(a) == 0:
        return []
    while b < c:
        subset.append(a[b])
        b += 1
    return subset


def concat(a: list[int], b: list[int]):
    """Generate a new list with the given list."""
    new_list = a
    if a == [] and b == []:
        return a and b
    for x in b:
        new_list.append(x)
    return new_list