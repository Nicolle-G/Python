import pytest
from proyecto.main import is_palindrome

@pytest.mark.parametrize(
    "word, expected",
    [
    ("oño", True),
    ("house", False)
    ],
)  

def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected