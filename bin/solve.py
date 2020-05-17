#!/usr/bin/env python3

"""
Given a number n, how efficiently can the largest possible squares of n size fit into the unit square?
"""
import argparse
from fractions import Fraction
import rectangle

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Number of squares to attempt to fit")
    parser.add_argument("--up-to", action="store_true", default=False, help="Show results in csv format up to n")
    args = parser.parse_args()

    if args.up_to:
        for i in range(1, args.n):
            square = rectangle.Rectangle(Fraction(1, 1))
            solution = square.solve(i)
            print("%s,%s,%s" % (i, float(solution), str(solution)))

    else:
        square = rectangle.Rectangle(Fraction(1, 1))
        solved = square.solve(args.n)
        print("Efficieny of %s tiles is %s (%s)" % (args.n, float(solved), str(solved)))


if __name__ == "__main__":
    main()
