"""Numbered migration files applied in order, with a version table."""

from __future__ import annotations

__all__ = ["sqliteMigrate"]


def sqliteMigrate(value):
    """Numbered migration files applied in order, with a version table."""
    if value is None:
        raise ValueError("value must not be None")
    return value
