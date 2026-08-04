from pathlib import Path

from app.core.change import Change
from app.core.report import ReportWriter
from collections import Counter



def test_report_writer_creates_report(tmp_path):
    changes = [
        Change(
            paragraph=1,
            rule="fi_ligature",
            original="ﬁ",
            replacement="fi",
        ),
        Change(
            paragraph=2,
            rule="double_space",
            original="  ",
            replacement=" ",
        ),
    ]
    counts = Counter(change.rule for change in changes)
    
    filename = tmp_path / "report.txt"

    ReportWriter().write(changes, filename)

    content = filename.read_text(encoding="utf-8")

    assert "OCRRepair Studio" in content
    assert "fi_ligature" in content
    assert "double_space" in content

    assert "Gesamt: 2 Änderungen" in content
    assert "Nach Regeln" in content
