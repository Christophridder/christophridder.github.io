"""Figurer til Kemi B – Gasligevægte: gaskamre med molekyler og partialtryk.
Kør fra crsite-roden:  python3 scripts/figurer/gasligevaegte.py
Output: static/img/gasligevaegte/*.svg (indsættes med shortcoden gaskammer)"""
import os
import math
import random
from html import escape

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "static", "img", "gasligevaegte")
os.makedirs(OUT, exist_ok=True)
MORK, GRA = "#1e293b", "#64748b"
ATOM = {"N": ("#2563eb", 8), "O": ("#ef4444", 7), "Br": ("#92400e", 9),
        "H": ("#e2e8f0", 5), "I": ("#7c3aed", 10)}
MOLEKYLE = {"NO": "NO", "Br2": ["Br", "Br"], "NOBr": ["N", "O", "Br"],
            "H2": "HH", "I2": "II", "HI": "HI"}
NAVN = {"NO": "NO", "Br2": "Br₂", "NOBr": "NOBr", "H2": "H₂", "I2": "I₂", "HI": "HI"}
FARVE = {"NO": "#2563eb", "Br2": "#92400e", "NOBr": "#15803d", "H2": "#64748b", "I2": "#7c3aed", "HI": "#be185d"}


def komma(p):
    return f"{p:.1f}".replace(".", ",")


def tegn_molekyle(navn, x, y, vinkel=0):
    ud, cx = f'<g transform="translate({x:.1f} {y:.1f}) rotate({vinkel:.0f}) scale(.72)">', 0
    atomer = list(MOLEKYLE[navn])
    pos, cur = [], 0
    for i, a in enumerate(atomer):
        r = ATOM[a][1]
        if i:
            cur += ATOM[atomer[i - 1]][1] * .75 + r * .75
        pos.append(cur)
    midt = cur / 2
    for a, p in zip(atomer, pos):
        f, r = ATOM[a]
        ud += f'<circle cx="{p-midt:.1f}" cy="0" r="{r}" fill="{f}" stroke="{MORK}" stroke-width="1"/>'
    return ud + "</g>"


def placer(antal, x, y, b, h, rng):
    """Lægger molekylerne i et rystet gitter, så de ikke overlapper."""
    alle = [n for n, k in antal.items() for _ in range(k)]
    rng.shuffle(alle)
    kol = math.ceil(math.sqrt(len(alle) * b / h))
    rk = math.ceil(len(alle) / kol)
    bc, hc = (b - 16) / kol, (h - 12) / rk
    celler = [(i, j) for j in range(rk) for i in range(kol)]
    rng.shuffle(celler)
    ud = ""
    for n, (i, j) in zip(alle, celler):
        px = x + 8 + bc * (i + .5) + rng.uniform(-.14, .14) * bc
        py = y + 6 + hc * (j + .5) + rng.uniform(-.14, .14) * hc
        ud += tegn_molekyle(n, px, py, rng.uniform(-35, 35))
    return ud


def kammer(ox, titel, antal, faktor, Y, fuld_h, hover, rng, pr_molekyle=.1):
    b, bund = 250, 330
    h = fuld_h
    top = bund - h
    s = f'<g class="gk" tabindex="0" data-t="{escape(hover, quote=True)}"><rect class="gk-hit" x="{ox-15}" y="4" width="290" height="486" rx="10"/>'
    s += f'<text x="{ox+b/2}" y="28" font-size="18" font-weight="bold" fill="{MORK}" text-anchor="middle">{titel}</text>'
    s += f'<rect x="{ox}" y="{top}" width="{b}" height="{h}" fill="#f8fafc"/>'
    s += f'<rect x="{ox+b/2-5}" y="44" width="10" height="{top-56}" fill="{GRA}"/>'
    s += f'<rect x="{ox}" y="{top-12}" width="{b}" height="12" fill="{GRA}"/>'
    s += f'<path d="M{ox} 48 V{bund} H{ox+b} V48" fill="none" stroke="{MORK}" stroke-width="4"/>'
    s += placer(antal, ox, top, b, h, rng)
    # Partialtryk som søjler
    y = 356
    for n, k in antal.items():
        p = k * pr_molekyle * faktor
        s += f'<text x="{ox}" y="{y+12}" font-size="15" fill="{FARVE[n]}" font-weight="bold">{NAVN[n]}</text>'
        s += f'<rect x="{ox+52}" y="{y}" width="{p*36:.1f}" height="15" fill="{FARVE[n]}"/>'
        s += f'<text x="{ox+58+p*36:.1f}" y="{y+13}" font-size="14" fill="{MORK}">{komma(p)} bar</text>'
        y += 24
    ptot = sum(antal.values()) * pr_molekyle * faktor
    s += f'<text x="{ox}" y="{y+12}" font-size="15" fill="{MORK}">p(total) = {komma(ptot)} bar</text>'
    s += f'<text x="{ox}" y="{y+36}" font-size="17" font-weight="bold" fill="{MORK}">{Y}</text></g>'
    return s


