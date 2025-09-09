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
# Run the agent (interactive mode)
uv run python main.py

# Or after installing in development mode
python main.py
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
├── main.py                        # Main entry point with CLI
├── secureboot_enabled_agent.py    # Strands Agent implementation
├── input_handler.py               # User input handling
├── models.py                      # Data models (User, InputMessage)
├── pyproject.toml                 # Project configuration
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

## Features (Planned)

- [ ] Secure boot status verification
- [ ] Automated secure boot enablement
- [ ] Configuration validation
- [ ] Error handling and recovery
- [ ] Logging and monitoring
