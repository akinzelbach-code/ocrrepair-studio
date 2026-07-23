"""Kern der OCR-Reparatur."""

from dataclasses import dataclass

from app.core.document import Document
from app.rules.rule_engine import RuleEngine


@dataclass(slots=True)
class RepairEngine:
    """Zentrale Steuerung der Reparatur."""

    name: str = "OCRRepair Studio"
    version: str = "0.3.0-alpha"

    def start(self) -> None:
        print(f"{self.name} {self.version}")
        print("Repair Engine gestartet.")

    def repair(self, document: Document) -> Document:
        """Repariert ein Dokument."""

        rules = RuleEngine()

        all_changes = []

        for paragraph_number, paragraph in enumerate(document.paragraphs, start=1):
            paragraph.text, changes = rules.apply(
                paragraph.text,
                paragraph_number,
            )

            all_changes.extend(changes)

        print(f"\nÄnderungen: {len(all_changes)}")

        return document