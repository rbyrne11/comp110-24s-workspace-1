"""Mutating functions."""

__author__ = "730410363"

def manual_append(word: list[int], num: int) -> None:
   """Adding to end of list."""
   word.append(num)
  

def double(num_1: list[int]) -> None:
   """Multiply parameter by 2."""
   idx=0
   while idx < len(num_1):
     num_1[idx] *= 2
     idx += 1

   

