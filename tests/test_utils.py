import pytest
from app.utils import format_date, sanitize_input

def test_format_date_valid():
    assert format_date("2023-01-01") == "2023-01-01"

def test_sanitize_input_removes_tags():
    assert sanitize_input("<script>alert('xss')</script>") == "alert('xss')"

def test_sanitize_input_empty():
    assert sanitize_input("") == ""
