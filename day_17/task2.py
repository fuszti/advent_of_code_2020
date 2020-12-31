from collections import Counter
from itertools import product

ACTIVE = "#"

def solve_task2(file_name):
    cube = read_file(file_name, simulation_length=6)
    for _ in range(6):
        cube = simulate(cube)
    return count_active_cells(cube)

def read_file(file_name, simulation_length):
    cube = None
    center_idx = None
    with open(file_name, "r") as f:
        for idx, line in enumerate(f):
            line = line.rstrip()
            if line != "":
                if cube is None:
                    cube = zero_cube(len(line) + 2*(simulation_length+1))
                    center_idx = (len(line) + 2*simulation_length) // 2 + 1
                for cell_idx, cell in enumerate(line):
                    cube[center_idx][center_idx][idx+simulation_length+1][cell_idx+simulation_length+1] = 1 if cell == ACTIVE else 0
    return cube

def simulate(cube):
    shape = len(cube)
    new_cube = zero_cube(shape)
    for idx0 in range(1, shape-1):
        for idx1 in range(1, shape-1):
            for idx2 in range(1, shape-1):
                for idx3 in range(1, shape-1):
                    new_cube[idx0][idx1][idx2][idx3] = calculate_new_value(cube, (idx0, idx1, idx2, idx3))
    return new_cube

def count_active_cells(cube):
    shape = len(cube)
    number_of_active_cells = 0
    for idx0 in range(shape):
        for idx1 in range(shape):
            for idx2 in range(shape):
                for idx3 in range(shape):
                    if cube[idx0][idx1][idx2][idx3] == 1:
                        number_of_active_cells += 1
    return number_of_active_cells

def zero_cube(shape):
    cube = [[[[0] * shape for _ in range(shape)] for __ in range(shape)] for ___ in range(shape)]
    return cube

def get_neighbors(cube, multi_index):
    idx0, idx1, idx2, idx3 = multi_index
    result = []
    for offset0, offset1, offset2, offset3 in product([-1, 0, 1], repeat=4):
        if not offset0 == offset1 == offset2 == offset3 == 0:
            result.append(cube[idx0 + offset0][idx1 + offset1][idx2 + offset2][idx3 + offset3])
    return result

def calculate_new_value(cube, multi_index):
    neighbors = get_neighbors(cube, multi_index)
    idx0, idx1, idx2, idx3 = multi_index
    curr_value = cube[idx0][idx1][idx2][idx3]
    number_of_active_neighbors = Counter(neighbors)[1]
    if curr_value == 0:
        return 1 if number_of_active_neighbors == 3 else 0
    return 1 if number_of_active_neighbors == 2 or number_of_active_neighbors == 3 else 0

if __name__ == "__main__":
    print(solve_task2("day_17/input.txt"))
