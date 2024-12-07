def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance

def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def main():
    import sys
    file_path = sys.argv[1]
    left_list, right_list = read_input(file_path)
    total_distance = calculate_total_distance(left_list, right_list)
    print(total_distance)

if __name__ == "__main__":
    main()
