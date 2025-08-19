import pytest
from src.main import sort

def test_sort():
    assert sort(10, 20, 30, 5) == "STANDARD"
    assert sort(100, 200, 300, 50) == "SPECIAL"
    assert sort(1000, 2000, 3000, 500) == "REJECTED"
