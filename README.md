# Packing zoom tiles

## Problem

When on a zoom call, as users join, it changes the amount of unused space.

This got me thinking, what's the optimal efficiency for packing in n tiles of videos onto the screen?

## Assumptions

1. First pass, we'll assume (incorrectly) that the screen and all tiles are square. This makes it simpler to reason about.
1. [Square packing in a square](https://en.wikipedia.org/wiki/Square_packing_in_a_square) make it seem like this problem is unsolved if you allow for angled squares. We want all the squares to be straight up and down.
1. Given the above, we're going to assume the most efficient packing is a "regular" one, where there are even rows and columns, potentially missing spot.
    1. Given that the squares have to be straight up and down, I think this assumption is true, but I haven't proved it yet
    2. This seems obvious, however the analogous result in [Sphere Packing](https://en.wikipedia.org/wiki/Kepler_conjecture) wasn't shown until 1998, it might not be :)
    
## Algorithm

1. Find all the smallest row by column arrangements
1. Of the above, determine the most efficient

## Results

As you can see in `results/results.txt`, it looks like the the best packing is the square one, just with entries missing.

Given this, see `lib/solve2.py`, essentially `n / nextPerfectSquare(n)` where `nextPerfectSquare` returns the smallest number >=n that is a perfect square.

This stands to reason, in that the ratio will be how far off you are from being a perfect square.

## Next steps

1. Does the regularity assumption hold?
    1. Can we prove that efficient packings don't for example misalign the squares?
1. Is there a straightforward extension to rectangles (which is closer to the original question)
