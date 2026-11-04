"""Figurer til Kemi B – Syrebase-ligevægte.
Kør fra crsite-roden:  python3 scripts/figurer/syrebase.py
Output: static/img/syrebase/*.svg"""
import math
import os
import random

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "static", "img", "syrebase")
os.makedirs(OUT, exist_ok=True)
MORK, GRA = "#1e293b", "#64748b"
ROD, BLA, GRON, GUL, LILLA = "#dc2626", "#2563eb", "#15803d", "#d97706", "#7c3aed"


def gem(navn, w, h, indhold):
    with open(os.path.join(OUT, navn), "w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif">'
                '<defs><marker id="sp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
                'orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>'
                f'<rect width="{w}" height="{h}" fill="white"/>{indhold}</svg>\n')
    print("Skrevet:", navn)


def t(x, y, s, st=18, f=MORK, a="middle", v="normal"):
    return f'<text x="{x}" y="{y}" font-size="{st}" fill="{f}" text-anchor="{a}" font-weight="{v}">{s}</text>'


def h_atom(x, y, r=9):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#f1f5f9" stroke="{MORK}" stroke-width="1.5"/>'


def kerne(x, y, farve, tekst="", r=22, ladning="", k=1):
    """Stort atom med brint rundt om sættes af kaldet; ladning skrives øverst til højre."""
    s = f'<circle cx="{x}" cy="{y}" r="{r}" fill="{farve}" stroke="{MORK}" stroke-width="1.5"/>'
    if tekst:
        s += t(x, y + 5 * k, tekst, 15 * k, "white", v="bold")
    return s


def tegn_ladning(x, y, l, k=1):
    f = ROD if l == "+" else BLA
    return (f'<circle cx="{x}" cy="{y}" r="{10*k}" fill="white" stroke="{f}" stroke-width="2"/>'
            + t(x, y + 6 * k, "+" if l == "+" else "−", 18 * k, f, v="bold"))


def med_h(x, y, farve, tekst, vinkler, r=22, ladning="", k=1):
    """Centralatom med H-atomer i de givne vinkler (grader)."""
    s = ""
    for v in vinkler:
        s += h_atom(x + (r * k + 6 * k) * math.cos(math.radians(v)), y - (r * k + 6 * k) * math.sin(math.radians(v)), 9 * k)
    s += kerne(x, y, farve, tekst, r * k, k=k)
    if ladning:
        s += tegn_ladning(x + 26 * k, y - 28 * k, ladning, k)
    return s


def gruppe(x, y, ladning="", h=False, k=1):
    """CH₃COO som aflang klump, evt. med et H på."""
    s = ""
    if h:
        s += h_atom(x + 50 * k, y, 9 * k)
    s += (f'<rect x="{x-44*k}" y="{y-20*k}" width="{88*k}" height="{40*k}" rx="{20*k}" fill="{GUL}" stroke="{MORK}" stroke-width="1.5"/>')
    s += t(x, y + 5 * k, "CH₃COO", 15 * k, "white", v="bold")
    if ladning:
        s += tegn_ladning(x + 44 * k, y - 22 * k, ladning, k)
    return s


def ligevaegtspile(x, y):
    return (f'<line x1="{x-34}" y1="{y-6}" x2="{x+34}" y2="{y-6}" stroke="{MORK}" stroke-width="3" marker-end="url(#sp)"/>'
            f'<line x1="{x+34}" y1="{y+6}" x2="{x-34}" y2="{y+6}" stroke="{MORK}" stroke-width="3" marker-end="url(#sp)"/>')


def bue(x1, x2, y, top, f=ROD, label="H⁺"):
    m = (x1 + x2) / 2
    return (f'<path d="M{x1} {y} Q{m} {top} {x2} {y}" fill="none" stroke="{f}" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#sp)"/>'
            + t(m, (y + top) / 2 - 8, label, 18, f, v="bold"))


def bjaelke(x1, x2, y, f, tekst):
    return (f'<path d="M{x1} {y} v14 H{x2} v-14" fill="none" stroke="{f}" stroke-width="3"/>'
            + t((x1 + x2) / 2, y + 36, tekst, 16, f, v="bold"))


