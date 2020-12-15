from typing import Dict, List

from task2_validators import get_validators_for_task2


VALID_KEYS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl", 
    "ecl",
    "pid", 
    "cid"
]

OPTIONAL = ["cid"]

def solve_task1(file_name):
    passports = read_passports(file_name)
    nbr_of_valid_passports = 0
    for passport in passports:
        if is_valid(passport):
            nbr_of_valid_passports += 1
    return nbr_of_valid_passports

def solve_task2(file_name):
    passports = read_passports(file_name)
    nbr_of_valid_passports = 0
    for passport in passports:
        if is_valid_2(passport):
            nbr_of_valid_passports += 1
            #print(passport)
            #print("----")
    return nbr_of_valid_passports


def read_passports(file_name) -> List[Dict[str, str]]:
    passports = []
    with open(file_name, "r") as f:
        curr_passport = {}
        for line in f:
            if line == "\n":
                passports.append(curr_passport)
                curr_passport = {}
            else:
                for key_value_pair in line.split():
                    key_, value_ = key_value_pair.split(":")
                    curr_passport[key_] = value_
    if len(curr_passport) > 0:
        passports.append(curr_passport)
    return passports

def is_valid(passport):
    passport_keys = list(passport.keys())
    missing_keys = [key_ for key_ in VALID_KEYS if key_ not in passport_keys]
    other_keys = [k for k in passport_keys if k not in VALID_KEYS + OPTIONAL]
    if other_keys:
        return False
    if len(missing_keys) == 0 or (len(missing_keys) == 1 and missing_keys[0] in OPTIONAL):
        return True
    return False

def is_valid_2(passport):
    is_valid_key = get_validators_for_task2()
    is_valid_keys = [is_valid_key[key_](value_) 
                     for key_, value_ in passport.items()]
    return all(is_valid_keys) and is_valid(passport)

if __name__ == "__main__":
    print(solve_task2("day_04/input.txt"))
