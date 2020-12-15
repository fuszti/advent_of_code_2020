from collections import Counter
import pytest

from task import solve_task1, get_bags_can_contain
from task2 import solve_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_07/small_input.txt", 4)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("required_bag_name, bags_contained_by, required_results",
                         [("test", {"not_contains": ["Not test", "neither test"],
                                   "test": ["not_test", "contains_test"]},
                            ["contains_test"]),
                          ("test", {"not_contains": ["Not test", "neither test"],
                                    "test": ["not_test", "contains_test"],
                                    "contains_test": ["contains_test_deeply"]},
                            ["contains_test", "contains_test_deeply"])])
def test_bags_contained_by(required_bag_name, bags_contained_by, required_results):
    bags = get_bags_can_contain(required_bag_name, bags_contained_by)     
    counted_results = Counter(bags)
    for required_bag in required_results:
        assert counted_results[required_bag] == 1, f"{required_bag} should be once in the results"                      

@pytest.mark.parametrize("file_name, result",
                         [("day_07/small_input.txt", 32)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."