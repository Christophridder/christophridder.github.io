"""Figurer til Fysik B – Energi (strand, spande, opvarmningsgraf, nyttevirkning).
Kør fra crsite-roden:  python3 scripts/figurer/energi_b.py
Output: static/img/energi-b/*.svg"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "static", "img", "energi-b")
os.makedirs(OUT, exist_ok=True)

C_VAND, C_SAND = 4182, 800  # J/(kg·K); tør sand ligger omkring 800
BLA, ROD, GUL, GRA, MORK = "#1d4ed8", "#dc2626", "#d97706", "#64748b", "#1e293b"


def gem(navn, w, h, indhold):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'font-family="Helvetica, Arial, sans-serif">\n'
           '<defs><marker id="p" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
           'markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" '
           'fill="context-stroke"/></marker></defs>\n' + indhold + "\n</svg>\n")
    with open(os.path.join(OUT, navn), "w", encoding="utf-8") as f:
        f.write(svg)
    print("Skrevet:", navn)


def tekst(x, y, s, str_=18, farve=MORK, anker="start", vaegt="normal"):
    return (f'<text x="{x}" y="{y}" font-size="{str_}" fill="{farve}" '
            f'text-anchor="{anker}" font-weight="{vaegt}">{s}</text>')


def sub(a, b, s=20):
    """Bogstav med sænket indeks som tspan-tekst."""
    return (f'<tspan font-style="italic">{a}</tspan><tspan dy="{s*0.3:.0f}" '
            f'font-size="{s*0.7:.0f}">{b}</tspan><tspan dy="{-s*0.3:.0f}">&#8203;</tspan>')


def pil(x1, y1, x2, y2, farve=ROD, b=4):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{farve}" '
            f'stroke-width="{b}" marker-end="url(#p)"/>')


def termometer(x, y, grader, tmax=50, lys=False):
    """Termometer: top i (x, y), 150 højt. Væsken følger skalaen 0–tmax °C."""
    h = 120
    fyld = h * grader / tmax
    k = "white" if lys else MORK
    return (f'<rect x="{x-9}" y="{y}" width="18" height="{h+12}" rx="9" fill="white" stroke="{k}" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y+h+18}" r="15" fill="{ROD}" stroke="{k}" stroke-width="2"/>'
            f'<rect x="{x-4}" y="{y+h+6-fyld:.1f}" width="8" height="{fyld+6:.1f}" fill="{ROD}"/>'
            + tekst(x + 22, y + 22, f"{grader} °C", 26, k, vaegt="bold"))


def blokke(x, y, n, farve):
    """n energiblokke; én blok = 800 J. Sidste blok kan være en brøkdel."""
    ud, b = "", 44
    for i in range(int(np.ceil(n))):
        w = b * min(1, n - i)
        ud += f'<rect x="{x+i*(b+3)}" y="{y}" width="{w:.1f}" height="22" fill="{farve}" stroke="white"/>'
    return ud


def strand(navn, dag):
    himmel = "#bfe3f7" if dag else "#1b2547"
    sand = "#ecd28f" if dag else "#9c8a5c"
    vand = "#4aa3df" if dag else "#23507e"
    lys = not dag
    T_sand, T_vand = (40, 22) if dag else (15, 18)
    s = f'<rect width="900" height="310" fill="{himmel}"/>'
    s += f'<rect y="290" width="900" height="290" fill="{sand}"/>'
    # Lavvandet sø: en flad skål i sandet
    s += f'<path d="M430 290 C500 290 520 372 610 372 L900 372 L900 290 Z" fill="{vand}"/>'
    s += tekst(24, 40, "Dag: solen skinner" if dag else "Nat: solen er væk", 28, "white" if lys else MORK, vaegt="bold")
    if dag:
        s += '<circle cx="450" cy="62" r="40" fill="#fbbf24"/>'
        s += pil(390, 105, 230, 270, GUL, 5) + pil(510, 105, 680, 270, GUL, 5)
        s += tekst(450, 135, "samme", 19, MORK, "middle") + tekst(450, 158, "solindstråling", 19, MORK, "middle")
    else:
        s += '<circle cx="450" cy="62" r="30" fill="#e2e8f0"/><circle cx="462" cy="54" r="26" fill="#1b2547"/>'
        for x, y in [(90, 90), (210, 60), (300, 120), (610, 50), (720, 110), (840, 70), (520, 140), (160, 150)]:
            s += f'<circle cx="{x}" cy="{y}" r="2.5" fill="white"/>'
        s += pil(230, 280, 230, 170, "#fca5a5", 5) + pil(680, 290, 680, 180, "#fca5a5", 5)
        s += tekst(450, 225, "begge afgiver energi", 19, "white", "middle")
        s += tekst(450, 248, "til natteluften", 19, "white", "middle")
    s += termometer(80, 170, T_sand, lys=lys)
    s += termometer(800, 170, T_vand, lys=lys)
    s += tekst(250, 345, "Sand", 24, MORK, "middle", "bold")
    s += tekst(740, 345, "Vand", 24, "white", "middle", "bold")
    # Varmekapaciteter som energiblokke
    s += '<rect y="400" width="900" height="180" fill="white"/>'
    s += tekst(24, 432, "Energi til at varme 1 kg op med 1 K (én blok = 800 J):", 20, MORK, vaegt="bold")
    s += tekst(24, 472, "Sand: c ≈ 800 J/(kg·K)", 20)
    s += blokke(300, 456, 1, GUL)
    s += tekst(24, 510, "Vand: c = 4182 J/(kg·K)", 20)
    s += blokke(300, 494, C_VAND / C_SAND, "#2563eb")
    if dag:
        s += tekst(24, 556, "Vand kræver ca. 5 gange så meget energi pr. grad. Derfor bliver sandet varmest.", 20, ROD, vaegt="bold")
    else:
        s += tekst(24, 556, "Når sandet mister 1 grad, skal vandet afgive ca. 5 gange så meget energi for det samme.", 19, ROD, vaegt="bold")
    gem(navn, 900, 580, s)


def spande():
    s = '<rect width="760" height="380" fill="white"/>'
    def spand(x, b, h_v, t1, t2, farve):
        y0 = 280
        return (f'<rect x="{x}" y="{y0-h_v}" width="{b}" height="{h_v}" fill="{farve}"/>'
                f'<path d="M{x} 60 V{y0} H{x+b} V60" fill="none" stroke="{MORK}" stroke-width="4"/>'
                + tekst(x + b / 2, y0 + 34, t1, 22, MORK, "middle", "bold")
                + tekst(x + b / 2, y0 + 62, t2, 18, MORK, "middle"))
    s += spand(110, 60, 200, "Sand", "lille c: smal spand", "#60a5fa")
    s += spand(420, 300, 40, "Vand", "stor c: bred spand", "#60a5fa")
    s += pil(140, 18, 140, 56, BLA) + pil(570, 18, 570, 56, BLA)
    s += tekst(160, 36, "samme mængde hældes i", 18, BLA)
    s += tekst(590, 36, "samme mængde", 18, BLA)
    s += tekst(186, 100, "højden stiger meget", 18, ROD) + tekst(570, 225, "højden stiger lidt", 18, ROD, "middle")
    gem("spande.svg", 760, 380, s)


def graf():
    plt.rcParams.update({"font.size": 13, "mathtext.fontset": "cm", "svg.fonttype": "path"})
    m = 1.0
    E = np.linspace(0, 40e3, 50)
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(E / 1e3, E / (m * C_SAND), color=GUL, lw=3)
    ax.plot(E / 1e3, E / (m * C_VAND), color=BLA, lw=3)
    Ex = 20e3
    for c, f in ((C_SAND, GUL), (C_VAND, BLA)):
        dT = Ex / (m * c)
        ax.plot([20, 20, 0], [0, dT, dT], color=f, ls="--", lw=1.2)
        ax.text(0.6, dT + 1, f"{dT:.1f} K".replace(".", ","), color=f)
    ax.text(31, 42, "Sand\n$c \\approx 800$ J/(kg·K)", color=GUL, ha="right", va="center")
    ax.text(39.5, 13.5, "Vand\n$c = 4182$ J/(kg·K)", color=BLA, ha="right", va="center")
    ax.set_xlim(0, 40); ax.set_ylim(0, 50)
    ax.set_xlabel("Tilført energi $E_{\\mathrm{tilført}}$ / kJ")
    ax.set_ylabel("Temperaturstigning $\\Delta T$ / K")
    ax.grid(alpha=.3)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(os.path.join(OUT, "opvarmning-graf.svg"), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Skrevet: opvarmning-graf.svg")


def opstilling():
    def maaler(ox):
        s = f'<rect x="{ox+14}" y="130" width="44" height="66" rx="6" fill="#e2e8f0" stroke="{MORK}" stroke-width="2"/>'
        s += f'<circle cx="{ox+36}" cy="163" r="13" fill="white" stroke="{MORK}" stroke-width="2"/>'
        s += tekst(ox + 36, 216, "stikkontakt", 14, GRA, "middle")
        s += f'<path d="M{ox+58} 163 H{ox+96}" stroke="{MORK}" stroke-width="4" fill="none"/>'
        s += f'<rect x="{ox+96}" y="110" width="124" height="106" rx="8" fill="#f8fafc" stroke="{MORK}" stroke-width="2.5"/>'
        s += f'<rect x="{ox+106}" y="122" width="104" height="38" fill="#0f172a"/>'
        s += f'<text x="{ox+158}" y="149" font-size="19" fill="#4ade80" text-anchor="middle" font-family="monospace">336000 J</text>'
        s += tekst(ox + 158, 188, "Energimåler", 15, MORK, "middle", "bold")
        return s

    def e_label(ox):
        return (f'<text x="{ox+158}" y="66" font-size="20" fill="{ROD}" text-anchor="middle">' + sub("E", "tilført") + "</text>"
                + pil(ox + 158, 74, ox + 158, 106, ROD, 3))

    def t_label(ox, x_til, y_til):
        s = f'<text x="{ox+268}" y="40" font-size="20" fill="{ROD}">' + sub("T", "vand, start") + "</text>"
        s += f'<text x="{ox+268}" y="68" font-size="20" fill="{ROD}">' + sub("T", "vand, slut") + "</text>"
        s += pil(ox + 330, 78, x_til, y_til, ROD, 3)
        return s

    def m_label(ox, x_til, y_til):
        return (f'<text x="{ox+150}" y="330" font-size="20" fill="{BLA}" text-anchor="middle">' + sub("m", "vand") + "</text>"
                + pil(ox + 182, 322, x_til, y_til, BLA, 3))

    s = '<rect width="1040" height="370" fill="white"/>'
    # Elkedel
    ox = 10
    s += maaler(ox)
    s += f'<path d="M{ox+220} 163 H{ox+250} V290 H{ox+270}" stroke="{MORK}" stroke-width="4" fill="none"/>'
    s += f'<path d="M{ox+270} 130 L{ox+262} 300 H{ox+420} L{ox+412} 130 Z" fill="#f1f5f9" stroke="{MORK}" stroke-width="3"/>'
    s += f'<path d="M{ox+267} 195 L{ox+262} 300 H{ox+420} L{ox+415} 195 Z" fill="#60a5fa"/>'
    s += f'<path d="M{ox+270} 130 L{ox+250} 112 L{ox+290} 112 Z" fill="#f1f5f9" stroke="{MORK}" stroke-width="3"/>'
    s += f'<path d="M{ox+412} 150 h38 v110 h-34" fill="none" stroke="{MORK}" stroke-width="6"/>'
    s += f'<rect x="{ox+255}" y="300" width="172" height="14" fill="{MORK}"/>'
    s += e_label(ox) + t_label(ox, ox + 340, 205) + m_label(ox, ox + 300, 270)
    s += tekst(ox + 340, 356, "Elkedel", 20, MORK, "middle", "bold")
    # Mikrobølgeovn
    ox = 530
    s += maaler(ox)
    s += f'<path d="M{ox+220} 163 H{ox+262}" stroke="{MORK}" stroke-width="4" fill="none"/>'
    s += f'<rect x="{ox+262}" y="115" width="236" height="190" rx="8" fill="#e2e8f0" stroke="{MORK}" stroke-width="3"/>'
    s += f'<rect x="{ox+276}" y="130" width="160" height="160" rx="4" fill="#fef9c3" stroke="{MORK}" stroke-width="2"/>'
    for y in (170, 215, 260):
        s += f'<circle cx="{ox+470}" cy="{y}" r="9" fill="#94a3b8"/>'
    s += f'<path d="M{ox+312} 205 V278 H{ox+400} V205" fill="none" stroke="{MORK}" stroke-width="3"/>'
    s += f'<rect x="{ox+314}" y="222" width="84" height="55" fill="#60a5fa"/>'
    s += f'<path d="M{ox+276} 280 H{ox+436}" stroke="{GRA}" stroke-width="4"/>'
    s += e_label(ox) + t_label(ox, ox + 356, 226) + m_label(ox, ox + 322, 262)
    s += tekst(ox + 380, 356, "Mikrobølgeovn", 20, MORK, "middle", "bold")
    gem("nyttevirkning-opstilling.svg", 1040, 370, s)


if __name__ == "__main__":
    strand("strand-dag.svg", True)
    strand("strand-nat.svg", False)
    spande()
    graf()
    opstilling()
