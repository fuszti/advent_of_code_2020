import numpy as np

def solve_task1(file_name):
    rules, my_ticket, nearby_tickets = read_file(file_name)
    valid_numbers = set().union(*[set(rule_range) for rule_ranges in rules.values() for rule_range in rule_ranges])
    result = sum_of_invalid_numbers(nearby_tickets, valid_numbers)
    return result

def solve_task2(file_name, key_word="departure"):
    rules, my_ticket, nearby_tickets = read_file(file_name)
    valid_numbers = set().union(*[set(rule_range) for rule_ranges in rules.values() for rule_range in rule_ranges])
    nearby_tickets = throw_out_invalid_tickets(nearby_tickets, valid_numbers)   
    valid_ticket_cells = np.array(nearby_tickets + [my_ticket])
    is_valid_rule_on_ticket = [[False] * valid_ticket_cells.shape[1] for _ in rules]
    cell_name_candidates = [[] for _ in range(valid_ticket_cells.shape[1])]
    for rule_name, rule_ranges in rules.items():
        for cell_idx, _ in enumerate(cell_name_candidates):
            if is_valid_rule_on_cell(rule_ranges, valid_ticket_cells, cell_idx):
                cell_name_candidates[cell_idx].append(rule_name)
    result = 1
    cell_names = get_cell_names(cell_name_candidates)
    for cell_idx, cell_name in enumerate(cell_names):
        if key_word in cell_name:
            result *= my_ticket[cell_idx]
    return result

def read_file(file_name):
    with open(file_name, "r") as f:
        rules = _parse_rules(f)
        my_ticket = _parse_my_ticket(f)
        nearby_tickets = _parse_nearby_tickets(f)
    return rules, my_ticket, nearby_tickets

def sum_of_invalid_numbers(tickets, valid_numbers):
    return sum([num for ticket in tickets for num in ticket if num not in valid_numbers])

def throw_out_invalid_tickets(nearby_tickets, valid_numbers):
    return [ticket for ticket in nearby_tickets if all([num in valid_numbers for num in ticket])]

def is_valid_rule_on_cell(rule_ranges, valid_ticket_cells, cell_idx):
    numbers = valid_ticket_cells[:, cell_idx].tolist()
    return all([num in set().union(*[set(r) for r in rule_ranges]) for num in numbers])

def get_cell_names(cell_name_candidates):
    while sum([len(candidates) for candidates in cell_name_candidates]) != len(cell_name_candidates):
        one_candidates = [candidates[0] for candidates in cell_name_candidates if len(candidates) == 1]
        new_cell_name_candidates = []
        for candidates in cell_name_candidates:
            if len(candidates) > 1:
                new_candidates = [candidate for candidate in candidates if candidate not in one_candidates]
                new_cell_name_candidates.append(new_candidates)
            else:
                new_cell_name_candidates.append(candidates)
        cell_name_candidates = new_cell_name_candidates
    return [candidates[0] for candidates in cell_name_candidates]

def _parse_rules(input_file):
    rules = {}
    line = input_file.readline().rstrip()
    while line != "":
        rule_name, ranges = _parse_one_rule(line)
        rules[rule_name] = ranges
        line = input_file.readline().rstrip()
    return rules

def _parse_my_ticket(input_file):
    input_file.readline()
    my_ticket = _parse_one_ticket(input_file.readline().rstrip())
    input_file.readline()
    return my_ticket

def _parse_nearby_tickets(input_file):
    input_file.readline()
    tickets = []
    line = input_file.readline().rstrip()
    while line != "":
        tickets.append(_parse_one_ticket(line))
        line = input_file.readline().rstrip()
    return tickets

def _parse_one_rule(line):
    rule_name, ranges_str = line.split(":")
    splited_ranges_str = ranges_str.split(" or ")
    ranges = []
    for range_str in splited_ranges_str:
        end_points_strings = range_str.split("-")
        ranges.append(range(int(end_points_strings[0]), int(end_points_strings[1]) + 1))
    return rule_name, ranges

def _parse_one_ticket(line):
    return [int(num) for num in line.split(",")]

if __name__ == "__main__":
    print(solve_task2("day_16/input.txt"))
