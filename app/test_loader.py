from app.rules.rule_loader import RuleLoader

loader = RuleLoader()

rules = loader.load("app/rules/default_rules.yaml")

for rule in rules:
    print(rule)