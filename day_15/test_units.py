import pytest

from task import solve_task1, solve_task2

@pytest.mark.parametrize("input_numbers, the_2020th_number",
                         [([0, 3, 6], 436),
                          ([1,3,2], 1),
                          ([2,1,3], 10),
                          ([1,2,3], 27),
                          ([2,3,1], 78),
                          ([3,2,1], 438),
                          ([3,1,2], 1836)])
def test_solve_task1(input_numbers, the_2020th_number):
    output = solve_task1(input_numbers)
    assert the_2020th_number == output, f"Result should be {the_2020th_number} instead of {output}."     

@pytest.mark.parametrize("input_numbers, result",
                         [([0, 3, 6], 175594),
                          ([1,3,2], 2578),
                          ([2,1,3], 3544142),
                          ([1,2,3], 261214),
                          ([2,3,1], 6895259),
                          ([3,2,1], 18),
                          ([3,1,2], 362)])
def test_solve_task2(input_numbers, result):
    output = solve_task2(input_numbers)
    assert result == output, f"Result should be {result} instead of {output}."   
                     