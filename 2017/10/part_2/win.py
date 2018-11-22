#!/usr/bin/env python

current_position = 0
skip_size = 0

with open("input","r") as f:
    lengths = f.read().strip()

    # Convert from ascii to int
    lengths = [ord(c) for c in lengths]

    # Add the ending they want
    lengths += [17, 31, 73, 47, 23]

my_list = list(range(256))

def get_length_wrap(length):
    """Returns a new list from the current list and index, wrapping around if need be."""
    return [my_list[i%256] for i in range(current_position, current_position+length)]

def write_wrap(new_list):
    """Writes new_list onto existing list, wrapping around if need be."""
    global my_list
    
    for i, c in enumerate(new_list):
        my_list[(current_position+i)%256] = c

# Do this 64 times
for _ in range(64):

    # Loop through our lengths
    for l in lengths:
        new_list = get_length_wrap(l)[::-1]
        
        if new_list != []:
            write_wrap(new_list)

        current_position += l + skip_size
        current_position %= 256
        skip_size += 1

dense = []

for i in range(0, len(my_list), 16):
    tmp = 0
    for j in range(16):
        tmp ^= my_list[i+j]
    dense.append(tmp)

dense_hex_hash = ''.join(['{0:02x}'.format(i) for i in dense])
print(dense_hex_hash)
