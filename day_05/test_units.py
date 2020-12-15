import pytest

from task import extract_row_and_col

@pytest.mark.parametrize("encoded_seat, row, col",
                          [("FBFBBFFRLR", 44, 5),
                           ("BFFFBBFRRR", 70, 7),
                           ("FFFBBBFRRR", 14, 7),
                           ("BBFFBBFRLL", 102, 4),
                           ("BBBBBBBRRR", 127, 7),
                           ("FFFFFFFLLL", 0, 0),
                           ("FFFFBBFRLL", 6, 4),
                           ("FFFFBBFLLL", 6, 0)])
def test_extract_row_and_col_from_encoded_seat(encoded_seat, row, col):
    extracted_row, extracted_col = extract_row_and_col(encoded_seat)
    assert row == extracted_row, f"Row should be {row} instead of {extracted_row} in case of {encoded_seat}"
    assert col == extracted_col, f"Column should be {col} instead of {extracted_col} in case of {encoded_seat}"            
