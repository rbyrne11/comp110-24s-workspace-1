"""Summing the elements of a list usign different loops."""

__author__ = "730410363"


def w_sum(vals: list[float]) -> float: 
    """Sum."""
    total = 0.0 
    idx = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1 
    return total 


def f_sum(vals: list[float]) -> float: 
    """For in loop sum."""
    total = 0.0
    for elem in vals: 
        total += elem 
    return total 


def f_range_sum(vals: list[float]) -> float:
    """Using range for sum."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total 