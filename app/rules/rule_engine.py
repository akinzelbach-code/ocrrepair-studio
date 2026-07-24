"""Regel-Engine."""

from app.core.change import Change
from app.rules.rule_loader import RuleLoader


class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def apply(
        self,
        text: str,
        paragraph_number: int,
    ) -> tuple[str, list[Change]]:
        """Wendet alle Regeln auf einen Text an."""

        all_changes: list[Change] = []

        for rule in self.rules:
            text, changes = rule.apply(text, paragraph_number)
            all_changes.extend(changes)

        return text, all_changes