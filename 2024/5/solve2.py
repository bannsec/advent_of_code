#!/usr/bin/env python3

import sys
from collections import deque, defaultdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 solve_print_queue.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read all lines from the file
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Separate the lines into rules (X|Y) and updates (comma-separated)
    rules = []
    updates = []

    is_parsing_rules = True
    for line in lines:
        if is_parsing_rules:
            if '|' in line:
                rules.append(line)
            else:
                # Once we see a line that doesn't contain '|', 
                # we assume all subsequent lines are updates
                is_parsing_rules = False
                updates.append(line)
        else:
            updates.append(line)

    # Parse the rules into a list of (X, Y) meaning X must come before Y
    constraints = []
    for rule in rules:
        left, right = rule.split('|')
        constraints.append((left.strip(), right.strip()))

    # Convert each update line into a list of pages
    parsed_updates = []
    for upd in updates:
        pages = [p.strip() for p in upd.split(',')]
        parsed_updates.append(pages)

    # Check if a single update is already in correct order
    def update_respects_rules(pages):
        index_map = {page: i for i, page in enumerate(pages)}
        for x, y in constraints:
            # Only check if both x and y are in this update
            if x in index_map and y in index_map:
                # If x must come before y, then index_map[x] < index_map[y]
                if index_map[x] >= index_map[y]:
                    return False
        return True

    # Topological sort to reorder an update correctly
    def reorder_update(pages):
        """
        Takes a list of pages in *any* order, uses the constraints
        to produce a topological ordering that satisfies all relevant rules.
        """
        # Build adjacency and indegree info for *only* the pages in this update
        adjacency = defaultdict(set)
        indegree = {page: 0 for page in pages}

        # Add edges for any constraint that applies to pages in this update
        for x, y in constraints:
            if x in indegree and y in indegree:
                # x must come before y
                if y not in adjacency[x]:
                    adjacency[x].add(y)
                    indegree[y] += 1

        # Kahn's Algorithm for topological sorting
        queue = deque([p for p in pages if indegree[p] == 0])
        sorted_list = []

        while queue:
            node = queue.popleft()
            sorted_list.append(node)
            for neighbor in adjacency[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If there's no cycle, sorted_list should have all pages
        # We assume the puzzle input doesn't produce cycles.
        return sorted_list

    # Separate updates into valid and invalid
    valid_updates = []
    invalid_updates = []

    for upd in parsed_updates:
        if update_respects_rules(upd):
            valid_updates.append(upd)
        else:
            invalid_updates.append(upd)

    # Part 1: Sum of middle pages of the already-correct updates
    sum_valid_middles = 0
    for upd in valid_updates:
        mid_index = len(upd) // 2
        sum_valid_middles += int(upd[mid_index])

    # Part 2: Reorder each invalid update, sum of middle pages
    sum_invalid_middles = 0
    for upd in invalid_updates:
        correct_order = reorder_update(upd)
        mid_index = len(correct_order) // 2
        sum_invalid_middles += int(correct_order[mid_index])

    # Print both results
    print(sum_valid_middles)   # Part One result
    print(sum_invalid_middles) # Part Two result

if __name__ == "__main__":
    main()

