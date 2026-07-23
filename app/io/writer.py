"""DOCX-Dateien schreiben."""

from docx import Document as WordDocument

from app.core.document import Document


class DocumentWriter:
    """Schreibt ein Word-Dokument."""

    def write(self, document: Document, filename: str) -> None:
        word = WordDocument()

        for paragraph in document.paragraphs:
            word.add_paragraph(paragraph.text)

        word.save(filename)