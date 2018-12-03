#!/usr/bin/env python

import string
import itertools

with open("../input","r") as f:
    inp = f.read()

def off_by_one(s1, s2):
    """bool: Are s1 and s2 off by exactly one character?"""
    off_by = 0

    for c1, c2 in zip(s1,s2):
        # Early exit
        if off_by > 1:
            return False

        if c1 != c2:
            off_by += 1
    
    return off_by == 1


inp = inp.strip().split("\n")

# Get the first solution
winner = next((x,y) for x,y in itertools.combinations(inp, 2) if off_by_one(x,y))

# Rebuild the string that matches
solution = ''.join(c1 for c1,c2 in zip(winner[0], winner[1]) if c1 == c2) 

print("Solution: " + solution)
