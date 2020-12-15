from copy import deepcopy

EMPTY = "L"
OCCUPIED = "#"
NO_SEAT = "."

def solve_task1(file_name):
    seats = read_file(file_name)
    is_changed = False
    #_print(seats)
    while not is_changed:
        prev_seats = deepcopy(seats)
        seats = simulate_one_step(seats)
        is_changed = is_same_the_seats(prev_seats, seats)
        #_print(seats)
    return count_occupied_seats(seats)

def _print(seats):
    for row in seats:
        print(row)
    print("-----")

def read_file(file_name):
    seats = []
    with open(file_name, "r") as f:
        for line in f:
            if line != "\n":
                curr_row = [symbol for symbol in line.rstrip()]
                seats.append(curr_row)
    return seats

def simulate_one_step(prev_seats):
    new_seats = deepcopy(prev_seats)
    for row_idx in range(len(prev_seats)):
        for col_idx in range(len(prev_seats[0])):
            if prev_seats[row_idx][col_idx] == EMPTY and \
                _count_occupied_adjacents(prev_seats, row_idx, col_idx) == 0:
                new_seats[row_idx][col_idx] = OCCUPIED
            elif prev_seats[row_idx][col_idx] == OCCUPIED and \
                _count_occupied_adjacents(prev_seats, row_idx, col_idx) >= 4:
                new_seats[row_idx][col_idx] = EMPTY
    return new_seats

def count_occupied_seats(seats):
    return len([seat for row in seats for seat in row if seat == OCCUPIED])

def is_same_the_seats(seats, prev_seats):
    for row, prev_row in zip(seats, prev_seats):
        for seat, prev_seat in zip(row, prev_row):
            if seat != prev_seat:
                return False
    return True

def _count_occupied_adjacents(seats, row_idx, col_idx):
    adjacents = _get_adjacents(seats, row_idx, col_idx)
    return len([seat for seat in adjacents if seat == OCCUPIED])

def _get_adjacents(seats, row_idx, col_idx):
    adjacents = []
    index_pairs = [
        (row_idx - 1, col_idx - 1),
        (row_idx - 1, col_idx),
        (row_idx - 1, col_idx + 1),
        (row_idx, col_idx - 1),
        (row_idx, col_idx + 1),
        (row_idx + 1, col_idx - 1),
        (row_idx + 1, col_idx),
        (row_idx + 1, col_idx + 1)
    ]
    for r, c in index_pairs:
        seat = _get_seat(seats, r, c)
        if seat is not None:
            adjacents.append(seat)
    return adjacents

def _get_seat(seats, r, c):
    if r < 0 or r >= len(seats):
        return None
    if c < 0 or c >= len(seats[0]):
        return None
    return seats[r][c]

if __name__ == "__main__":
    print(solve_task1("day_11/input.txt"))
