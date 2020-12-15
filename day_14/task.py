NATURAL_MASK_ELEM = "X"


def solve_task1(file_name):
    saved_numbers = get_final_numbers_after_running(file_name)
    return sum(saved_numbers)

def get_final_numbers_after_running(file_name):
    memory = {}
    with open(file_name, "r") as f:
        mask = None
        for line in f:
            if _is_mask_init(line):
                mask = _extract_mask(line)
            else:
                memory_address, number = _preproc_line(line)
                memory[memory_address] = modify_by_mask(number, mask)
    return list(memory.values())

def modify_by_mask(number, mask):
    number_bin_str = bin(number)[2:]
    full_bin_number_rep = "0" * (len(mask) - len(number_bin_str)) + number_bin_str
    new_number = "".join([full_bin_number_rep[idx] 
                          if mask_elem == NATURAL_MASK_ELEM else mask_elem 
                          for idx, mask_elem in enumerate(mask)])
    return int(new_number, 2)

def _is_mask_init(line):
    return line[:4] == "mask"

def _preproc_line(line):
    memory_address = int(line.split("]")[0].split("[")[1])
    number = int(line.split("=")[1])
    return memory_address, number

def _extract_mask(line):
    return line.rstrip().split("=")[1][1:]

if __name__ == "__main__":
    print(solve_task1("day_14/input.txt"))
