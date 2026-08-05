# OCRRepair Studio – Regelbibliothek

## Kategorien

| Kategorie | Beschreibung |
|-----------|--------------|
| ligatures | Ligaturen wie ﬁ, ﬂ, ﬃ |
| orthography | Rechtschreibung, Umlaute, ß |
| whitespace | Leerzeichen |
| punctuation | Satzzeichen |
| hyphenation | Silbentrennung |
| numbers | Zahlen |
| medical | Medizinische Fachbegriffe |

## Aufbau einer Regel

```yaml
- name: ligature_fi
  description: "Ersetzt die Ligatur ﬁ durch fi."
  category: "ligatures"
  pattern: "ﬁ"
  replacement: "fi"
  regex: true