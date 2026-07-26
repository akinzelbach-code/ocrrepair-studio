import pytest
from app.rules.exceptions import RuleValidationError
from app.rules.rule_loader import RuleLoader


def test_rule_loader_loads_temporary_yaml(tmp_path):
    yaml_file = tmp_path / "rules.yaml"

    yaml_file.write_text(
        """
- name: test_rule
  description: Testregel
  category: test
  pattern: Test
  replacement: Prüfung
""",
        encoding="utf-8",
    )

    loader = RuleLoader()

    rules = loader.load(str(tmp_path))

    assert len(rules) == 1

    rule = rules[0]

    assert rule.name == "test_rule"
    assert rule.pattern == "Test"
    assert rule.replacement == "Prüfung"
    assert rule.regex is False
    assert rule.description == "Testregel"
    assert rule.category == "test"

def test_rule_loader_missing_replacement(tmp_path):
    yaml_file = tmp_path / "rules.yaml"

    yaml_file.write_text(
        """
- name: test_rule
  description: Testregel
  category: test
  pattern: Test
  
""",
        encoding="utf-8",
    )

    loader = RuleLoader()

    with pytest.raises(RuleValidationError) as exc_info:
        loader.load(str(tmp_path))

    assert "replacement" in str(exc_info.value)
    assert "rules.yaml" in str(exc_info.value)
   