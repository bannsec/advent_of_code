def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def main():
    import sys
    file_path = sys.argv[1]
    reports = read_input(file_path)
    safe_report_count = count_safe_reports(reports)
    print(safe_report_count)

if __name__ == "__main__":
    main()
