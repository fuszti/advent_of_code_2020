import pytest

from task import solve_task1, solve_task2


@pytest.mark.parametrize("file_name, result",
                         [("day_10/small_input.txt", 35),
                          ("day_10/medium_input.txt", 220)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("file_name, result",
                         [("day_10/small_input.txt", 8),
                          ("day_10/medium_input.txt", 19208)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."