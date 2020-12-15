from itertools import product
NATURAL_MASK_ELEM = "0"
FLOATING_MASK_ELEM = "X"


def solve_task2(file_name):
    memory = {}
    with open(file_name, "r") as f:
        mask = None
        for line in f:
            if _is_mask_init(line):
                mask = _extract_mask(line)
            else:
                memory_address, number = _preproc_line(line)
                concrete_memory_adresses = modify_by_mask2(memory_address, mask)
                for concrete_memory_adress in concrete_memory_adresses:
                    memory[concrete_memory_adress] = number
    return sum(list(memory.values()))

def modify_by_mask2(number, mask):
    numbers = []
    number_bin_str = bin(number)[2:]
    full_bin_number_rep = "0" * (len(mask) - len(number_bin_str)) + number_bin_str
    new_number_digits = [full_bin_number_rep[idx] 
                         if mask_elem == NATURAL_MASK_ELEM else mask_elem 
                         for idx, mask_elem in enumerate(mask)]
    new_number_digits = [new_number_digits[idx] if mask_elem != FLOATING_MASK_ELEM else FLOATING_MASK_ELEM
                         for idx, mask_elem in enumerate(mask)]
    nbr_of_floating_elements = sum([1 for elem in new_number_digits if elem == FLOATING_MASK_ELEM])
    for curr_combination in product(["0", "1"], repeat=nbr_of_floating_elements):
        curr_idx_in_combination = 0
        curr_number_digits = []
        for digit in new_number_digits:
            if digit == FLOATING_MASK_ELEM:
                curr_number_digits.append(curr_combination[curr_idx_in_combination])
                curr_idx_in_combination += 1
            else:
                curr_number_digits.append(digit)
        numbers.append(int("".join(curr_number_digits), 2))
    return numbers

def _is_mask_init(line):
    return line[:4] == "mask"

def _preproc_line(line):
    memory_address = int(line.split("]")[0].split("[")[1])
    number = int(line.split("=")[1])
    return memory_address, number

def _extract_mask(line):
    return line.rstrip().split("=")[1][1:]

if __name__ == "__main__":
    print(solve_task2("day_14/input.txt"))
