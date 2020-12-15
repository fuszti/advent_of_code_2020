from functools import partial


def solve_task1(file_name):
    direction = [0, 1]
    curr_pos = [0, 0]
    with open(file_name, "r") as f:
        for line in f:
            if line != "\n":
                transform = command2transform(line.rstrip())
                curr_pos, direction = transform(curr_pos, direction)
                #print(f"pos: {curr_pos}     dir: {direction}")
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
        return partial(move, parameter, [1, 0])
    elif command == "E":
        return partial(move, parameter, [0, 1])
    elif command == "S":
        return partial(move, parameter, [-1, 0])
    return partial(move, parameter, [0, -1])

def rot90_left(times, curr_pos, direction):
    for _ in range(times):
        direction = [direction[1], -direction[0]]
    return curr_pos, direction

def move_forward(distance, curr_pos, direction):
    movement = [distance * direction[0], distance * direction[1]]
    return [curr_pos[0] + movement[0], curr_pos[1] + movement[1]], direction

def move(distance, direction, curr_pos, direction_will_be_untouched):
    movement = [distance * direction[0], distance * direction[1]]
    return [curr_pos[0] + movement[0], curr_pos[1] + movement[1]], direction_will_be_untouched

if __name__ == "__main__":
    print(solve_task1("day_12/input.txt"))