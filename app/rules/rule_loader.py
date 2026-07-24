"""Lädt OCR-Regeln aus einer YAML-Datei."""

from pathlib import Path

import yaml

from app.rules.rule import Rule


class RuleLoader:
    """Lädt Regeln aus YAML."""

    def load(self) -> list[Rule]:
        yaml_file = Path(__file__).parent / "default_rules.yaml"

        with yaml_file.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return [
    Rule(
        name=item["name"],
        pattern=item["pattern"],
        replacement=item["replacement"],
        regex=item.get("regex", False),
    )
    for item in data
]
        