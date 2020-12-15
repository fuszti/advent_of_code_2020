def solve_task1(file_name):
    with open(file_name, "r") as f:
        curr_group_answers = set()
        result = 0
        for line in f:
            if line == "\n":
                result += len(curr_group_answers)
                curr_group_answers = set()
            else:
                line = line.rstrip()
                for question in line:
                    curr_group_answers.add(question)
        result += len(curr_group_answers) 
    return result

def solve_task2(file_name):
    with open(file_name, "r") as f:
        curr_group_answers = set()
        result = 0
        is_new_group = True
        for line in f:
            if line == "\n":
                result += len(curr_group_answers)
                curr_group_answers = set()
                is_new_group = True
            else:
                line = line.rstrip()
                curr_person = set()
                for question in line:
                    curr_person.add(question)
                if is_new_group:
                    is_new_group = False
                    curr_group_answers = curr_person
                else:
                    curr_group_answers = curr_group_answers.intersection(curr_person)
        result += len(curr_group_answers) 
    return result

if __name__ == "__main__":
    print(solve_task2("day_06/input.txt"))