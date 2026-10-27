"""Figurer til Fysik A – Centralbevægelse.
Kør fra crsite-roden:  python3 scripts/figurer/centralbevaegelse.py
Output: static/img/centralbevaegelse/*.svg"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse, Polygon, Rectangle, FancyArrowPatch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "static", "img", "centralbevaegelse")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 13, "mathtext.fontset": "cm", "svg.fonttype": "path"})
BLA, GRON, ROD, GRA = "#1d4ed8", "#16a34a", "#dc2626", "#64748b"


def pil(ax, p0, p1, farve, lw=2.4, ms=18):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=farve,
                                 shrinkA=0, shrinkB=0, zorder=5))


def gem(fig, navn):
    fig.savefig(os.path.join(OUT, navn), bbox_inches="tight", transparent=False, facecolor="white")
    plt.close(fig)
    print("Skrevet:", os.path.join(OUT, navn))


# ---------------------------------------------------------------- 1. Stedvektor, fart og acceleration
def cirkel_vektorer():
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    r, th = 1.0, np.radians(50)
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r * np.cos(t), r * np.sin(t), color=GRA, lw=1.4)
    ax.annotate("", xy=(1.45, 0), xytext=(-1.35, 0), arrowprops=dict(arrowstyle="-|>", color="black", lw=1))
    ax.annotate("", xy=(0, 1.45), xytext=(0, -1.35), arrowprops=dict(arrowstyle="-|>", color="black", lw=1))
    ax.text(1.47, -0.09, "$x$", fontsize=15); ax.text(0.05, 1.45, "$y$", fontsize=15)
    P = np.array([r * np.cos(th), r * np.sin(th)])
    # Komposanter
    ax.plot([P[0], P[0]], [0, P[1]], ls="--", color=GRA, lw=1.2)
    ax.plot([0, P[0]], [P[1], P[1]], ls="--", color=GRA, lw=1.2)
    ax.text(P[0] / 2, -0.13, r"$r\cdot\cos(\omega t)$", ha="center", va="top", fontsize=14)
    ax.text(-0.04, P[1], r"$r\cdot\sin(\omega t)$", ha="right", va="center", fontsize=14)
    # Vinkel
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=np.degrees(th), color="black", lw=1.2))
    ax.text(0.31 * np.cos(th / 2), 0.31 * np.sin(th / 2), r"$\omega t$", fontsize=14, ha="left", va="center")
    # Vektorer
    pil(ax, (0, 0), P, BLA)
    ax.text(P[0] * 0.45 - 0.08, P[1] * 0.45 + 0.07, r"$\vec r$", color=BLA, fontsize=18)
    v = 0.6 * np.array([-np.sin(th), np.cos(th)])
    pil(ax, P, P + v, GRON)
    ax.text(*(P + v + np.array([0.04, 0.04])), r"$\vec v$", color=GRON, fontsize=18, ha="left")
    n = 0.07 * np.array([np.sin(th), -np.cos(th)])          # lidt ved siden af r-pilen
    a = -0.55 * P
    pil(ax, P + n, P + n + a, ROD)
    ax.text(*(P + n + a * 0.55 + np.array([0.08, -0.06])), r"$\vec a$", color=ROD, fontsize=18)
    ax.plot(*P, "o", color="black", ms=9, zorder=6)
    ax.text(P[0] + 0.07, P[1] + 0.05, "genstand", fontsize=12)
    ax.set_xlim(-1.4, 1.6); ax.set_ylim(-1.35, 1.55); ax.set_aspect("equal"); ax.axis("off")
    gem(fig, "cirkel-vektorer.svg")


# ---------------------------------------------------------------- 2. Rør-forsøget
def roer_forsoeg():
    fig, ax = plt.subplots(figsize=(7.2, 6.4))
    # Glasrør
    ax.add_patch(Rectangle((-0.06, -0.9), 0.12, 1.5, fc="#e0f2fe", ec="#0369a1", lw=1.5, zorder=3))
    ax.text(0.12, -0.55, "glasrør\n(du holder her)", fontsize=11, color="#0369a1")
    # Cirkelbanen i perspektiv
    top = np.array([0, 0.6])
    ax.add_patch(Ellipse((0, 0.95), 3.2, 0.7, fill=False, ls="--", color=GRA, lw=1.2))
    S = np.array([1.45, 0.83])                       # proppen
    ax.plot([top[0], S[0]], [top[1], S[1]], color="black", lw=1.3)   # snor
    ax.plot(*S, "o", ms=16, color="#b45309", zorder=6)
    ax.text(S[0] + 0.1, S[1] + 0.12, "prop, masse $m$", fontsize=12)
    ax.text(0.65, 0.58, "$L$", fontsize=15)
    pil(ax, S + np.array([0, 0.18]), S + np.array([-0.35, 0.36]), GRON, lw=2, ms=14)
    ax.text(S[0] - 0.45, S[1] + 0.42, r"$\vec v$", color=GRON, fontsize=15)
    pil(ax, S, S + 0.35 * (top - S) / np.linalg.norm(top - S), ROD, lw=2.2)
    ax.text(S[0] - 0.45, S[1] - 0.25, r"$F = M\cdot g$", color=ROD, fontsize=14)
    # Snor ned gennem røret og lodder
    ax.plot([0, 0], [0.6, -1.25], color="black", lw=1.3, zorder=4)
    ax.add_patch(Rectangle((-0.03, -1.0), 0.06, 0.05, color="#a855f7", zorder=5))  # clips
    ax.annotate("papirclips som\nmarkør: hold\nden lige under\nrøret, så $L$ er fast",
                xy=(0.04, -0.98), xytext=(0.5, -1.35), fontsize=10.5, color="#7e22ce",
                arrowprops=dict(arrowstyle="->", color="#7e22ce"))
    ax.add_patch(Rectangle((-0.16, -1.65), 0.32, 0.4, fc="#94a3b8", ec="black", lw=1.2, zorder=5))
    ax.text(0, -1.45, "$M$", ha="center", va="center", fontsize=15, zorder=6)
    ax.text(-0.25, -1.45, "lodder", ha="right", va="center", fontsize=12)
    pil(ax, (0, -1.67), (0, -2.0), ROD, lw=2)
    ax.text(0.06, -1.95, r"$M\cdot g$", color=ROD, fontsize=14)
    ax.set_xlim(-1.9, 2.2); ax.set_ylim(-2.1, 1.45); ax.set_aspect("equal"); ax.axis("off")
    gem(fig, "roer-forsoeg.svg")


# ---------------------------------------------------------------- 3. Keglependul
def keglependul():
    fig, ax = plt.subplots(figsize=(6.6, 6.2))
    O = np.array([0, 1.6]); h, rr = 1.6, 0.95
    ax.plot([-0.5, 0.5], [O[1], O[1]], color="black", lw=3)
    for x in np.linspace(-0.45, 0.45, 7):
        ax.plot([x, x + 0.1], [O[1], O[1] + 0.1], color="black", lw=1)
    ax.add_patch(Ellipse((0, 0), 2 * rr, 0.45, fill=False, ls="--", color=GRA, lw=1.2))
    P = np.array([rr, 0])
    ax.plot([O[0], P[0]], [O[1], P[1]], color="black", lw=1.4)
    ax.plot([O[0], -rr], [O[1], 0], color=GRA, lw=1, ls=":")
    ax.plot([0, 0], [O[1], 0], color=GRA, lw=1.2, ls="--")
    ax.plot([0, rr], [0, 0], color=GRA, lw=1.2, ls="--")
    ax.text(-0.1, 0.8, "$h$", fontsize=16, ha="right"); ax.text(rr / 2, -0.13, "$r$", fontsize=16, ha="center", va="top")
    ax.text(0.58, 0.95, "$L$", fontsize=16)
    th = np.arctan(rr / h)
    ax.add_patch(Arc(O, 0.7, 0.7, theta1=-90, theta2=-90 + np.degrees(th), color="black", lw=1.2))
    ax.text(0.11, O[1] - 0.48, r"$\theta$", fontsize=16)
    ax.plot(*P, "o", ms=16, color="#b45309", zorder=6)
    # Kræfter
    Tv = 0.75 * (O - P) / np.linalg.norm(O - P)
    pil(ax, P, P + Tv, BLA); ax.text(*(P + Tv + np.array([0.05, 0])), r"$\vec T$", color=BLA, fontsize=17)
    mg = np.array([0, -Tv[1]])
    pil(ax, P, P + mg, "black"); ax.text(P[0] + 0.07, P[1] + mg[1] + 0.02, r"$m\cdot\vec g$", fontsize=15)
    Fr = np.array([Tv[0], 0])
    pil(ax, P, P + Fr, ROD, lw=2.8)
    ax.text(P[0] + Fr[0] / 2, P[1] + 0.1, r"$\vec F_{\mathrm{res}}$", color=ROD, fontsize=16, ha="center")
    ax.plot([P[0] + Tv[0], P[0] + Tv[0]], [P[1], P[1] + Tv[1]], color=GRA, lw=1, ls=":")
    ax.set_xlim(-1.2, 1.7); ax.set_ylim(-0.95, 1.85); ax.set_aspect("equal"); ax.axis("off")
    gem(fig, "keglependul.svg")


# ---------------------------------------------------------------- 4. Keplers 2. lov (til print)
def kepler2():
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    a, e = 1.0, 0.6
    b = a * np.sqrt(1 - e * e)

    def pos(Ma):
        E = Ma
        for _ in range(30):
            E -= (E - e * np.sin(E) - Ma) / (1 - e * np.cos(E))
        return a * (np.cos(E) - e), b * np.sin(E)

    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(a * np.cos(t) - a * e, b * np.sin(t), color=GRA, lw=1.4)
    for (m0, m1), farve, tekst in [((-0.35, 0.35), "#93c5fd", "nær Jorden:\nkort og bred"),
                                   ((np.pi - 0.35, np.pi + 0.35), "#fcd34d", "langt væk:\nlang og smal")]:
        pts = [(0, 0)] + [pos(m) for m in np.linspace(m0, m1, 40)]
        ax.add_patch(Polygon(pts, closed=True, fc=farve, ec="black", lw=0.8, alpha=0.85))
    ax.plot(0, 0, "o", ms=20, color="#2563eb"); ax.text(0, -0.2, "Jorden", ha="center", va="top", fontsize=12)
    ax.text(0.47, 0.35, "samme\ntidsrum", fontsize=11, ha="center")
    ax.text(-1.55, 0.45, "samme\ntidsrum", fontsize=11, ha="center")
    ax.text(0.5, -0.55, "areal $A_1$", fontsize=13, ha="center")
    ax.text(-1.45, -0.42, "areal $A_2 = A_1$", fontsize=13, ha="center")
    ax.text(0.47, 0.62, "perigæum\n(hurtigst)", fontsize=10.5, ha="center", color=GRA)
    ax.text(-1.95, 0.72, "apogæum\n(langsomst)", fontsize=10.5, ha="center", color=GRA)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-2.35, 0.75)
    gem(fig, "kepler2.svg")


if __name__ == "__main__":
    cirkel_vektorer(); roer_forsoeg(); keglependul(); kepler2()
