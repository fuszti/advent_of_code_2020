def solve_task1(file_name):
    required_bag = "shiny gold bag"
    bags_contained_by = read_file(file_name)
    bags_can_contain = get_bags_can_contain(required_bag, bags_contained_by)
    return len(bags_can_contain)

def read_file(file_name):
    bags_contained_by = {}
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip()
            contained_by, contains_bags = line.split(" contain ")
            if contains_bags != "no other bags.":
                contains_bags = contains_bags.split(",")
                contained_by = _trim_s(contained_by)
                contains_bags = [_trim_s(contain_bag) for contain_bag in contains_bags]
                contains_bags = [_trim_num(contain_bag) for contain_bag in contains_bags]
                for bag in contains_bags:
                    bags_contained_by.setdefault(bag, []).append(contained_by)
    return bags_contained_by

def get_bags_can_contain(required_bag, bags_contained_by):
    result = set()
    for contained_by in bags_contained_by.get(required_bag, []):
        result.add(contained_by)
        contained_deeply_by = get_bags_can_contain(contained_by, bags_contained_by)
        result = result.union(contained_deeply_by)
    return result

def _trim_s(bag_name):
    bag_name = bag_name.rstrip()
    bag_name = bag_name[:-1] if bag_name[-1] == "." else bag_name
    return bag_name[:-1] if bag_name[-1] == "s" else bag_name

def _trim_num(bag_name):
    first_letter_idx = 0
    while bag_name[first_letter_idx] == " " or ("0" <= bag_name[first_letter_idx] <= "9"):
        first_letter_idx += 1
    return bag_name[first_letter_idx:]

if __name__ == "__main__":
    print(solve_task1("day_07/input.txt"))
