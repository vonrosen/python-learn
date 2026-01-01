import pytest
from quick_sort import quick_sort

@pytest.mark.parametrize("a, expected", [
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([1,2,3,4],[1,2,3,4]),
    ([],[]),
    ([11],[11]),
    ([11,1],[1,11]),
])
def test_sort_desc_arr(a, expected):
    quick_sort(a)
    assert a == expected
