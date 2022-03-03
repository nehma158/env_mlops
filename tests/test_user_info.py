import pytest
import io
from src.user_info import *

# test user email
def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'
    
# test user name
def test_user_name_with_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('nehma 158'))
    assert get_name_from_input() is None

def test_user_name_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('nehma158'))
    assert get_name_from_input() == 'nehma158'
    
# test password
def test_password_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('GeQq#d44_d'))
    assert get_password_from_input() == 'GeQq#d44_d'
    
def test_password_less_than_eight(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Ge_g4'))
    assert get_password_from_input() is None
    
def test_password_no_special_character(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('GeQqd44jfkzfez5d'))
    assert get_password_from_input() is None

def test_password_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('GeQqdjfkzfezd'))
    assert get_password_from_input() is None
    
def test_password_no_uppercase(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('aer2egf55'))
    assert get_password_from_input() is None
    
    