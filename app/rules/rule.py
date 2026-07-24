"""Definition einer OCR-Regel."""

import re
from dataclasses import dataclass

from app.core.change import Change


@dataclass(slots=True)
class Rule:
    name: str
    pattern: str
    replacement: str
    regex: bool = False

    def apply(
        self,
        text: str,
        paragraph_number: int,
    ) -> tuple[str, list[Change]]:
        """Wendet die Regel auf einen Text an."""

        changes: list[Change] = []

        if self.regex:
            matches = list(re.finditer(self.pattern, text))

            if not matches:
                return text, changes

            for _ in matches:
                changes.append(
                    Change(
                        paragraph=paragraph_number,
                        rule=self.name,
                        original=self.pattern,
                        replacement=self.replacement,
                    )
                )

            text = re.sub(self.pattern, self.replacement, text)

        else:
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