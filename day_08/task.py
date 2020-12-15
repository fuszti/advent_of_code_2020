from copy import deepcopy

def nope(accumalator, line_idx, arg):
    return accumalator, line_idx + 1

def jump(accumalator, line_idx, arg):
    return accumalator, line_idx + arg

def acc(accumalator, line_idx, arg):
    return accumalator + arg, line_idx + 1

class Machine:
    def __init__(self, accumalator=0):
        self.accumalator = accumalator
        self.commands = {
            "nop": nope,
            "acc": acc,
            "jmp": jump
        }
        self.read_line_indices = set()
    
    def run(self, program_code, line_idx=0):
        if line_idx in self.read_line_indices:
            return 1, self.accumalator
        elif line_idx == len(program_code):
            return 0, self.accumalator
        command, arg = program_code[line_idx]
        self.read_line_indices.add(line_idx)
        self.accumalator, line_idx = self.commands[command](
            self.accumalator, line_idx, arg
        )
        return self.run(program_code, line_idx)
        
    
def solve_task1(file_name):
    program_code = read_file(file_name)
    machine = Machine()
    return_code, accumalator = machine.run(program_code)
    return accumalator

def solve_task2(file_name):
    program_code = read_file(file_name)
    for line_idx, (command, arg) in enumerate(program_code):
        if command == "jmp" or command == "nop":
            new_command = "jmp" if command == "nop" else "nop"
            machine = Machine()
            program_code_copy = deepcopy(program_code)
            program_code_copy[line_idx] = (new_command, arg)
            return_code, accumalator = machine.run(program_code_copy)
            if return_code == 0:
                return accumalator
    return None

def read_file(file_name):
    program_code = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip()
            if line != "":
                command, arg = line.split()
                program_code.append((command, int(arg)))
    return program_code

if __name__ == "__main__":
    print(solve_task2("day_08/input.txt"))