"""Definition einer OCR-Regel."""

from dataclasses import dataclass

from app.core.change import Change


@dataclass(slots=True)
class Rule:
    """Eine einfache Ersetzungsregel."""

    name: str
    pattern: str
    replacement: str

    def apply(
        self,
        text: str,
        paragraph_number: int,
    ) -> tuple[str, list[Change]]:
        """
        Wendet die Regel auf einen Text an.

        Rückgabe:
            (neuer_text, liste_der_änderungen)
        """

        changes: list[Change] = []

        if self.pattern not in text:
            return text, changes

        count = text.count(self.pattern)

        for _ in range(count):
            changes.append(
                Change(
                    paragraph=paragraph_number,
                    rule=self.name,
                    original=self.pattern,
                    replacement=self.replacement,
                )
            )

        text = text.replace(self.pattern, self.replacement)

        return text, changes