#!/usr/bin/env python

current_position = 0
skip_size = 0

with open("input","r") as f:
    lengths = f.read().strip().split(",")
    lengths = [int(x) for x in lengths]

my_list = list(range(256))

def get_length_wrap(length):
    """Returns a new list from the current list and index, wrapping around if need be."""
    return [my_list[i%256] for i in range(current_position, current_position+length)]

def write_wrap(new_list):
    """Writes new_list onto existing list, wrapping around if need be."""
    global my_list
    
    for i, c in enumerate(new_list):
        my_list[(current_position+i)%256] = c

# Loop through our lengths
for l in lengths:
    new_list = get_length_wrap(l)[::-1]
    
    if new_list != []:
        write_wrap(new_list)

    current_position += l + skip_size
    current_position %= 256
    skip_size += 1

print("Part 1: " + str(my_list[0] * my_list[1]))

