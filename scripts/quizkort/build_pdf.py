"""Laver print-PDF med quiz-og-byt kort (2 x 4 pr. A4) ud fra data/quiz/<navn>.yaml
Kør fra crsite-roden:  python3 scripts/quizkort/build_pdf.py integration
Resultat: static/pdfs/quiz-<navn>.pdf"""
import os, re, sys, subprocess, tempfile, shutil
import yaml

navn = sys.argv[1] if len(sys.argv) > 1 else "integration"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
data = yaml.safe_load(open(os.path.join(ROOT, "data", "quiz", f"{navn}.yaml"), encoding="utf-8"))
IMG = os.path.join(ROOT, "static", "img", f"quiz-{navn}")  # grafer/billeder: <navn>.pdf til print, <navn>.svg til web
OUTPDF = os.path.join(ROOT, "static", "pdfs", f"quiz-{navn}.pdf")

# Kategorier: kan defineres i YAML under "typer" (navn: {label, farve}); ellers bruges standarden
STD_TYPER = {"graf": {"label": "Aflæs grafen", "farve": "2471A3"},
             "begreb": {"label": "Begreb", "farve": "1E8449"},
             "funktion": {"label": "Integrér", "farve": "CA6F1E"}}
TYPER = data.get("typer") or STD_TYPER
ERSTAT = {"·": r"$\cdot$", "→": r"$\rightarrow$", "✓": r"$\checkmark$", "²": r"$^2$", "³": r"$^3$",
          "½": r"$\tfrac{1}{2}$", "–": "--", "…": r"\dots{}", "%": r"\%", "&": r"\&", "#": r"\#"}

def tex(s):
    """Tekst -> LaTeX. Matematik mellem $...$ bevares; resten får specialtegn erstattet."""
    s = str(s)
    dele = re.split(r"(\$[^$]+\$)", s)
    ud = []
    for d in dele:
        if d.startswith("$") and d.endswith("$") and len(d) > 1:
            ud.append(d)
        else:
            d = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", d)
            for a, b in ERSTAT.items():
                d = d.replace(a, b)
            ud.append(d)
    return "".join(ud)

W, H = 105.0, 297.0 / 4   # kortstørrelse i mm
pages = []
kort = sorted(data["kort"], key=lambda k: k["nr"])
for i in range(0, len(kort), 8):
    pages.append(kort[i:i + 8])

def card(k, col, row):
    x0, y0 = col * W, row * H           # øverste venstre hjørne (y nedad)
    typ = TYPER.get(k["type"], {}).get("label", k["type"])
    farve = "type" + re.sub(r"[^a-zA-Z]", "", k["type"])
    badge = rf"\colorbox{{{farve}}}{{\color{{white}}\sffamily\bfseries\footnotesize\,{k['nr']}\ \ {typ}\,}}"
    maerke = k.get("maerke") or ("enhed" if k.get("enhed") else None)
    if maerke:
        badge += rf"\ \colorbox{{enhed}}{{\sffamily\bfseries\footnotesize\,{tex(maerke)}\,}}"
    har_bill = bool(k.get("billede"))
    spm_str = r"\small" if har_bill else r"\Large"
    bill = ""
    if har_bill:
        bill = rf"\par\vspace{{1mm}}\centering\includegraphics[height=37mm,width=90mm,keepaspectratio]{{{os.path.join(IMG, k['billede'])}.pdf}}"
    body = (rf"\begin{{minipage}}[t][{H-24:.1f}mm][t]{{{W-10:.1f}mm}}{badge}\par\vspace{{{1.5 if har_bill else 4}mm}}"
            rf"{{{spm_str}\raggedright {tex(k['spm'])}\par}}{bill}\end{{minipage}}")
    svar = (rf"\rotatebox{{180}}{{\begin{{minipage}}[c][14mm][c]{{{W-14:.1f}mm}}\footnotesize\raggedright"
            rf"\textbf{{Svar:}} {tex(k['svar'])}"
            + (rf"\par\vspace{{0.6mm}}{{\scriptsize\color{{black!65}}\textbf{{Hint:}} {tex(k['hint'])}}}" if k.get('hint') else "")
            + r"\end{minipage}}")
    return rf"""
\node[anchor=north west,inner sep=0] at ([xshift={x0+5}mm,yshift=-{y0+4}mm]current page.north west) {{{body}}};
\fill[svarbg] ([xshift={x0+3}mm,yshift=-{y0+H-3}mm]current page.north west) rectangle ([xshift={x0+W-3}mm,yshift=-{y0+H-19}mm]current page.north west);
\node[anchor=center,inner sep=0] at ([xshift={x0+W/2}mm,yshift=-{y0+H-11}mm]current page.north west) {{{svar}}};
"""

doc = [r"""\documentclass[a4paper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,graphicx,tikz,xcolor}
""" + "".join(rf"\definecolor{{type{re.sub(r'[^a-zA-Z]', '', n)}}}{{HTML}}{{{str(t.get('farve','2471A3')).lstrip('#')}}}" for n, t in TYPER.items()) + r"""
\definecolor{enhed}{HTML}{F9E79F}\definecolor{svarbg}{HTML}{EAF2F8}
\pagestyle{empty}\setlength{\parindent}{0pt}
\begin{document}"""]
for p in pages:
    doc.append(r"\null\begin{tikzpicture}[remember picture,overlay]")
    # klippelinjer
    doc.append(r"\draw[black!35,dashed,line width=0.3pt] (current page.north) -- (current page.south);")
    for r in range(1, 4):
        doc.append(rf"\draw[black!35,dashed,line width=0.3pt] ([yshift=-{r*H}mm]current page.north west) -- ([yshift=-{r*H}mm]current page.north east);")
    for j, k in enumerate(p):
        doc.append(card(k, j % 2, j // 2))
    doc.append(rf"\node[anchor=south,font=\tiny\sffamily,text=black!40] at ([yshift=1mm]current page.south) {{{tex(data['titel'])}}};")
    doc.append(r"\end{tikzpicture}\newpage")
doc.append(r"\end{document}")

tmp = tempfile.mkdtemp()
with open(os.path.join(tmp, "kort.tex"), "w", encoding="utf-8") as f:
    f.write("\n".join(doc))
for _ in range(2):  # to gennemløb, så tikz kan placere kortene på siden
    r = subprocess.run(["xelatex", "-interaction=nonstopmode", "kort.tex"], cwd=tmp, capture_output=True, text=True)
if r.returncode != 0 or not os.path.exists(os.path.join(tmp, "kort.pdf")):
    print(r.stdout[-3000:]); sys.exit(f"Fejl – se {tmp}/kort.log")
shutil.copy(os.path.join(tmp, "kort.pdf"), OUTPDF)
print("Skrevet:", OUTPDF)
