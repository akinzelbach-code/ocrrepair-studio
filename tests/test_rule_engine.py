from app.rules.rule import Rule
from app.rules.rule_engine import RuleEngine


def test_rule_engine_applies_all_rules():
    rules = [
        Rule(
            name="street",
            pattern="Stra e",
            replacement="Straße",
        ),
        Rule(
            name="opening",
            pattern="Offnung",
            replacement="Öffnung",
        ),
    ]

    engine = RuleEngine(rules)

    text, changes = engine.apply(
        "Stra e und Offnung",
        1,
    )

    assert text == "Straße und Öffnung"
    assert len(changes) == 2