import pytest

from task import solve_task1, solve_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_16/small_input.txt", 71)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("file_name, result, key_word",
                         [("day_16/small_input.txt", 14, "seat"),
                          ("day_16/small_input2.txt", 12, "class")])
def test_task2(file_name, result, key_word):
    r = solve_task2(file_name, key_word)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."
