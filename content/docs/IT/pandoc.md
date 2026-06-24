---
# === SIDEOPSÆTNING ===
title: "Pandoc"
geometry:
  - top=2cm        # margen foroven  (skær ned for mindre luft øverst)
  - bottom=2cm     # margen forneden
  - left=2.5cm     # venstre margen
  - right=2.5cm    # højre margen
papersize: a4

# === SKRIFT OG AFSTAND ===
fontsize: 11pt          # 10pt / 11pt / 12pt
linestretch: 1.15       # linjeafstand (1 = enkelt, 1.5 = halvanden)
# mainfont: "Helvetica Neue"   # kræver --pdf-engine=xelatex (se nederst)

# === SPROG (dansk orddeling) ===

# === ÆGTE TIL/FRA-KONTAKTER ===
toc: false              # true = indholdsfortegnelse forrest
toc-depth: 2            # hvor dybt indholdsfortegnelsen går
numbersections: false   # true = nummererede overskrifter (1, 1.1, ...)
colorlinks: true        # farvede links i stedet for røde bokse
linkcolor: blue
urlcolor: blue

# === EKSTRA LATEX-PAKKER (til avanceret styring) ===
header-includes:
  - \usepackage{float}     # giver [H] til at låse tabeller/billeder på plads
  - \usepackage{booktabs}  # pænere tabellinjer
---

# Cheat sheet: PDF-styring med pandoc

Kompilér med:

```bash
pandoc fil.md -o fil.pdf
```

---

## Sideskift

Skriv på en linje for sig (med tom linje over og under):

```latex
\newpage
```

- `\newpage` — almindeligt sideskift
- `\clearpage` — sideskift der også "tømmer" ventende billeder/tabeller

---

## Lodret afstand

```latex
\vspace{1cm}     % indsæt 1 cm tom plads
\vspace*{2cm}    % virker også øverst på en side
```

---

## Margener (i YAML-headeren)

Skru på `top`, `bottom`, `left`, `right` i `geometry`-blokken øverst.
Mindre `top` = mindre luft øverst på siden.

---

## Skrifttype

Standardmotoren kan ikke skifte font. Vil du have en bestemt skrifttype,
fjern `#` foran `mainfont` og kompilér med:

```bash
pandoc fil.md -o fil.pdf --pdf-engine=xelatex
```

---

## Indholdsfortegnelse og nummerering

I YAML: sæt `toc: true` og/eller `numbersections: true`.
Eller fra kommandolinjen:

```bash
pandoc fil.md -o fil.pdf --toc --number-sections
```

---

## Billeder med fast størrelse

Markdown alene ignorerer størrelse — tilføj en attribut:

```markdown
![Figurtekst](billede.png){ width=60% }
```

Vil du låse billedet præcis hvor det står, brug rå LaTeX med `[H]`
(kræver `float`-pakken, som allerede er i headeren):

```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth]{billede.png}
\caption{Figurtekst}
\end{figure}
```

---

## Tabel i fuld bredde, låst på plads

```latex
\begin{table}[H]
\centering
\resizebox{\textwidth}{!}{%
\begin{tabular}{|c|c|c|}
\hline
A & B & C \\
\hline
1 & 2 & 3 \\
\hline
\end{tabular}%
}
\caption{Tabeltekst}
\end{table}
```

---

## Hurtig oversigt: kommandolinje-flag

| Flag | Gør |
|:-----|:----|
| `--toc` | Indholdsfortegnelse |
| `--number-sections` | Nummererede overskrifter |
| `--pdf-engine=xelatex` | Tillader egne skrifttyper |
| `-V geometry:margin=2cm` | Sæt margen uden YAML |
| `--highlight-style=tango` | Farvetema til kodeblokke |
