from pathlib import Path

import yaml

from app.rules.exceptions import RuleValidationError
from app.rules.rule import Rule


REQUIRED_FIELDS = (
    "name",
    "description",
    "category",
    "pattern",
    "replacement",
)


class RuleLoader:
    """Lädt alle YAML-Regeldateien."""

    def load(self, directory: str) -> list[Rule]:
        rules = []

        root = Path(directory)

        for file in sorted(root.rglob("*.yaml")):
            with open(file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or []

            for item in data:
                # Regel validieren
                for field in REQUIRED_FIELDS:
                    if field not in item:
                        raise RuleValidationError(
                            f"Invalid rule in '{file.name}': "
                            f"missing required field '{field}'"
                        )

                # Regel erzeugen
                rules.append(
                    Rule(
                        name=item["name"],
                        description=item["description"],
                        category=item["category"],
                        pattern=item["pattern"],
                        replacement=item["replacement"],
                        regex=item.get("regex", False),
                    )
                )

        return rules