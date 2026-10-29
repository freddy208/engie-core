import argparse

from engie_core.text import count_words, normalize_text, slugify


def build_parser() -> argparse.ArgumentParser:
    """Build the engie command-line interface."""
    parser = argparse.ArgumentParser(
        prog="engie", description="Text utilities for engineering and AI projects."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    normalize_parser = subparsers.add_parser(
        "normalize", help="Normalize whitespace and lowercase a text."
    )

    normalize_parser.add_argument("text", help="Text to normalize.")

    count_parser = subparsers.add_parser("count", help="Count the number of words in a text.")

    count_parser.add_argument("text", help="Text to analyze.")

    slugify_parser = subparsers.add_parser("slug", help="Convert a title into a URL-friendly slug.")
    slugify_parser.add_argument("text", help="Text to convert.")
    return parser


def main():
    """Run the engie command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "normalize":
        result = normalize_text(args.text)
        print(result)
    elif args.command == "count":
        result = count_words(args.text)
        print(result)
    elif args.command == "slug":
        result = slugify(args.text)
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
