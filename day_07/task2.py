def solve_task2(file_name):
    required_bag = "shiny gold bag"
    bag_contains = read_file(file_name)
    return count_bags_in_it(required_bag, bag_contains)

def read_file(file_name):
    bag_contains = {}
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip()
            contained_by, contains_bags = line.split(" contain ")
            if contains_bags != "no other bags.":
                contains_bags = contains_bags.split(",")
                contained_by = _trim_s(contained_by)
                contains_bags = [_trim_s(contain_bag) for contain_bag in contains_bags]
                for bag_with_num in contains_bags:
                    num, bag = _extract_num_and_bag(bag_with_num)
                    bag_contains.setdefault(contained_by, []).append((bag, num))
    return bag_contains

def count_bags_in_it(bag_name, bag_contains):
    result = 0
    for bag, num in bag_contains.get(bag_name, []):
        result += num
        result += num * count_bags_in_it(bag, bag_contains)
    return result

def _trim_s(bag_name):
    bag_name = bag_name.rstrip()
    bag_name = bag_name[:-1] if bag_name[-1] == "." else bag_name
    return bag_name[:-1] if bag_name[-1] == "s" else bag_name

def _extract_num_and_bag(bag_with_num):
    first_letter_idx = 0
    while bag_with_num[first_letter_idx] == " " or ("0" <= bag_with_num[first_letter_idx] <= "9"):
        first_letter_idx += 1
    return int(bag_with_num[:first_letter_idx-1]), bag_with_num[first_letter_idx:]

if __name__ == "__main__":
    print(solve_task2("day_07/input.txt"))
