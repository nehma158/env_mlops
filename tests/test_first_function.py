import pytest
from first_function import *

# Test 
def test_wrong_answer():
    assert func(3) != 5

def test_correct_answer():
    assert func(3) == 4