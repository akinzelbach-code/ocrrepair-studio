"""Erzeugt einen OCR-Reparaturbericht."""

from pathlib import Path

from app.core.change import Change
from collections import Counter



class ReportWriter:
    """Schreibt einen Änderungsbericht."""

    def write(
        self,
        changes: list[Change],
        filename: str = "OCRRepair_Report.txt",
    ) -> None:

        path = Path(filename)

        with path.open("w", encoding="utf-8") as file:

            file.write("OCRRepair Studio\n")
            file.write("=================\n\n")

            for change in changes:
                file.write(f"Absatz {change.paragraph}\n")
                file.write(f"Regel: {change.rule}\n")
                file.write(
                     f"{change.original} -> {change.replacement}\n\n"
    )

            counts = Counter(change.rule for change in changes)

            file.write("-----------------\n")
            file.write("Nach Regeln\n\n")

            for rule, count in sorted(counts.items()):
                file.write(f"{rule}: {count}\n")

            file.write("\n")
            file.write(f"Gesamt: {len(changes)} Änderungen\n")