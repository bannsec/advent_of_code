import re

def extract_mul_instructions(memory):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    return pattern.findall(memory)

def calculate_sum_of_mul_results(instructions):
    return sum(int(x) * int(y) for x, y in instructions)

def main():
    import sys
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        memory = file.read()
    instructions = extract_mul_instructions(memory)
    result_sum = calculate_sum_of_mul_results(instructions)
    print(result_sum)

if __name__ == "__main__":
    main()
