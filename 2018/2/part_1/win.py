#!/usr/bin/env python

import string

with open("../input","r") as f:
    inp = f.read()

def do_count(s):
    # Running totals
    global num_two, num_three
    counts = {}

    # Init the count
    for c in string.ascii_lowercase:
        counts[c] = 0

    # Count them up
    for c in s:
        counts[c] += 1

    # Update totals
    if len([c for c,val in counts.items() if val == 2]) > 0:
        num_two += 1

    if len([c for c,val in counts.items() if val == 3]) > 0:
        num_three += 1


num_two = 0
num_three = 0

inp = inp.strip().split("\n")

for i in inp:
    do_count(i)

print("Checksum: " + str(num_two * num_three))

