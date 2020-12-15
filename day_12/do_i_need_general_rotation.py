with open("day_12/input.txt", "r") as f:
    values = set()
    for line in f:
        if line[0] == "R" or line[0] == "L":
            values.add(int(line[1:]))
print(values)
