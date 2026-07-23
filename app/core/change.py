"""Beschreibt eine einzelne Änderung."""

from dataclasses import dataclass


@dataclass(slots=True)
class Change:
    """Eine durchgeführte OCR-Korrektur."""

    paragraph: int
    rule: str
    original: str
    replacement: str