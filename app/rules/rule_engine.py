"""Regel-Engine."""

from app.core.change import Change
from app.rules.default_rules import DEFAULT_RULES


class RuleEngine:
    """Verarbeitet alle OCR-Regeln."""

    def apply(
        self,
        text: str,
        paragraph_number: int,
    ) -> tuple[str, list[Change]]:
        """Wendet alle Regeln auf einen Text an."""

        all_changes: list[Change] = []

        for rule in DEFAULT_RULES:
            text, changes = rule.apply(text, paragraph_number)
            all_changes.extend(changes)

        return text, all_changes