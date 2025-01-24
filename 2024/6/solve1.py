#!/usr/bin/env python3

import sys

def turn_right(direction):
    """
    Rotate direction 90 degrees to the right.
    Directions are in order: 0=up, 1=right, 2=down, 3=left.
    """
    return (direction + 1) % 4

def get_deltas(direction):
    """
    Return (dr, dc) for moving one step in the given direction.
    0=up, 1=right, 2=down, 3=left.
    """
    if direction == 0:  # up
        return -1, 0
    elif direction == 1:  # right
        return 0, 1
    elif direction == 2:  # down
        return 1, 0
    elif direction == 3:  # left
        return 0, -1

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <input-file>".format(sys.argv[0]))
        sys.exit(1)
    
    # Read the map from file
    with open(sys.argv[1], 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    # Convert map to a 2D list for easier indexing
    # (Alternatively, we can just keep lines as is, but let's do it a bit more uniformly.)
    grid = [list(row) for row in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Find guard position and initial direction
    guard_row, guard_col = None, None
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    guard_direction = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                guard_row, guard_col = r, c
                guard_direction = direction_map[grid[r][c]]
                break
        if guard_row is not None:
            break
    
    # Keep track of visited positions
    visited = set()
    visited.add((guard_row, guard_col))

    while True:
        # Check if there's something directly in front
        dr, dc = get_deltas(guard_direction)
        front_r = guard_row + dr
        front_c = guard_col + dc
        
        # If front is out of bounds, the guard would leave the map on the next step - break out
        if not (0 <= front_r < rows and 0 <= front_c < cols):
            break

        # If there's an obstacle in front, turn right
        if grid[front_r][front_c] == '#':
            guard_direction = turn_right(guard_direction)
        else:
            # Move forward
            guard_row, guard_col = front_r, front_c
            visited.add((guard_row, guard_col))

    print(len(visited))

if __name__ == "__main__":
    main()

