import pytest

from engie_core.text import count_words, normalize_text, slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello world"),
        ("Python   Programming", "python programming"),
        ("  HELLO   World  ", "hello world"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize_text(text, expected):
    assert normalize_text(text) == expected


def test_normalize_text_rejects_none():
    with pytest.raises(TypeError):
        normalize_text(None)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", 2),
        ("Hello    wonderful   world", 3),
        ("", 0),
        ("   ", 0),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected


def test_count_words_rejects_none():
    with pytest.raises(TypeError):
        count_words(None)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello-world"),
        ("Special Characters!@#$%^&*()", "special-characters"),
        ("Crème brûlée à Noël", "creme-brulee-a-noel"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


@pytest.mark.parametrize(
    ("text", "exception"),
    [("", ValueError), (None, TypeError)],
)
def test_slugify_rejects_empty_or_none(text, exception):
    with pytest.raises(exception):
        slugify(text)
