"""Utility functions within lists."""

__author__: str = "730410363"


def all(num: list[int], match: int) -> bool:
    """Check for a match."""
    idx = 0
    if len(num) == 0:
        return False
    
    while len(num) > idx: 
        if num[idx] != match:
            return False
        idx += 1

    return True


def max(numbers: list[int]) -> int:
    """Determine max from the given list."""
    if len(numbers) == 0:
        raise ValueError("max () arg is an empty list")
    max_num = numbers[0]
    idx = 1
    while idx < len(numbers):
        if numbers[idx] > max_num: 
            max_num = numbers[idx]
        idx += 1
    
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determine if length of lists are equal."""
    if len(list1) != len(list2):
        return False
    
    while len(list1):
        if list1.pop() != list2.pop():
            return False
    
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Adding list 2 elements to list 1."""
    idx = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1