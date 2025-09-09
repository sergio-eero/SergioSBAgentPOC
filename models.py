"""Data models for the eero secure boot agent."""

from dataclasses import dataclass


@dataclass
class User:
    """Represents a user interacting with the agent."""
    role: str = "operator"


@dataclass
class InputMessage:
    """Represents an input message from a user."""
    raw_string: str
    user: User
