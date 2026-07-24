from app.rules.rule import Rule

rule = Rule(
    name="missing_sz",
    pattern=r"Stra\s+e",
    replacement="Straße",
    regex=True,
)

tests = [
    "Stra e",
    "Stra  e",
    "Stra     e",
]

for text in tests:
    repaired, changes = rule.apply(text, 1)

    print(f"Eingabe : {text}")
    print(f"Ausgabe : {repaired}")
    print(f"Änderungen: {len(changes)}")
    print("-" * 30)