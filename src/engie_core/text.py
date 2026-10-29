import re
import unicodedata


def normalize_text(text: str) -> str:
    """Normalize a string by lowercasing it, removing accents and punctuation,
    and collapsing consecutive whitespace.

    Args:
        text: The text to normalize.

    Returns:
        The normalized text, or an empty string when the input is empty or
        contains only whitespace and punctuation.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    decomposed = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in decomposed if not unicodedata.combining(char)).lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def count_words(text: str) -> int:
    """Count words separated by whitespace in a string.

    Args:
        text: The text whose words should be counted.

    Returns:
        The number of whitespace-separated words. Empty or whitespace-only
        input returns zero.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    return len(text.split())


def slugify(text: str) -> str:
    """Convert a string to a lowercase, accent-free, hyphen-separated slug.

    Args:
        text: The text to convert.

    Returns:
        A slug containing ASCII letters and digits separated by hyphens.
        Input without ASCII letters or digits returns an empty string.

    Raises:
        ValueError: If ``text`` is empty.
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not text:
        raise ValueError("Text must not be empty.")

    decomposed = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in decomposed if not unicodedata.combining(char)).lower()
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
