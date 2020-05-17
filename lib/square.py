
import math
from fractions import Fraction

def get_next_perfect_square(n):
    x = int(math.ceil(math.sqrt(n)))
    return x * x

def solve(n):
    return Fraction(n, get_next_perfect_square(n))
