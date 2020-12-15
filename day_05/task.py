def solve_task1(file_name):
    max_seat_id = -1
    with open(file_name, "r") as f:
        for encoded_seat in f:
            row, col = extract_row_and_col(encoded_seat)
            seat_id = row * 8 + col
            max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id
    return max_seat_id

def extract_row_and_col(encoded_seat):
    row_str, col_str = encoded_seat[:7], encoded_seat[-3:]
    row_str = _convert_to_binary_str(row_str, zero="F", one="B")
    col_str = _convert_to_binary_str(col_str, zero="L", one="R")
    row_bin, col_bin = int(row_str, 2), int(col_str, 2)
    return int(row_bin), int(col_bin)

def _convert_to_binary_str(s, zero, one):
    s = s.replace(zero, "0")
    s = s.replace(one, "1")
    return s

if __name__ == "__main__":
    print(solve_task1("day_05/input.txt"))
