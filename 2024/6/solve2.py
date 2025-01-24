#!/usr/bin/env python3

import sys

def turn_right(direction):
    """
    Rotate direction 90 degrees to the right.
    Directions: 0=up, 1=right, 2=down, 3=left.
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
    else:  # 3=left
        return 0, -1

def simulate_guard(grid, start_r, start_c, start_dir):
    """
    Simulate the guard's movement on the map until the guard
    either leaves the map (return False) or gets stuck in a loop (return True).

    grid is a list of lists of characters.
    start_r, start_c is the guard's starting row and column.
    start_dir is the guard's initial direction (0=up, 1=right, 2=down, 3=left).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Keep track of (row, col, direction) states we've seen to detect loops.
    visited_states = set()

    r, c = start_r, start_c
    direction = start_dir

    while True:
        # If we've been here (same position + direction) before, it's a loop.
        if (r, c, direction) in visited_states:
            return True  # The guard is stuck in a loop!
        visited_states.add((r, c, direction))

        # Compute the position in front of the guard
        dr, dc = get_deltas(direction)
        front_r = r + dr
        front_c = c + dc

        # If the guard would walk off the map, guard leaves => no loop
        if not (0 <= front_r < rows and 0 <= front_c < cols):
            return False

        # If there's an obstacle in front, turn right
        if grid[front_r][front_c] == '#':
            direction = turn_right(direction)
        else:
            # Move forward
            r, c = front_r, front_c

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        sys.exit(1)
    
    # Read the map
    with open(sys.argv[1], 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    # Convert map to a 2D list for easier manipulation
    grid = [list(row) for row in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Locate guard's starting position & direction
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    guard_r = guard_c = None
    guard_dir = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                guard_r, guard_c = r, c
                guard_dir = direction_map[grid[r][c]]
                break
        if guard_r is not None:
            break

    # Replace the guard's symbol with '.' so it becomes effectively empty
    grid[guard_r][guard_c] = '.'

    # Now, we want to try adding one new obstruction at each possible '.' spot
    # (except the guard's starting position).
    valid_positions_count = 0

    for r in range(rows):
        for c in range(cols):
            # Must be a valid empty spot, not the guard's original start
            if (r, c) == (guard_r, guard_c):
                continue  # can't place obstacle on guard's starting position
            if grid[r][c] != '.':
                continue  # only place new obstacle on empty space

            # Temporarily place an obstacle here
            grid[r][c] = '#'

            # Simulate the guard's route
            if simulate_guard(grid, guard_r, guard_c, guard_dir):
                # If True, the guard gets stuck in a loop for this placement
                valid_positions_count += 1

            # Remove the obstacle to try the next spot
            grid[r][c] = '.'

    print(valid_positions_count)

if __name__ == "__main__":
    main()

