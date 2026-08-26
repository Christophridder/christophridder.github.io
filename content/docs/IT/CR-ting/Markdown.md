---
title: "Markdown"
date: 2025-05-29
draft: true
weight: 1
---

## Overskrifter

| Syntax | Resultat |
| --- | --- |
| `# Overskrift` | H1 |
| `## Overskrift` | H2 |
| `### Overskrift` | H3 |
| `#### Overskrift` | H4 |

## Tekstformatering

| Syntax | Resultat |
| --- | --- |
| `**fed**` | **fed** |
| `*kursiv*` | *kursiv* |
| `***fed kursiv***` | ***fed kursiv*** |
| `~~gennemstreg~~` | ~~gennemstreg~~ |
| `` `inline kode` `` | `inline kode` |
| `> citat` | Blokcitat |
| `---` | Vandret linje |

## Lister

| Syntax | Resultat |
| --- | --- |
| `- punkt` | Uordnet liste |
| `1. punkt` | Ordnet liste |
| `  - underpunkt` | Indrykning (2 spaces) |
| `- [x] opgave` | Afkrydset opgave |
| `- [ ] opgave` | Ikke afkrydset opgave |

## Links & billeder

| Syntax | Beskrivelse |
| --- | --- |
| `[tekst](url)` | Link |
| `![alt](billede.png)` | Billede |
| `[tekst](url "titel")` | Link med titel |
| `<https://url>` | Autolink |

## Kodeblok

\`\`\`python
# Skriv dit sprog efter de tre backticks
print("hello world")
\`\`\`

## Tabel

```
| Kolonne 1 | Kolonne 2 |
| --------- | --------- |
| :---      | ---:      |
```

| `:---` | Venstrejusteret |
| `---:` | Højrejusteret |
| `:---:` | Centreret |

## Front matter

```yaml
---
title: "Min side"
date: 2025-01-01
draft: false
---
```
