def calculate_similarity_score(left_list, right_list):
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_list.count(number)
    return similarity_score

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
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(similarity_score)

if __name__ == "__main__":
    main()
