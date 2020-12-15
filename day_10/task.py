from collections import Counter

import numpy as np

def solve_task1(file_name):
    joltage_rates = read_file(file_name)
    sorted_joltage_rates = [0] + sorted(joltage_rates)
    sorted_joltage_rates_np = np.array(sorted_joltage_rates + [max(sorted_joltage_rates)+3])
    rate_diff_list = np.diff(sorted_joltage_rates_np).tolist()
    rate_diff_counts = Counter(rate_diff_list)
    return rate_diff_counts[1] * rate_diff_counts[3]

def solve_task2(file_name):
    joltage_rates = read_file(file_name)
    sorted_joltage_rates = [0] + sorted(joltage_rates) + [max(joltage_rates) + 3]
    return count_possible_chains(sorted_joltage_rates)

def read_file(file_name):
    with open(file_name, "r") as f:
        joltage_rates = [int(line) for line in f if line != "\n"]
    return joltage_rates

def count_possible_chains(sorted_joltage_rates):
    compatible_diffs = [1, 2, 3]
    nbr_of_possible_chains = [0] * len(sorted_joltage_rates)
    nbr_of_possible_chains[0] = 1
    for idx, joltage_rate in enumerate(sorted_joltage_rates[1:]):
        curr_idx = idx + 1
        step_back = 1
        while curr_idx - step_back >= 0 and \
            joltage_rate - sorted_joltage_rates[curr_idx - step_back] <= 3:
            nbr_of_possible_chains[curr_idx] += nbr_of_possible_chains[curr_idx - step_back]
            step_back += 1
    return nbr_of_possible_chains[-1]

if __name__ == "__main__":
    print(solve_task2("day_10/input.txt"))
