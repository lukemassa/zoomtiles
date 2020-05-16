#!/usr/bin/env python3

"""
Given a number n, how efficiently can the largest possible squares of n size fit into the unit square?
"""
import argparse
import math
import fractions

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
    return n / float(area), (n, area)

def get_ratio_as_fraction(x, y):
    return str(fractions.Fraction(x, y))


def solve(n, as_fraction=False):
    max_efficiency = 0
    max_ratio = (0, 0)
    for x, y in possible_dimensions(n):
        efficiency, ratio = get_efficiency(n, x, y)
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            max_ratio = ratio
    if as_fraction:
        # I first thought I wanted this reduced, but now I'm not sure
        return "%s/%s" % (max_ratio)
        # return get_ratio_as_fraction(max_ratio[0], max_ratio[1])
    return max_efficiency
