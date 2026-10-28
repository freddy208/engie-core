import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize the input text by removing extra spaces and converting it to lowercase.

    Args:
        text (str): The input string.

    Returns:
        str: The normalized text.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    return " ".join(text.lower().split())


def count_words(text: str) -> int:
    """
    Count the number of words in the input text.

    Args:
        text (str): The input string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    return len(text.split())


def slugify(text: str) -> str:
    """
    Convert the input text into a slug format (lowercase, hyphen-separated).

    Args:
        text (str): The input string.

    Returns:
        str: The slugified text.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    text = text.lower()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")

    return text
