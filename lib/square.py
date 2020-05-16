#!/usr/bin/env python3

"""
Given a number n, how efficiently can the largest possible squares of n size fit into the unit square?
"""
import argparse
import math
from fractions import Fraction

def possible_dimensions(n):
    # This is a special case just because
    # the below algorithm would duplicate (2, 1)
    if n == 2:
        yield (1, 2)
        return
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        j = int(math.ceil(n / float(i)))
        yield i, j


def get_efficiency(n, x, y):
    edge = max(x, y)
    area = edge * edge
    if n > area:
        raise AssertionError("%d > %d * %d, cannot fit tiles!" % (n, x, y))
    return Fraction(n, area)

def solve(n):
    max_efficiency = Fraction(0, 1)
    for x, y in possible_dimensions(n):
        efficiency = get_efficiency(n, x, y)
        if efficiency > max_efficiency:
            max_efficiency = efficiency
    return max_efficiency
