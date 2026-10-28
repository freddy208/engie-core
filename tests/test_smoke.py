from engie_core.text import count_words, normalize_text, slugify


def test_normalize_text():
    assert normalize_text("  Hello World  ") == "hello world"
    assert normalize_text("Python   Programming") == "python programming"
    assert normalize_text("   Leading and trailing spaces   ") == "leading and trailing spaces"
    assert normalize_text("Multiple     spaces") == "multiple spaces"

def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("Python Programming Language") == 3
    assert count_words("   Leading and trailing spaces   ") == 4
    assert count_words("Multiple     spaces") == 2

def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("Python Programming Language") == "python-programming-language"
    assert slugify("   Leading and trailing spaces   ") == "leading-and-trailing-spaces"
    assert slugify("Multiple     spaces") == "multiple-spaces"
    assert slugify("Special Characters!@#$%^&*()") == "special-characters"