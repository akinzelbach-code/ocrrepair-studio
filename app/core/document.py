"""Interne Repräsentation eines Dokuments."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Paragraph:
    """Ein Absatz des Dokuments."""
    text: str


@dataclass(slots=True)
class Document:
    """Das interne Dokumentmodell."""

    paragraphs: list[Paragraph] = field(default_factory=list)

    def add_paragraph(self, text: str) -> None:
        """Fügt einen Absatz hinzu."""
        self.paragraphs.append(Paragraph(text))

    @property
    def paragraph_count(self) -> int:
        """Anzahl der Absätze."""
        return len(self.paragraphs)