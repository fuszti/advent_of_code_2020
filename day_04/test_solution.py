import pytest

from task import solve_task1, solve_task2
from task2_validators import get_validators_for_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_04/small_input.txt", 2),
                         ("day_04/no_opt_missing.txt", 1)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("file_name, result",
                         [("day_04/invalid_passports_for_task2.txt", 0),
                          ("day_04/valid_passports_for_task2.txt", 4)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

def test_validators():
    passport = {
        "hcl":"#888785", "iyr":"2015",
        "ecl":"hzl", "hgt":"164cm", "pid":"545766238", 
        "eyr":"2022", "byr":"2001", "cid":"88"
    }
    is_valids = get_validators_for_task2()
    for key_, value_ in passport.items():
        assert is_valids[key_](value_), f"{key_} should be True"
