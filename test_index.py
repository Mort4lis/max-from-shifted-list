import pytest

from index import max_from_shifted_list


@pytest.mark.parametrize('arr', [
    [1],
    [5, 2],
    [5, 5, 5],
    [7, 5, 6],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [4, 5, 7, 8, 9, 10, 1, 2, 3],
    [8, 9, 10, 1, 2, 3, 4, 5, 7],
    [50, 40, 35, 20, 1, 5, 6, 8, 10, 12, 15, 40],
    [45, 46, 51, 60, 61, 1, 5, 10, 15, 20, 35, 40]
])
def test_max_from_shifted_list(arr):
    assert max_from_shifted_list(arr) == max(arr)


def test_max_from_shifted_empty_list():
    with pytest.raises(ValueError):
        assert max_from_shifted_list([])
