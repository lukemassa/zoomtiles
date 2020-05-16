# Packing zoom tiles

## Problem

When on a zoom call, as users join, it changes the amount of unused space.

This got me thinking, what's the optimal efficiency for packing in n tiles of videos onto the screen?

## Assumptions

1. First pass, we'll assume (incorrectly) that the screen and all tiles are square. This makes it simpler to reason about.
1. [Square packing in a square](https://en.wikipedia.org/wiki/Square_packing_in_a_square) make it seem like this problem is unsolved if you allow for angled squares. We want all the squares to be straight up and down.
1. Given the above, we're going to assume the most efficient packing is a "regular" one, where there are even rows and columns, potentially missing spot.
    1. Given that the squares have to be straight up and down, I think this assumption is true, but I haven't proved it yet
    
## Algorithm

1. Find all the smallest row by column arrangements
1. Of the above, determine the most efficient

## Results

Results of the first 1000 runs are in results/results.txt
Looking at them, 
