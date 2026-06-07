import pytest
import string

from app.password_generator import generate_password


SYMBOLS = "!@#$%^&*()-_=+"


def test_password_length():
    password = generate_password(length=10)
    assert len(password) == 15


def test_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=3)


def test_password_contains_lowercase():
    password = generate_password(length=12)
    assert any(c in string.ascii_lowercase for c in password)


def test_password_contains_digits():
    password = generate_password(
        length=12,
        use_digits=True,
        use_symbols=False,
        use_uppercase=False,
    )
    assert any(c in string.digits for c in password)


def test_password_contains_symbols():
    password = generate_password(
        length=12,
        use_digits=False,
        use_symbols=True,
        use_uppercase=False,
    )
    assert any(c in SYMBOLS for c in password)


def test_password_contains_uppercase():
    password = generate_password(
        length=12,
        use_digits=False,
        use_symbols=False,
        use_uppercase=True,
    )
    assert any(c in string.ascii_uppercase for c in password)


def test_password_only_lowercase():
    password = generate_password(
        length=12,
        use_digits=False,
        use_symbols=False,
        use_uppercase=False,
    )
    assert all(c in string.ascii_lowercase for c in password)


def test_guaranteed_characters_present():
    password = generate_password(
        length=12,
        use_digits=True,
        use_symbols=True,
        use_uppercase=True,
    )

    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in SYMBOLS for c in password)
    assert any(c in string.ascii_uppercase for c in password)
