# engie-core

I professional  python foundation for building reliable engineering and AI projects.

## Features

- Text normalization utilities
- Word counting
- URL slug generation
- Clean code structure
- Automated linting and testing

## Installation

```bash
git clone https://github.com/freddy208/engie-core.git
cd engie-core
python -m venv .venv
source .venv/bin/activate # ubuntu version
pip install -e .
```
## Usage

```bash
from engie_core.text import normalize_text
print(normalize_text("  Hello  World   "))
print(count_words("Je suis ingénieur"))
print(slugify("Master Génie Logiciel & IA"))
```

## Development

```bash
pip install -e ".[dev]"
ruff check .
pytest -v
pytest -q

```

## CLI usage

After installing the package :

```bash
engie --hlep
```
NormLalize text :

```bash
engie normalize " Welcome to Cameroon "
```
Count words :

```bash
engie count " Peace Work Fatherland  "
```

Create a slug URL :

```bash
engie slug " students tech 21987"
```

## Error handling

The CLI validates user input and returns clean error messages when the input is invalid.

## Project structure

```bash
src/engie_core   Source code
tests/      Automated tests   
docs/       Project documentations
.github/worflows  CI configuration
```

## License

MIT
