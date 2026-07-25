from app.rules.rule import Rule


def test_simple_replacement():
    rule = Rule(
        name="Straße",
        pattern="Stra e",
        replacement="Straße",
    )

    text, changes = rule.apply("Stra e", 1)

    assert text == "Straße"
    assert len(changes) == 1