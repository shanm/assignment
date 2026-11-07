# Conftest.py
from unittest import result

import test_add

@test_add.fixture
def sample_data():
    return {"name": "Alice", "age": 30, "city": "New York"}

#test_user.py
import test_add

def test_user_check(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    assert sample_data["city"] == "New York"
    
# PArameterized test
@test_add.mark.parameterize(a, b, result,[
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30)
])
def test_add(a, b, result):
    assert a + b == result
    
#pytest file_name.py::test_add

def num_add(a, b):
    return a + b

def test_num_add():
    assert num_add(3, 4) == 7
    
#################################
import pytest

def add(a, b):
    return a + b

@pytest.mark.parameterized(
    "a,b,expected", [
        (1, 2, 3),
        (4, 5, 9),
        (10, 20, 30)
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected
