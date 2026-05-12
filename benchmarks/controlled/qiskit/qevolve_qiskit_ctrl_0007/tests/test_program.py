from src.program import square, compute_squares


def test_square_single():
    assert square(3) == 9
    assert square(0) == 0


def test_compute_squares_list():
    values = [0, 1, 2, 3]
    result = compute_squares(values)
    assert isinstance(result, list)
    assert result == [0, 1, 4, 9]