def syre():
    s = gruppe(120, 130, h=True) + t(120, 196, "CH₃COOH", 18) + t(120, 220, "syre", 17, GRA)
    s += t(222, 138, "+", 28) + med_h(310, 130, "#ef4444", "O", [150, 30]) + t(310, 196, "H₂O", 18) + t(310, 220, "base", 17, GRA)
    s += bue(180, 300, 92, 34) + ligevaegtspile(450, 130)
    s += gruppe(600, 130, ladning="-") + t(600, 196, "CH₃COO⁻", 18) + t(600, 220, "korresponderende base", 15, GRA)
    s += t(708, 138, "+", 28) + med_h(800, 130, "#ef4444", "O", [150, 30, 270], ladning="+") + t(800, 196, "H₃O⁺", 18) + t(800, 220, "korresponderende syre", 15, GRA)
    s += bjaelke(120, 600, 234, BLA, "syre-basepar 1: forskellen er én H⁺")
    s += bjaelke(310, 800, 284, GRON, "syre-basepar 2: forskellen er én H⁺")
    gem("syre-ligevaegt.svg", 920, 345, s)


def base():
    s = med_h(120, 130, BLA, "N", [90, 210, 330]) + t(120, 196, "NH₃", 18) + t(120, 220, "base", 17, GRA)
    s += t(222, 138, "+", 28) + med_h(310, 130, "#ef4444", "O", [150, 30]) + t(310, 196, "H₂O", 18) + t(310, 220, "syre", 17, GRA)
    s += bue(285, 150, 92, 34) + ligevaegtspile(450, 130)
    s += med_h(600, 130, BLA, "N", [45, 135, 225, 315], ladning="+") + t(600, 196, "NH₄⁺", 18) + t(600, 220, "korresponderende syre", 15, GRA)
    s += t(708, 138, "+", 28) + med_h(800, 130, "#ef4444", "O", [30], ladning="-") + t(800, 196, "OH⁻", 18) + t(800, 220, "korresponderende base", 15, GRA)
    s += bjaelke(120, 600, 234, BLA, "syre-basepar 1: forskellen er én H⁺")
    s += bjaelke(310, 800, 284, GRON, "syre-basepar 2: forskellen er én H⁺")
    gem("base-ligevaegt.svg", 920, 345, s)


def baeger(ox, titel, partikler, under, seed, kol=5):
    rng = random.Random(seed)
    b, h, top = 340, 300, 60
    s = t(ox + b / 2, 32, titel, 21, v="bold")
    s += f'<rect x="{ox}" y="{top+16}" width="{b}" height="{h-16}" fill="#dbeafe"/>'
    s += f'<path d="M{ox-8} {top} H{ox} V{top+h} H{ox+b} V{top} H{ox+b+8}" fill="none" stroke="{MORK}" stroke-width="4"/>'
    rk = 5
    celler = [(i, j) for j in range(rk) for i in range(kol)]
    rng.shuffle(celler)
    for p, (i, j) in zip(partikler, celler):
        x = ox + 8 + (b - 16) / kol * (i + .5) + rng.uniform(-8, 8)
        y = top + 22 + (h - 30) / rk * (j + .5) + rng.uniform(-6, 6)
        s += p(x, y)
    return s + t(ox + b / 2, top + h + 30, under, 17)


def staerk_svag():
    k = .62
    h3o = lambda x, y: med_h(x, y, "#ef4444", "", [150, 30, 270], ladning="+", k=k)
    cl = lambda x, y: kerne(x, y, GRON, "Cl", 22 * k * 1.15, k=.75) + tegn_ladning(x + 15, y - 15, "-", .6)
    ha = lambda x, y: gruppe(x - 4, y, h=True, k=.62)
    a = lambda x, y: gruppe(x, y, ladning="-", k=.62)
    s = baeger(20, "Stærk syre: HCl", [cl] * 12 + [h3o] * 12, "Næsten alle molekyler har afgivet H⁺", 4)
    s += baeger(400, "Svag syre: CH₃COOH", [ha] * 11 + [a, h3o], "Kun få molekyler har afgivet H⁺", 5, kol=3)
    gem("staerk-svag.svg", 760, 400, s)


if __name__ == "__main__":
    syre()
    base()
    staerk_svag()
