NOT_EXIST_IDX = -1

def solve_task1(numbers, last_turn_idx=2020):
    number_to_last_idx = {}
    for idx, number in enumerate(numbers):
        last_idx = number_to_last_idx.get(number, NOT_EXIST_IDX)
        number_to_last_idx[number] = idx + 1
    last_number = numbers[-1]
    for curr_turn_idx in range(idx + 1, last_turn_idx):
        last_number = 0 if last_idx == NOT_EXIST_IDX else curr_turn_idx - last_idx
        last_idx = number_to_last_idx.get(last_number, NOT_EXIST_IDX)
        number_to_last_idx[last_number] = curr_turn_idx + 1
    return last_number

def solve_task2(numbers):
    return solve_task1(numbers, 30000000)

if __name__ == "__main__":
    input_of_task1 = [1,0,18,10,19,6]
    print(solve_task2(input_of_task1))
