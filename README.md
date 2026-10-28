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
source .venv/bin/activate #ubuntu version
pip install -e .
```
## Usage

```bash
from engie_core.text import normalize_text
print(normalize_text("  Hello  World   "))
```

## Development

```bash
ruff check .
pytest -q

```
