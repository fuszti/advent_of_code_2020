import pytest

from task import solve_task1, modify_by_mask
from task2 import solve_task2, modify_by_mask2


@pytest.mark.parametrize("file_name, result",
                         [("day_14/small_input.txt", 165)])
def test_task1(file_name, result):
    r = solve_task1(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("number, mask, result",
                         [(11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 73),
                          (1, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1X", 3),
                          (3, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0X", 1,),
                          (3, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX11", 3)])
def test_modify_by_mask(number, mask,  result):
    modified_number = modify_by_mask(number, mask)
    assert result == modified_number, f"Masked number should be {result} instead of {modified_number}."

@pytest.mark.parametrize("file_name, result",
                         [("day_14/small_input2.txt", 208)])
def test_task2(file_name, result):
    r = solve_task2(file_name)
    assert r == result, f"{file_name} failed. It returned with {r} instead of {result}."

@pytest.mark.parametrize("number, mask, result",
                         [(1, "000000000000000000000000000000000X1X", [2, 3, 6, 7]),
                          (3, "000000000000000000000000000000000X0X", [2, 3, 6 ,7],),
                          (3, "000000000000000000000000000000000XXX", list(range(9)))])
def test_modify_by_mask2(number, mask, result):
    modified_numbers = modify_by_mask2(number, mask)
    for required_elem, calculated_elem in zip(sorted(result), sorted(modified_numbers)):
        assert required_elem == calculated_elem, \
            f"Masked number should be {required_elem} instead of {calculated_elem}."
