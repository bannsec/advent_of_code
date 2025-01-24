#!/usr/bin/env python3

import sys

def is_valid_mas(segment):
    """Check if a 3-letter segment is MAS or SAM."""
    return segment in ("MAS", "SAM")

def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # We'll treat each valid cell (r, c) as the center of an X.
    # That means we need (r-1, c-1), (r+1, c+1), (r-1, c+1), (r+1, c-1) to be valid cells.
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Top-left diagonal (r-1,c-1) -> (r,c) -> (r+1,c+1)
            diag1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
            # Top-right diagonal (r-1,c+1) -> (r,c) -> (r+1,c-1)
            diag2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]

            if is_valid_mas(diag1) and is_valid_mas(diag2):
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

    total_occurrences = count_x_mas_occurrences(grid)
    
    # Print the result
    print(total_occurrences)

if __name__ == "__main__":
    main()

