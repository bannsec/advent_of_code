#!/usr/bin/env python

with open("../input","r") as f:
    inp = f.read()

inp = inp.strip().split("\n")
inp = [int(x) for x in inp]

# Sets are fast for identifying if elements exist
totals = set([0])
last_total = 0

# Since we may have to loop the input, wrap it forever
while True:

    # For each input int
    for i in inp:

        # Update the total
        new_total = last_total + i

        # Check if we've seen this before
        if new_total in totals:
            print("Found: " + str(new_total))
            break
        else:
            # Haven't seen it, update our set
            totals.add(new_total)
            last_total = new_total
    else:
        continue
    break
