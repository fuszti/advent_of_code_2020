import pytest

from task import solve_task1, solve_task2


@pytest.mark.parametrize("file_name, preamble_len, result",
                         [("day_09/small_input.txt", 5, 127)])
def test_task1(file_name, preamble_len, result):
    r = solve_task1(file_name, preamble_len)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("file_name, result",
                         [("day_09/small_input.txt", 62)])
def test_task2(file_name, result):
    r = solve_task2(file_name, 5)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."