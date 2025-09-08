# Eero Secure Boot Agent

An AI agent designed to help enable secure boot for new eero devices.

## Setup

This project uses `uv` for Python package management. Make sure you have `uv` installed:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

```bash
# Install dependencies
uv sync

# Install in development mode
uv pip install -e .
```

## Usage

```bash
# Run the main script
python main.py

# Or use the installed command
eero-agent
```

## Development

```bash
# Install development dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .
```

## Project Structure

```
eero-secureboot-agent/
├── main.py              # Main entry point
├── pyproject.toml       # Project configuration
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Features (Planned)

- [ ] Device discovery and identification
- [ ] Secure boot status verification
- [ ] Automated secure boot enablement
- [ ] Configuration validation
- [ ] Error handling and recovery
- [ ] Logging and monitoring
