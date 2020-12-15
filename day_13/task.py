def solve_task1(file_name):
    with open(file_name,"r") as f:
        time = int(f.readline())
        buses = [int(i) for i in f.readline().split(",") if i != "x"]
    remaining = [i - time%i if time%i > 0 else 0 for i in buses]
    min_idx = remaining.index(min(remaining))
    return remaining[min_idx] * buses[min_idx]

def solve_task2(file_name):
    with open(file_name,"r") as f:
        time = int(f.readline())
        buses = [int(i) if i != "x" else -1 for i in f.readline().split(",")]

        found = False
        initial_time_candidates = [buses[i] - i if buses[i] != -1 else -1 for i in range(len(buses)) ]
        time = max(initial_time_candidates)
        step = buses[initial_time_candidates.index(time)]
        print(step)
        prod = 1
        for b in buses:
            prod *= b
        print(prod)
        time = abs(prod)
        while not found:
            moduluses = [(time + i)%buses[i] if buses[i] != -1 else 0 for i in range(len(buses))]
            if min(moduluses) == 0 and max(moduluses) == 0:
                found = True
            else:
                time += -1
    return time

if __name__=="__main__":
    print(solve_task2("day_13/input.txt"))