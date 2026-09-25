"""crsite-side (.md) -> PDF med blå bjælke, som de andre PDF'er.
Kør fra crsite-roden:
    python3 scripts/pdf/md2pdf.py content/docs/mat/integration-i-fysik.md
Undertitlen i bjælken tages fra linjen '**Niveau: ...** · **Emne: ...**' (eller angiv selv: --sub "tekst").
PDF-navnet tages fra 'pdf:' i front matter (ellers static/pdfs/<filnavn>.pdf)."""
import os, re, sys, subprocess, tempfile, argparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ap = argparse.ArgumentParser(); ap.add_argument("md"); ap.add_argument("--sub", default=None)
a = ap.parse_args()
src = open(a.md, encoding="utf-8").read()

fm = re.match(r"^---\n(.*?)\n---\n", src, re.S)
front, body = (fm.group(1), src[fm.end():]) if fm else ("", src)
title = (re.search(r'^title:\s*"?(.*?)"?\s*$', front, re.M) or [None, "Uden titel"])[1]
pdfm = re.search(r'^pdf:\s*"?(.*?)"?\s*$', front, re.M)
out = os.path.join(ROOT, "static", pdfm.group(1) if pdfm else f"pdfs/{os.path.splitext(os.path.basename(a.md))[0]}.pdf")

# Mangler 'pdf:' i front matter? Så skriv den ind i .md-filen, så siden får den blå PDF-bjælke på hjemmesiden
if fm and not pdfm:
    rel = os.path.relpath(out, os.path.join(ROOT, "static")).replace(os.sep, "/")
    ny_front = front.rstrip("\n") + f'\npdf: "{rel}"\npdf_ny_fane: true'
    open(a.md, "w", encoding="utf-8").write(f"---\n{ny_front}\n---\n" + src[fm.end():])
    print(f"Tilføjede 'pdf: \"{rel}\"' og 'pdf_ny_fane: true' til {a.md}")

# Undertitel fra Niveau/Emne-linjen (fjernes fra brødteksten)
sub = a.sub
m = re.search(r"^\*\*Niveau:.*$", body, re.M)
if m:
    if sub is None:
        sub = re.sub(r"\*\*", "", m.group(0)).replace(" · ", r" \quad ")
    body = body[:m.start()] + body[m.end():]
sub = sub or ""

# Hugo -> pandoc: shortcodes væk, relref-links til tekst, blanke linjer før overskrifter/lister
body = re.sub(r"\[([^\]]+)\]\(\{\{<\s*relref[^>]*>\}\}\)", r"\1", body)
body = re.sub(r"\{\{[<%].*?[>%]\}\}", "", body)
tmp = tempfile.mkdtemp()
def billede(m):
    """/img/x.svg -> PDF (LaTeX kan ikke læse SVG). Bruger x.pdf hvis den findes, ellers rsvg-convert eller cairosvg."""
    alt, sti = m.group(1), os.path.join(ROOT, "static", m.group(2).lstrip("/"))
    if sti.endswith(".svg"):
        pdf = sti[:-4] + ".pdf"
        if not os.path.exists(pdf):
            pdf = os.path.join(tmp, os.path.basename(sti)[:-4] + ".pdf")
            if subprocess.run(["which", "rsvg-convert"], capture_output=True).returncode == 0:
                subprocess.run(["rsvg-convert", "-f", "pdf", "-o", pdf, sti], check=True)
            else:
                import cairosvg  # pip install cairosvg
                cairosvg.svg2pdf(url=sti, write_to=pdf)
        sti = pdf
    return f"![{alt}]({sti})"
body = re.sub(r"!\[([^\]]*)\]\((/img/[^)\s]+)\)", billede, body)
lines, fixed = body.splitlines(), []
islist = lambda l: re.match(r"\s*([-*]|\d+\.)\s", l)
infence = False
for l in lines:
    if l.startswith("```"): infence = not infence
    # Vandrette streger (---, ***, ___) mellem afsnit droppes i PDF'en (de bliver på hjemmesiden)
    if not infence and re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", l): continue
    if not infence and fixed and fixed[-1].strip():
        if l.startswith("#") or (islist(l) and not islist(fixed[-1])): fixed.append("")
    fixed.append(l)
    if not infence and l.startswith("#"): fixed.append("")
body = "\n".join(fixed)
# Unicode-sænket skrift (CO₂) -> pandoc-subscript
for k, v in {"₀":"0","₁":"1","₂":"2","₃":"3","₄":"4","₅":"5","₆":"6","₇":"7","₈":"8","₉":"9"}.items():
    body = body.replace(k, "~" + v + "~")
body = body.replace("~~", "")

# mhchem: brug pakken hvis TeX har den; ellers advar og lav simple \ce{} om til \mathrm med subscripts
har_mhchem = subprocess.run(["kpsewhich", "mhchem.sty"], capture_output=True, text=True).stdout.strip() != ""
if not har_mhchem and r"\ce{" in body:
    print("ADVARSEL: mhchem.sty mangler i din TeX -> installér med:  sudo tlmgr install mhchem\n"
          "          Indtil da laves simple \\ce{}-formler om til \\mathrm{} (kun tal -> subscript).", file=sys.stderr)
    def ce2mathrm(m):
        f = re.sub(r"(?<=[A-Za-z)\]])(\d+)", r"_{\1}", m.group(1))
        return r"\mathrm{" + f + "}"
    body = re.sub(r"\\ce\{([^{}]*)\}", ce2mathrm, body)

header = r"""\usepackage{xcolor}\definecolor{barblue}{HTML}{3498DB}\definecolor{headblue}{HTML}{2471A3}
MHCHEM\usepackage{tikz}\usepackage{titlesec}\usepackage{float}\usepackage{booktabs}
\titleformat*{\section}{\Large\bfseries\sffamily\color{headblue}}
\titleformat*{\subsection}{\large\bfseries\sffamily\color{headblue}}
\titleformat*{\subsubsection}{\normalsize\bfseries\sffamily\color{headblue}}
\AtBeginDocument{\hypersetup{colorlinks=true,urlcolor=headblue,linkcolor=headblue}}% nyere pandoc indlæser hyperref efter -H
\makeatletter\renewcommand{\maketitle}{%
\begin{tikzpicture}[remember picture,overlay]
\fill[barblue] (current page.north west) rectangle ([yshift=-24mm]current page.north east);
\node[anchor=north west,text=white,font=\sffamily\bfseries\LARGE] at ([xshift=12mm,yshift=-5mm]current page.north west) {\@title};
\node[anchor=north west,text=white,font=\sffamily\small] at ([xshift=12mm,yshift=-15mm]current page.north west) {SUBTITLE};
\end{tikzpicture}\vspace*{8mm}}\makeatother
""".replace("SUBTITLE", sub).replace("MHCHEM", r"\usepackage[version=4]{mhchem}" if har_mhchem else r"\providecommand{\ce}[1]{\mathrm{#1}}")

open(os.path.join(tmp, "h.tex"), "w").write(header)
open(os.path.join(tmp, "in.md"), "w").write(f'---\ntitle: "{title}"\n---\n' + body)
r = subprocess.run(["pandoc", "in.md", "-f", "markdown-auto_identifiers", "-o", out, "--pdf-engine=xelatex",
                    "-H", "h.tex", "-V", "lang=da", "-V", "fontsize=11pt",
                    "-V", "geometry:top=30mm,bottom=22mm,left=22mm,right=22mm"], cwd=tmp, capture_output=True, text=True)
if r.returncode: sys.exit(r.stderr)
print("Skrevet:", out)
