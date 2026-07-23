"""Standardregeln."""

from app.rules.rule import Rule

DEFAULT_RULES = [
    Rule(
        name="missing_sz",
        pattern="Stra e",
        replacement="Straße",
    ),
    Rule(
        name="missing_umlaut_ae",
        pattern="Sch den",
        replacement="Schäden",
    ),
    Rule(
        name="missing_umlaut_ue",
        pattern="f r",
        replacement="für",
    ),
    Rule(
        name="published",
        pattern="ver ffentlicht",
        replacement="veröffentlicht",
    ),
]