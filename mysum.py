#!/usr/bin/env python3

from typing import List, Tuple, Union, Sequence


def mysum(numbers: Union[List[int], Tuple[int]]):
    total = 0
    for one_number in numbers:
        total += one_number
    return total


print(mysum([10, 20, 30]))
print(mysum((10, 20, 30)))
print(mysum([10, 'abc', 30]))
