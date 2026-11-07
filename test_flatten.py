import pytest
from flatten import flattern

@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, [2, [3, [4,5]]], 6, [7,8,[9]]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, [2, [3, 4]], 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([[[[1]]]], [1]),
        ([[], [1, [], [2]], 3], [1, 2, 3]),
    ]
)
def test_flattern(arr, expected):
      assert flattern(arr) ==   expected    
      

def test_flattern_empty():
    assert flattern([]) == []
    
def test_flattern_single_element():
    assert flattern([1]) == [1]