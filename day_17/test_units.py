from collections import Counter
import pytest

from task import solve_task1, get_neighbors, calculate_new_value 
from task2 import solve_task2

CUBE_2x2x2 = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
              [[0, 0, 0], [0, 111, 112], [0, 121, 122]],
              [[0, 211, 212], [0, 221, 222], [0, 0, 0]]]

CUBE_CENTER_0_TO_1 = [[[0, 0, 1], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 1], [0, 0, 1]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

CUBE_CENTER_1_TO_1 = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

CUBE_CENTER_1_TO_0 = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 1, 1], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]  

CUBE_CENTER_1_TO_0_LOT_1 = [[[1, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
                            [[0, 1, 1], [0, 0, 0], [0, 0, 0]]]                   


@pytest.mark.parametrize("file_name, result",
                         [("day_17/small_input.txt", 112)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("cube, multi_index_of_cell, neighbors",
                         [(CUBE_2x2x2, (1, 1, 1), [112, 121, 122, 211, 212, 221, 222]+[0]*19)])
def test_neighbors(cube, multi_index_of_cell, neighbors):
    neighbors_guess = get_neighbors(cube, multi_index_of_cell)
    counter_of_guess = Counter(neighbors_guess)
    counter_of_neighbors = Counter(neighbors)

    assert len(counter_of_guess) == len(counter_of_neighbors), "There is not found neighbors."
    for neighbor, count in counter_of_neighbors.items():
        assert count == counter_of_guess[neighbor], f"{neighbor} should be {count} times in neighbors."

@pytest.mark.parametrize("cube, new_value_of_center",
                         [(CUBE_CENTER_0_TO_1, 1),
                          (CUBE_CENTER_1_TO_0, 0),
                          (CUBE_CENTER_1_TO_1, 1),
                          (CUBE_CENTER_1_TO_0_LOT_1, 0)])
def test_new_value_calculation(cube, new_value_of_center):
    guessed_value = calculate_new_value(cube, (1, 1, 1))
    assert new_value_of_center == guessed_value, f"New value of (1, 1, 1) should be {new_value_of_center}." 

@pytest.mark.parametrize("file_name, result",
                         [("day_17/small_input.txt", 848)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."                        
