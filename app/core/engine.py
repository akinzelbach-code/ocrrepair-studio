"""Kern der OCR-Reparatur."""

from dataclasses import dataclass, field
from app.logger import logger
from app import config
from app.core.document import Document
from app.core.report import ReportWriter
from app.rules.rule_engine import RuleEngine
from app.rules.rule_loader import RuleLoader


@dataclass(slots=True)
class RepairEngine:
    """Zentrale Steuerung der Reparatur."""

    name: str = config.APP_NAME
    version: str = config.VERSION

    rule_engine: RuleEngine = field(init=False)

    def __post_init__(self) -> None:
        loader = RuleLoader()
        loaded_rules = loader.load(config.RULES_DIR)
        self.rule_engine = RuleEngine(loaded_rules)

    def start(self) -> None:
        
        logger.info("%s %s", self.name, self.version)
        logger.info("Repair Engine gestartet.")

    def repair(self, document: Document) -> Document:
        """Repariert ein Dokument."""

        all_changes = []

        for paragraph_number, paragraph in enumerate(document.paragraphs, start=1):
            paragraph.text, changes = self.rule_engine.apply(
                paragraph.text,
                paragraph_number,
            )
            all_changes.extend(changes)

        report = ReportWriter()
        report.write(all_changes)

        logger.info("Änderungen: %d", len(all_changes))
        logger.info("Bericht gespeichert: %s", config.REPORT_FILE)

        return document