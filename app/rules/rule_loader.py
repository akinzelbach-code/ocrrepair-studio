from pathlib import Path
import yaml

from app.rules.rule import Rule


class RuleLoader:
    """Lädt alle YAML-Regeldateien."""

    def load(self, directory: str) -> list[Rule]:
        rules = []

        root = Path(directory)

        for file in sorted(root.rglob("*.yaml")):
            with open(file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or []

            for item in data:
                rules.append(
                    Rule(
                        name=item["name"],
                        pattern=item["pattern"],
                        replacement=item["replacement"],
                        regex=item.get("regex", False),
                    )
                )

        return rules