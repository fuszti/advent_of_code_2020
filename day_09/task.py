from itertools import combinations

def solve_task1(file_name, preamble_len):
    numbers = read_file(file_name)
    for curr_idx in range(preamble_len, len(numbers)):
        if not is_valid(numbers[curr_idx], numbers[curr_idx - preamble_len: curr_idx]):
            return numbers[curr_idx]

def solve_task2(file_name, preamble_len):
    numbers = read_file(file_name)
    for curr_idx in range(preamble_len, len(numbers)):
        num = numbers[curr_idx]
        candidates = numbers[curr_idx - preamble_len: curr_idx]
        if not is_valid(num, candidates):
            return min_max_sum_of_optimal_sublist(num, numbers[:curr_idx])

def read_file(file_name):
    with open(file_name, "r") as f:
        numbers = [int(line) for line in f if line != "\n"]
    return numbers

def is_valid(num, number_candidates):
    for a, b in combinations(number_candidates, 2):
        if a + b == num:
            return True
    return False

def min_max_sum_of_optimal_sublist(num, number_candidates):
    indices = list(range(len(number_candidates)))
    for sublist_start_ind, sublist_end_ind in combinations(indices, 2):
        sublist = number_candidates[sublist_start_ind:sublist_end_ind+1]
        if sum(sublist) == num:
            return min(sublist) + max(sublist)
    return None

if __name__ == "__main__":
    print(solve_task2("day_09/input.txt", 25))