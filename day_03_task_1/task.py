from collections import namedtuple

Slope = namedtuple("Slope", ("col_step", "row_step"))

def count_trees_from_file(file_name):
    map_str = read_file(file_name)
    return count_trees(map_str, 0, 0)

def solve_task2(file_name):
    map_str = read_file(file_name)
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    result = 1
    for slope in slopes:
        result *= count_trees(map_str, 0, 0, row_step=slope.row_step, col_step=slope.col_step)
    return result

def read_file(file_name):
    with open(file_name, "r") as f:
        rows = [row.rstrip() for row in f]
    return rows

def count_trees(map_str, start_row, start_col, row_step=1, col_step=3):
    row_ind = start_row
    col_ind = start_col
    nbr_of_rows = len(map_str)
    nbr_of_cols = len(map_str[0])
    tree_counter = 0
    while row_ind < nbr_of_rows:
        if map_str[row_ind][col_ind] == "#":
            tree_counter += 1
        row_ind = increase(row_ind, row_step, nbr_of_rows+2*row_step)
        col_ind = increase(col_ind, col_step, nbr_of_cols)
    return tree_counter

def increase(ind, step, length):
    ind += step
    ind %= length
    return ind

if __name__ == "__main__":
    #print(count_trees_from_file("day_03_task_1/input.txt"))
    print(solve_task2("day_03_task_1/input.txt"))
