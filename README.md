# engie-core

![Python](https://img.shields.io/badge/python-3.14%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/freddy208/engie-core/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/badge/version-0.1.0-orange)

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
Normlize text :

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
tests/           Automated tests
docs/            Project documentations
.github/worflows  CI configuration
```


## Release

Current version `0.1.0`

This project follows sematic versionning

- Major : Incompatible API changes 
- Minor : backward-compatible features
- Patch : backward-compatible bug fixes

## Roadmap

- [x] Text utilities
- [x] CLI
- [x] Automated tests
- [x] CI pipeline
- [ ] Publish to PyPI
- [ ] Add code coverage
- [ ] Add documentation site

## License

MIT
