from functools import partial


def solve_task2(file_name):
    curr_pos = [0, 0]
    waypoint = [10, 1]
    with open(file_name, "r") as f:
        for line in f:
            if line != "\n":
                transform = command2transform(line.rstrip())
                curr_pos, waypoint = transform(curr_pos, waypoint)
                print(f"line: {line}   pos: {curr_pos}     waypoint: {waypoint}")
    return abs(curr_pos[0]) + abs(curr_pos[1])

def command2transform(command_str):
    command, parameter = command_str[0], int(command_str[1:])
    if command == "L":
        return partial(rot90_left, parameter // 90)
    elif command == "R":
        return partial(rot90_left, 4 - parameter // 90)
    elif command == "F":
        return partial(move_forward, parameter)
    elif command == "N":
        return partial(move, parameter, [0, 1])
    elif command == "E":
        return partial(move, parameter, [1, 0])
    elif command == "S":
        return partial(move, parameter, [0, -1])
    return partial(move, parameter, [-1, 0])

def rot90_left(times, curr_pos, waypoint):
    return curr_pos, rot90_left_origin(times, waypoint)

def rot90_left_origin(times, direction):
    for _ in range(times):
        direction = [-direction[1], direction[0]]
    return direction

def move_forward(distance, curr_pos, direction):
    movement = [distance * direction[0], distance * direction[1]]
    return [curr_pos[0] + movement[0], curr_pos[1] + movement[1]], direction

def move(distance, direction, curr_pos, waypoint):
    movement = [distance * direction[0], distance * direction[1]]
    return curr_pos, [waypoint[0] + movement[0], waypoint[1] + movement[1]]

if __name__ == "__main__":
    print(solve_task2("day_12/input.txt"))