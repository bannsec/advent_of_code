#!/usr/bin/env python3

import sys

def count_xmas_occurrences(grid):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # All 8 directions: (row increment, col increment)
    directions = [
        (0, 1),  # left-to-right
        (0, -1), # right-to-left
        (1, 0),  # top-to-bottom
        (-1, 0), # bottom-to-top
        (1, 1),  # diagonal down-right
        (1, -1), # diagonal down-left
        (-1, 1), # diagonal up-right
        (-1, -1) # diagonal up-left
    ]

    for r in range(rows):
        for c in range(cols):
            # Check each direction if "XMAS" can fit
            for dr, dc in directions:
                # Check boundary
                end_r = r + (len(word) - 1) * dr
                end_c = c + (len(word) - 1) * dc
                if 0 <= end_r < rows and 0 <= end_c < cols:
                    # Collect characters in this direction
                    chars = []
                    for i in range(len(word)):
                        rr = r + i*dr
                        cc = c + i*dc
                        chars.append(grid[rr][cc])
                    
                    # Compare to "XMAS"
                    if "".join(chars) == word:
                        count += 1
    return count

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Read input lines, strip, and store in a list of lists (characters)
    with open(file_path, 'r', encoding='utf-8') as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    total_occurrences = count_xmas_occurrences(grid)
    
    # Print the result
    print(total_occurrences)

if __name__ == "__main__":
    main()

