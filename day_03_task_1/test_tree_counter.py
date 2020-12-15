import pytest

from task import count_trees_from_file, solve_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_03_task_1/half_free.txt", 4),
                          ("day_03_task_1/small_input.txt", 7),
                          ("day_03_task_1/strict_test.txt", 0)])
def test_on_small_examples(file_name, result):
    r = count_trees_from_file(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

def test_task2_on_small_example():
    r = solve_task2("day_03_task_1/small_input.txt")
    assert r == 336
