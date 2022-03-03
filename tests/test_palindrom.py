import pytest
from palindrom import *

def test_palindrom_correct():
    assert is_palindrom('kayak'), 'Kayak should be a palindrom'
    
def test_palindrom_not_correct():
    assert not is_palindrom('bateau'), 'bateau is not a palindrom'