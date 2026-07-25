import pytest

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


@pytest.mark.parametrize(
    "pattern,replacement,input_text,expected",
    [
        ("ﬁ", "fi", "ﬁnden", "finden"),
        ("ﬂ", "fl", "ﬂiegen", "fliegen"),
        ("ﬀ", "ff", "Auﬀassung", "Auffassung"),
        ("ﬃ", "ffi", "Suﬃx", "Suffix"),
        ("ﬄ", "ffl", "Staﬄel", "Stafflel"),
    ],
)
def test_ligatures(pattern, replacement, input_text, expected):
    rule = Rule(
        name="ligature",
        pattern=pattern,
        replacement=replacement,
    )

    text, changes = rule.apply(input_text, 1)

    assert text == expected
    assert len(changes) == 1


def test_no_match():
    rule = Rule(
        name="ligature",
        pattern="ﬁ",
        replacement="fi",
    )

    text, changes = rule.apply("finden", 1)

    assert text == "finden"
    assert changes == []


def test_multiple_matches():
    rule = Rule(
        name="ligature",
        pattern="ﬁ",
        replacement="fi",
    )

    text, changes = rule.apply("ﬁnden und ﬁltern", 1)

    assert text == "finden und filtern"
    assert len(changes) == 2

def test_regex_replacement():
    rule = Rule(
        name="digits",
        pattern=r"\d+",
        replacement="#",
        regex=True,
    )

    text, changes = rule.apply(
        "Es gibt 12 Patienten und 5 Ärzte.",
        1,
    )

    assert text == "Es gibt # Patienten und # Ärzte."
    assert len(changes) == 2