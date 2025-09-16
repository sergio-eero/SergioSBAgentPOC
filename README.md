# Eero Secure Boot Agent

An AI agent designed to help enable secure boot for new eero devices.

## Setup

### Prerequisites

This project requires:
- **Node.js 20** - Required for MCP server functionality
- **Python 3.11+** - For the main application
- **uv** - For Python package management

Install the prerequisites:

```bash
# Install Node.js 20 (using nvm - recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20

# Or install Node.js 20 directly from https://nodejs.org/

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
