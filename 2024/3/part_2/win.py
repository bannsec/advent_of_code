import re
import sys

def main():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        memory = file.read()

    # Pattern to find mul() instructions, capturing the two numbers
    mul_pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    # Pattern to find do() or don't() instructions
    do_pattern = re.compile(r'\bdo\(\)')
    dont_pattern = re.compile(r"\bdon't\(\)")

    # We'll process the memory string from left to right, marking regions of enable/disable
    # Approach: Use an index and find the earliest instruction (mul, do, don't) in sequence.
    # Keep track of enable state, and sum up valid mul instructions.

    enabled = True  # Default state
    current_index = 0
    total_sum = 0

    # To handle all instructions in order, we can find all matches and sort them by position.
    instructions = []
    for match in mul_pattern.finditer(memory):
        instructions.append((match.start(), 'mul', match.group(1), match.group(2)))
    for match in do_pattern.finditer(memory):
        instructions.append((match.start(), 'do'))
    for match in dont_pattern.finditer(memory):
        instructions.append((match.start(), 'dont'))

    # Sort instructions by their position in the memory
    instructions.sort(key=lambda x: x[0])

    # Iterate over instructions in order
    for instr in instructions:
        if instr[1] == 'do':
            enabled = True
        elif instr[1] == 'dont':
            enabled = False
        elif instr[1] == 'mul':
            # instr = (start, 'mul', x, y)
            if enabled:
                x, y = int(instr[2]), int(instr[3])
                total_sum += x * y

    print(total_sum)

if __name__ == "__main__":
    main()
