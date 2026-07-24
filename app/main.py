"""OCRRepair Studio - Einstiegspunkt."""

from app.core.engine import RepairEngine
from app.core.engine import RepairEngine
from app.io.reader import DocumentReader
from app.io.writer import DocumentWriter

def main() -> None:
    engine = RepairEngine()
    engine.start()
    from pathlib import Path

    print(Path("examples/test.docx").resolve())
    reader = DocumentReader()
    document = reader.read("examples/test.docx")
    document = engine.repair(document)
    writer = DocumentWriter()
    writer.write(document, "examples/test_korrigiert.docx")
    print()
    print("Dokument erfolgreich gelesen.")
    print(f"Absätze: {document.paragraph_count}")

    for i, paragraph in enumerate(document.paragraphs, start=1):
        print(f"{i}: {paragraph.text}")


if __name__ == "__main__":
    main()