def pil(x, tekst1, tekst2=""):
    s = f'<line x1="{x}" y1="190" x2="{x+34}" y2="190" stroke="#dc2626" stroke-width="4" marker-end="url(#gp)"/>'
    return s


def gem(navn, w, h, indhold):
    with open(os.path.join(OUT, navn), "w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif">'
                '<defs><marker id="gp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
                '<path d="M0 0L10 5L0 10z" fill="#dc2626"/></marker></defs>'
                f'<rect width="{w}" height="{h}" fill="white"/>{indhold}</svg>\n')
    print("Skrevet:", navn)


def legende(y, navne, x=20):
    s = ""
    for n in navne:
        s += tegn_molekyle(n, x + 20, y) + f'<text x="{x+42}" y="{y+5}" font-size="15" fill="{MORK}">{NAVN[n]}</text>'
        x += 120
    return s


def nobr():
    rng = random.Random(7)
    s = kammer(20, "1. Ligevægt", {"NO": 16, "Br2": 8, "NOBr": 12}, 1, "Y = K = 0,70 bar⁻¹", 280,
               "1. Ligevægt: 16 NO, 8 Br₂ og 12 NOBr. Y = 1,2² / (1,6² · 0,8) = 0,70 bar⁻¹, og det er K. Samlet tryk: 3,6 bar.", rng)
    s += pil(285, "") 
    s += kammer(340, "2. Lige efter", {"NO": 16, "Br2": 8, "NOBr": 12}, 2, "Y = 0,35 bar⁻¹ (K &gt; Y)", 140,
                "2. Lige efter: Volumen er halveret, og molekylerne er de samme. Alle partialtryk er fordoblet. Y er halveret til 0,35 bar⁻¹, fordi der er 3 faktorer i nævneren og 2 i tælleren. K > Y, så ligevægten forskydes mod højre.", rng)
    s += pil(605, "")
    s += kammer(660, "3. Ny ligevægt", {"NO": 14, "Br2": 7, "NOBr": 14}, 2, "Y = K ≈ 0,70 bar⁻¹", 140,
                "3. Ny ligevægt: 2 NO og 1 Br₂ er blevet til 2 NOBr. Der er færre molekyler, så det samlede tryk er faldet fra 7,2 til 7,0 bar. Y er tilbage på K (tallene er afrundet), og K er uændret.", rng)
    s += legende(520, ["NO", "Br2", "NOBr"])
    gem("nobr.svg", 940, 545, s)


def hi():
    rng = random.Random(3)
    s = kammer(20, "1. Ligevægt", {"H2": 2, "I2": 2, "HI": 15}, 1, "Y = K = 56", 280,
               "1. Ligevægt: Y = 1,5² / (0,2 · 0,2) = 56. Der er 2 gasmolekyler på hver side af reaktionsskemaet.", rng)
    s += pil(285, "")
    s += kammer(340, "2. Efter sammenpresning", {"H2": 2, "I2": 2, "HI": 15}, 2, "Y = K = 56", 140,
                "2. Efter sammenpresning: Alle partialtryk er fordoblet. Y = 3,0² / (0,4 · 0,4) = 56. To faktorer 2 i tælleren og to i nævneren går ud med hinanden. Y = K, så ligevægten forskydes ikke.", rng)
    s += legende(520, ["H2", "I2", "HI"])
    gem("hi.svg", 620, 545, s)


if __name__ == "__main__":
    nobr()
    hi()
