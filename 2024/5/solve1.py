#!/usr/bin/env python3

import sys

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
    
    # First, collect all lines until we reach something that doesn't have '|'
    # Then, the rest will be the updates.
    is_parsing_rules = True
    
    for line in lines:
        # If it's still in the rules section
        if is_parsing_rules:
            if '|' in line:
                rules.append(line)
            else:
                # Once we see a line that doesn't contain '|', 
                # we assume all subsequent lines are updates
                is_parsing_rules = False
                updates.append(line)  # Add the first update line
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
    
    def update_respects_rules(pages):
        """
        Check if the list of pages respects the rules in 'constraints'.
        Only consider rules relevant to the pages in this update.
        """
        # Make a quick index lookup so we can quickly check ordering
        index_map = {page: i for i, page in enumerate(pages)}
        
        for x, y in constraints:
            # Only check if both x and y are in this update
            if x in index_map and y in index_map:
                # If x must come before y, then index_map[x] < index_map[y]
                if index_map[x] >= index_map[y]:
                    return False
        return True
    
    valid_updates = []
    for upd in parsed_updates:
        if update_respects_rules(upd):
            valid_updates.append(upd)
    
    # Find the middle page number of each correctly-ordered update
    # The "middle" is the element at index len(upd)//2 (0-based).
    middle_sum = 0
    for upd in valid_updates:
        mid_index = len(upd) // 2
        middle_sum += int(upd[mid_index])
    
    # Print the sum
    print(middle_sum)

if __name__ == "__main__":
    main()

