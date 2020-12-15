import pytest

from task import solve_task1 
from task2 import solve_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_11/small_input.txt", 37)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("file_name, result",
                         [("day_11/small_input.txt", 26)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."