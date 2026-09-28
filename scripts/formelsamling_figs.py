"""Genererer SVG-figurer til formelsamlingerne (fysik + kemi).
Kør fra repo-roden:  python3 scripts/formelsamling_figs.py
-> skriver til static/images/formelsamling/
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Polygon, Arc

plt.rcParams.update({
    "svg.fonttype": "path",
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "mathtext.fontset": "dejavusans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "images", "formelsamling")
os.makedirs(OUT, exist_ok=True)

BLUE = "#1f5fa8"
RED = "#c0392b"
GREEN = "#2e8b57"
ORANGE = "#d9822b"
GREY = "#666666"
LIGHT = "#dce8f5"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), format="svg", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("skrev", name)


def arrow(ax, x0, y0, x1, y1, color=BLUE, lw=2.2, style="-|>", ms=14, **kw):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms,
                        color=color, lw=lw, shrinkA=0, shrinkB=0, **kw)
    ax.add_patch(a)
    return a


def dim(ax, x0, y0, x1, y1, text, color=GREY, off=(0, 0), **kw):
    arrow(ax, x0, y0, x1, y1, color=color, lw=1.2, style="<|-|>", ms=9)
    ax.text((x0 + x1) / 2 + off[0], (y0 + y1) / 2 + off[1], text, color=color,
            ha="center", va="center", **kw)


def blank(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


# ---------------------------------------------------------------- FYSIK C
def nyttevirkning():
    fig, ax = blank(7, 3.0)
    # tilført
    ax.add_patch(Polygon([[0, 0], [4, 0], [4, 3], [0, 3]], color=BLUE, alpha=.85))
    # nyttig (øverst, går videre til højre)
    ax.add_patch(Polygon([[4, 1.9], [7.2, 1.9], [7.8, 2.45], [7.2, 3], [4, 3]], color=GREEN, alpha=.9))
    # tab (bøjer nedad)
    ax.add_patch(Polygon([[4, 0], [4, 1.9], [5.6, 1.9], [5.6, -0.8], [6.15, -0.8], [4.75, -1.8],
                          [3.35, -0.8], [3.9, -0.8], [3.9, 0]], color=RED, alpha=.8))
    ax.text(2, 1.5, "Tilført energi\n$E_{\\mathrm{tilført}}$", color="white", ha="center", va="center", fontsize=13)
    ax.text(5.9, 2.45, "Nyttig energi $E_{\\mathrm{nyttig}}$", color="white", ha="center", va="center", fontsize=10)
    ax.text(6.4, -1.2, "Tab – ender som\ntermisk energi", color=RED, ha="left", va="center", fontsize=11)
    ax.text(8.1, 0.6, "$\\eta = \\dfrac{E_{\\mathrm{nyttig}}}{E_{\\mathrm{tilført}}}$", fontsize=15, ha="left", va="center")
    ax.set_xlim(-0.2, 11)
    ax.set_ylim(-2, 3.2)
    save(fig, "nyttevirkning.svg")


def boelge():
    fig, ax = plt.subplots(figsize=(7.5, 2.8))
    lam, A = 4.0, 1.0
    x = np.linspace(0, 10, 600)
    ax.plot(x, A * np.sin(2 * np.pi * x / lam), color=BLUE, lw=2.4)
    ax.axhline(0, color=GREY, lw=1, ls="--")
    ax.text(10.1, 0, "ligevægt", va="center", color=GREY, fontsize=9)
    # lambda mellem to toppe
    dim(ax, 1, 1.25, 5, 1.25, "", color=RED)
    ax.text(3, 1.45, "bølgelængde $\\lambda$", color=RED, ha="center")
    ax.plot([1, 1], [1, 1.3], color=RED, lw=.8)
    ax.plot([5, 5], [1, 1.3], color=RED, lw=.8)
    dim(ax, 7.3, 0, 7.3, -1, "", color=GREEN)
    ax.text(7.45, -0.5, "amplitude $A$", color=GREEN, va="center")
    arrow(ax, 8.6, 0.75, 9.9, 0.75, color=ORANGE, lw=1.6)
    ax.text(9.25, 0.95, "$v$", color=ORANGE, ha="center")
    ax.set_xlim(0, 11.2)
    ax.set_ylim(-1.35, 1.85)
    ax.set_xlabel("sted $x$")
    ax.set_ylabel("udsving $y$")
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, "boelge.svg")


def staaende():
    fig, axs = plt.subplots(3, 1, figsize=(6.5, 4.2), sharex=True)
    x = np.linspace(0, 1, 400)
    for n, ax in zip([1, 2, 3], axs):
        y = np.sin(n * np.pi * x)
        ax.fill_between(x, y, -y, color=LIGHT)
        ax.plot(x, y, color=BLUE, lw=2)
        ax.plot(x, -y, color=BLUE, lw=2, ls="--")
        knots = np.arange(0, n + 1) / n
        ax.plot(knots, 0 * knots, "o", color=RED, ms=5)
        ax.plot([0, 0], [-1.2, 1.2], color="k", lw=4)
        ax.plot([1, 1], [-1.2, 1.2], color="k", lw=4)
        ax.axis("off")
        frac = {1: "$L = \\frac{1}{2}\\lambda$", 2: "$L = \\lambda$", 3: "$L = \\frac{3}{2}\\lambda$"}[n]
        ax.text(1.05, 0, f"$n = {n}$:   {frac}", va="center", fontsize=12)
        ax.set_ylim(-1.3, 1.3)
    axs[0].text(0.5, 1.45, "Streng fastgjort i begge ender – knuder (rød) i enderne", ha="center", fontsize=10, color=GREY)
    axs[0].set_xlim(-0.05, 1.6)
    save(fig, "staaende_boelger.svg")


def gitter():
    fig, ax = blank(7, 4)
    ax.plot([0, 0], [-2.6, 2.6], color="k", lw=3)
    for y in np.linspace(-2.4, 2.4, 13):
        ax.plot([0, 0], [y - .08, y + .08], color="white", lw=3.5)
    ax.text(0, 2.9, "gitter\n(spalteafstand $d$)", ha="center", fontsize=9)
    arrow(ax, -2.6, 0, -0.15, 0, color=RED, lw=2.5)
    ax.text(-1.4, 0.3, "laser $\\lambda$", color=RED, ha="center")
    L = 6
    ax.plot([L, L], [-3, 3], color=GREY, lw=4)
    ax.text(L + .2, 3.0, "skærm", color=GREY, fontsize=9)
    for n, yy in [(0, 0), (1, 1.5), (-1, -1.5), (2, 3.0 * .95), (-2, -3.0 * .95)]:
        ax.plot([0, L], [0, yy], color=RED, lw=1.2, alpha=.8 if n else 1)
        ax.plot(L, yy, "o", color=RED, ms=7)
        ax.text(L + .25, yy, f"$n = {n}$", va="center", fontsize=10)
    ax.add_patch(Arc((0, 0), 3.2, 3.2, theta1=0, theta2=np.degrees(np.arctan(1.5 / L)), color=BLUE, lw=1.5))
    ax.text(1.85, 0.2, "$\\theta_1$", color=BLUE, fontsize=12)
    dim(ax, L - .6, 0, L - .6, 1.5, "", color=BLUE)
    ax.text(L - .75, .75, "$x_1$", color=BLUE, ha="right", va="center")
    dim(ax, 0, -2.95, L, -2.95, "", color=BLUE)
    ax.text(L / 2, -3.3, "$L$", color=BLUE, ha="center")
    ax.text(8.2, 0.3, "$d \\cdot \\sin\\theta_n = n \\cdot \\lambda$", fontsize=14)
    ax.text(8.2, -0.6, "$\\tan\\theta_n = \\dfrac{x_n}{L}$", fontsize=13)
    ax.set_xlim(-2.8, 12)
    ax.set_ylim(-3.6, 3.4)
    save(fig, "gitter.svg")


def em_spektrum():
    fig, ax = plt.subplots(figsize=(8.5, 2.6))
    regions = [("γ-stråling", -14, -11, "#6a3d9a"), ("røntgen", -11, -8, "#8e6bbf"),
               ("UV", -8, np.log10(380e-9), "#b39ddb"), ("", np.log10(380e-9), np.log10(750e-9), None),
               ("infrarød (IR)", np.log10(750e-9), -3, "#e57373"), ("mikrobølger", -3, 0, "#f0a35e"),
               ("radiobølger", 0, 3, "#f3c969")]
    for name, a, b, c in regions:
        if c:
            ax.add_patch(Rectangle((a, 0), b - a, 1, color=c))
            ax.text((a + b) / 2, 0.5, name, ha="center", va="center", fontsize=9,
                    rotation=0 if b - a > 1.6 else 90)
    # synligt som regnbue
    xs = np.linspace(np.log10(380e-9), np.log10(750e-9), 60)
    cmap = plt.get_cmap("nipy_spectral")
    for i in range(len(xs) - 1):
        ax.add_patch(Rectangle((xs[i], 0), xs[i + 1] - xs[i], 1, color=cmap(0.12 + 0.75 * i / 60)))
    ax.annotate("synligt lys\n380–750 nm", xy=(np.log10(550e-9), 1), xytext=(np.log10(550e-9), 1.75),
                ha="center", fontsize=9, arrowprops=dict(arrowstyle="-", color=GREY))
    ax.set_xlim(-14, 3)
    ax.set_ylim(0, 2.3)
    ax.set_yticks([])
    ticks = list(range(-14, 4, 2))
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"$10^{{{t}}}$" for t in ticks])
    ax.set_xlabel("bølgelængde $\\lambda$ / m      (frekvens og fotonenergi vokser mod venstre)")
    ax.spines["left"].set_visible(False)
    save(fig, "em_spektrum.svg")


def tidslinje():
    people = [
        (-384, "Aristoteles"), (-287, "Archimedes"), (-276, "Eratosthenes"), (100, "Ptolemæus"),
        (1473, "Kopernikus"), (1546, "Tycho Brahe"), (1564, "Galilei"), (1571, "Kepler"),
        (1629, "Huygens"), (1643, "Newton"), (1644, "Rømer"), (1777, "Ørsted"),
        (1791, "Faraday"), (1831, "Maxwell"), (1858, "Planck"), (1867, "M. Curie"),
        (1879, "Einstein"), (1885, "Bohr"),
    ]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 2.9), gridspec_kw={"width_ratios": [1, 2.2]}, sharey=True)
    for ax, lo, hi in [(a1, -450, 200), (a2, 1440, 1960)]:
        ax.set_xlim(lo, hi)
        ax.axhline(0, color="k", lw=1.5)
        ax.set_ylim(-2.1, 1.8)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.set_yticks([])
    a1.set_xticks([-400, -200, 0, 200]); a1.set_xticklabels(["400 f.Kr.", "200 f.Kr.", "0", "200"], fontsize=8)
    a2.set_xticks(range(1450, 1951, 100)); a2.tick_params(labelsize=8)
    for ax in (a1, a2):
        ax.xaxis.set_ticks_position("none")
    k = 0
    for year, name in people:
        ax = a1 if year < 500 else a2
        up = 1 if k % 2 == 0 else -1
        lev = [0.45, 0.95, 1.4][(k // 2) % 3]
        ax.plot([year, year], [0, up * lev], color=GREY, lw=.8)
        ax.plot(year, 0, "o", color=BLUE, ms=5)
        ax.text(year, up * (lev + .08), name, ha="center", va="bottom" if up > 0 else "top", fontsize=8.5)
        k += 1
    a1.text(200, 0, " ≈ ", fontsize=14, va="center", ha="left", backgroundcolor="white")
    fig.suptitle("Fødselsår (ca.) – bemærk tidsspringet mellem oldtid og renæssance", fontsize=9, color=GREY, y=-0.04)
    fig.subplots_adjust(wspace=0.05)
    save(fig, "tidslinje.svg")


# ---------------------------------------------------------------- FYSIK B
def skraaplan():
    th = np.radians(28)
    fig, ax = blank(6.5, 4)
    L = 8
    ax.add_patch(Polygon([[0, 0], [L, 0], [0, L * np.tan(th)]], color="#e8e8e8", ec="k"))
    ax.add_patch(Arc((L, 0), 2.4, 2.4, theta1=180 - np.degrees(th), theta2=180, color="k"))
    ax.text(L - 1.65, 0.28, "$\\theta$", fontsize=13)
    # klods
    u = np.array([-np.cos(th), np.sin(th)])       # op ad planen
    nrm = np.array([np.sin(th), np.cos(th)])      # vinkelret ud
    c0 = np.array([L, 0]) + u * 4.2
    w, h = 1.6, 1.0
    corners = [c0 - u * w / 2, c0 + u * w / 2, c0 + u * w / 2 + nrm * h, c0 - u * w / 2 + nrm * h]
    ax.add_patch(Polygon(corners, color=LIGHT, ec=BLUE, lw=1.5))
    cm = c0 + nrm * h / 2
    s = 2.6
    arrow(ax, *cm, cm[0], cm[1] - s, color=RED)
    ax.text(cm[0] + .15, cm[1] - s, "$F_{\\mathrm{tyngde}} = m\\cdot g$", color=RED, va="top")
    fn = cm + nrm * s * np.cos(th)
    arrow(ax, *cm, *fn, color=BLUE)
    ax.text(fn[0] + .1, fn[1], "$F_N = m\\cdot g\\cdot\\cos\\theta$", color=BLUE)
    fg = cm + u * 1.6
    arrow(ax, *cm, *fg, color=GREEN)
    ax.text(fg[0] - .2, fg[1] + .25, "$F_{\\mathrm{gnid}}$", color=GREEN, ha="right")
    # komposanter
    par = cm - u * s * np.sin(th)
    arrow(ax, *cm, *par, color=RED, lw=1.2, linestyle="--")
    ax.text(par[0] + .15, par[1] - .5, "$F_{\\parallel} = m\\cdot g\\cdot\\sin\\theta$", color=RED, fontsize=10)
    perp = cm - nrm * s * np.cos(th)
    arrow(ax, *cm, *perp, color=RED, lw=1.2, linestyle="--")
    ax.set_xlim(-0.5, 12)
    ax.set_ylim(-0.5, 5.3)
    save(fig, "skraaplan.svg")


def archimedes():
    fig, ax = blank(6, 4)
    ax.add_patch(Rectangle((0, 0), 5, 3.2, color="#bfdcf2"))
    ax.plot([0, 0, 5, 5], [4.2, 0, 0, 4.2], color="k", lw=2)
    ax.add_patch(Rectangle((1.8, 1.0), 1.4, 1.3, color="#b0b0b0", ec="k"))
    ax.text(2.5, 1.65, "$V$", ha="center", va="center", fontsize=13)
    ax.plot([2.5, 2.5], [2.3, 4.3], color="k", lw=1)
    ax.text(2.6, 4.1, "snor / kraftmåler", fontsize=9)
    arrow(ax, 2.2, 1.65, 2.2, 3.7, color=GREEN)
    ax.text(1.95, 3.5, "$F_{\\mathrm{op}}$", color=GREEN, ha="right", fontsize=12)
    arrow(ax, 2.8, 1.65, 2.8, -0.6, color=RED)
    ax.text(3.0, -0.4, "$F_{\\mathrm{tyngde}}$", color=RED, fontsize=12)
    ax.text(0.2, 0.3, "væske, densitet $\\rho_{\\mathrm{væske}}$", fontsize=9, color="#1a4f7a")
    ax.text(5.5, 2.2, "$F_{\\mathrm{op}} = \\rho_{\\mathrm{væske}} \\cdot V_{\\mathrm{fortrængt}} \\cdot g$", fontsize=13)
    ax.text(5.5, 1.3, "Opdriften er lig med tyngden\naf den fortrængte væske.", fontsize=10, color=GREY)
    ax.text(5.5, 0.2, "Flyder hvis $\\rho_{\\mathrm{legeme}} < \\rho_{\\mathrm{væske}}$", fontsize=10, color=GREY)
    ax.set_xlim(-0.3, 11.5)
    ax.set_ylim(-0.9, 4.5)
    save(fig, "archimedes.svg")


def gaslove():
    fig, axs = plt.subplots(1, 3, figsize=(10, 3.0))
    V = np.linspace(0.6, 5, 200)
    for T, c, lab in [(1, BLUE, "$T_1$"), (1.8, RED, "$T_2 > T_1$")]:
        axs[0].plot(V, T * 2 / V, color=c, lw=2, label=lab)
    axs[0].set_title("Boyle–Mariotte ($T$ konstant)\n$p\\cdot V$ = konstant", fontsize=10)
    axs[0].set_xlabel("$V$"); axs[0].set_ylabel("$p$"); axs[0].legend(frameon=False, fontsize=9)
    Tc = np.linspace(-273.15, 150, 50)
    for ax, lab, title in [(axs[1], "$V$", "$p$ konstant:  $V/T$ = konstant"),
                           (axs[2], "$p$", "$V$ konstant:  $p/T$ = konstant")]:
        ax.plot(Tc[Tc >= -40], (Tc[Tc >= -40] + 273.15) / 100, color=BLUE, lw=2)
        ax.plot(Tc[Tc <= -40], (Tc[Tc <= -40] + 273.15) / 100, color=BLUE, lw=1.3, ls="--")
        ax.plot(-273.15, 0, "o", color=RED)
        ax.annotate("0 K = −273,15 °C", (-273.15, 0), (-250, 2.9), fontsize=9, color=RED,
                    arrowprops=dict(arrowstyle="->", color=RED))
        ax.set_xlabel("$t$ / °C"); ax.set_ylabel(lab); ax.set_title(title, fontsize=10)
        ax.set_ylim(0, 4.4); ax.set_xlim(-290, 160)
    for ax in axs:
        ax.set_yticks([])
    axs[0].set_xticks([])
    fig.tight_layout()
    save(fig, "gaslove.svg")


def _res(ax, x, y, vertical=False, label=""):
    if vertical:
        ax.add_patch(Rectangle((x - .2, y - .5), .4, 1, fc="white", ec="k", lw=1.6, zorder=3))
        ax.text(x + .35, y, label, va="center", fontsize=11)
    else:
        ax.add_patch(Rectangle((x - .5, y - .2), 1, .4, fc="white", ec="k", lw=1.6, zorder=3))
        ax.text(x, y + .4, label, ha="center", fontsize=11)


def _batt(ax, x, y):
    ax.plot([x - .5, x - .1], [y, y], color="white", lw=6, zorder=2)
    ax.plot([x - .1, x - .1], [y - .45, y + .45], color="k", lw=2, zorder=3)
    ax.plot([x + .1, x + .1], [y - .22, y + .22], color="k", lw=4, zorder=3)
    ax.text(x - .1, y + .55, "+", ha="center", fontsize=10)
    ax.text(x, y - .9, "$U$", ha="center", fontsize=11)


def kredsloeb():
    fig, ax = blank(9, 3.3)
    # serie
    ax.plot([0, 4, 4, 0, 0], [0, 0, 2.5, 2.5, 0], color="k", lw=1.6)
    _batt(ax, 2, 0)
    _res(ax, 1.2, 2.5, label="$R_1$"); _res(ax, 2.8, 2.5, label="$R_2$")
    arrow(ax, 4.0, 1.6, 4.0, 1.0, color=BLUE, lw=1.6); ax.text(4.2, 1.3, "$I$", color=BLUE)
    ax.text(2, -2.0, "Serieforbindelse\n$R = R_1 + R_2$,  samme $I$", ha="center", fontsize=10)
    # parallel
    o = 6.5
    ax.plot([o, o + 4.5, o + 4.5, o, o], [0, 0, 2.8, 2.8, 0], color="k", lw=1.6)
    ax.plot([o + 2.2, o + 2.2], [0, 2.8], color="k", lw=1.6)
    ax.plot([o + 4.5, o + 4.5], [0, 2.8], color="k", lw=1.6)
    _batt(ax, o + 1.1, 0)
    _res(ax, o + 2.2, 1.4, vertical=True, label="$R_1$")
    _res(ax, o + 4.5, 1.4, vertical=True, label="$R_2$")
    ax.text(o + 2.25, -2.0, "Parallelforbindelse\n$\\frac{1}{R} = \\frac{1}{R_1} + \\frac{1}{R_2}$,  samme $U$",
            ha="center", fontsize=10)
    ax.set_xlim(-0.5, 12)
    ax.set_ylim(-2.8, 3.4)
    save(fig, "kredsloeb.svg")


def henfald():
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    t = np.linspace(0, 4.3, 300)
    ax.plot(t, 100 * 0.5 ** t, color=BLUE, lw=2.4)
    for n in [1, 2, 3]:
        y = 100 * 0.5 ** n
        ax.plot([0, n, n], [y, y, 0], color=RED, ls="--", lw=1)
        ax.text(0.04, y + 2, f"$N_0/{2**n}$", color=RED, fontsize=10)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["0", "$T_{½}$", "$2T_{½}$", "$3T_{½}$", "$4T_{½}$"])
    ax.set_yticks([0, 25, 50, 100]); ax.set_yticklabels(["0", "", "", "$N_0$"])
    ax.set_xlabel("tid $t$"); ax.set_ylabel("antal kerner $N$ (eller aktivitet $A$)")
    ax.text(2.2, 72, "$N(t) = N_0 \\cdot \\left(\\frac{1}{2}\\right)^{t/T_{½}} = N_0 \\cdot e^{-k\\cdot t}$", fontsize=12)
    ax.set_ylim(0, 108); ax.set_xlim(0, 4.3)
    save(fig, "henfald.svg")


def energiniveauer():
    fig, ax = plt.subplots(figsize=(6.5, 4))
    E = lambda n: -13.6 / n ** 2
    for n in range(1, 7):
        ax.plot([0, 6], [E(n), E(n)], color="k", lw=1.4)
        if n <= 3:
            ax.text(6.1, E(n), f"$n={n}$:  {E(n):.2f} eV".replace(".", ","), va="center", fontsize=9)
    ax.text(6.1, -0.75, "$n = 4, 5, 6, \\ldots$", va="center", fontsize=9)
    ax.plot([0, 6], [0, 0], color=GREY, ls="--")
    ax.text(6.1, 0.55, "$n = \\infty$: ioniseret (0 eV)", fontsize=9, color=GREY)
    cols = {3: "#d62728", 4: "#17becf", 5: "#1f3fbf", 6: "#7b2fbf"}
    lam = {3: 656, 4: 486, 5: 434, 6: 410}
    for i, m in enumerate([3, 4, 5, 6]):
        x = 2.4 + i * 0.8
        arrow(ax, x, E(m), x, E(2), color=cols[m], lw=1.8, ms=10)
        ax.text(x, E(2) - 0.35, f"{lam[m]}", ha="center", va="top", fontsize=8, color=cols[m])
    arrow(ax, 0.8, E(2), 0.8, E(1), color="#8e6bbf", lw=1.8, ms=10)
    ax.text(0.95, -7, "Lyman (UV)", fontsize=8, color="#8e6bbf")
    ax.text(4.6, -5.0, "Balmer (synligt, nm)", fontsize=8, ha="center")
    ax.set_ylabel("energi $E_n$ / eV")
    ax.set_xticks([]); ax.set_xlim(0, 8.3); ax.set_ylim(-14.4, 1.2)
    ax.spines["bottom"].set_visible(False)
    ax.set_title("$E_n = -\\dfrac{13{,}6\\ \\mathrm{eV}}{n^2}$  (hydrogen)", fontsize=11)
    save(fig, "energiniveauer.svg")


# ---------------------------------------------------------------- FYSIK A
def skraat_kast():
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    v0, a, g = 10, np.radians(50), 9.82
    T = 2 * v0 * np.sin(a) / g
    t = np.linspace(0, T, 200)
    x = v0 * np.cos(a) * t
    y = v0 * np.sin(a) * t - 0.5 * g * t ** 2
    ax.plot(x, y, color=BLUE, lw=2.4)
    s = 0.28
    arrow(ax, 0, 0, v0 * np.cos(a) * s, v0 * np.sin(a) * s, color=RED)
    ax.text(v0 * np.cos(a) * s + .1, v0 * np.sin(a) * s, "$\\vec{v}_0$", color=RED, fontsize=13)
    arrow(ax, 0, 0, v0 * np.cos(a) * s, 0, color=RED, lw=1.2, linestyle="--")
    ax.text(v0 * np.cos(a) * s / 2, -0.35, "$v_{0x} = v_0\\cos\\alpha$", color=RED, ha="center", fontsize=9)
    arrow(ax, 0, 0, 0, v0 * np.sin(a) * s, color=RED, lw=1.2, linestyle="--")
    ax.text(-0.15, v0 * np.sin(a) * s / 2, "$v_{0y} = v_0\\sin\\alpha$", color=RED, ha="right", fontsize=9)
    ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=0, theta2=50, color="k"))
    ax.text(0.9, 0.3, "$\\alpha$")
    xm, ym = x.max() / 2, y.max()
    arrow(ax, xm, ym, xm + v0 * np.cos(a) * s, ym, color=ORANGE)
    ax.text(xm + 0.3, ym + 0.25, "i toppen: $v_y = 0$", color=ORANGE, fontsize=9)
    ax.plot([xm, xm], [0, ym], color=GREY, ls=":")
    ax.text(xm + .1, ym / 2, "$h_{\\max}$", color=GREY)
    arrow(ax, x[140], y[140], x[140], y[140] - 1.3, color=GREEN)
    ax.text(x[140] + .15, y[140] - 1.1, "$\\vec{g}$", color=GREEN, fontsize=12)
    dim(ax, 0, -0.9, x.max(), -0.9, "")
    ax.text(x.max() / 2, -1.3, "kastelængde (samme højde): $x = \\dfrac{v_0^2\\sin(2\\alpha)}{g}$", ha="center", va="top", color=GREY, fontsize=9)
    ax.set_xlim(-2.8, 11.5); ax.set_ylim(-2.3, 4.6)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "skraat_kast.svg")


def cirkel():
    fig, ax = blank(5.5, 4)
    ax.add_patch(Circle((0, 0), 2, fill=False, color=GREY, lw=1.5, ls="--"))
    ph = np.radians(40)
    p = 2 * np.array([np.cos(ph), np.sin(ph)])
    q = 2 * np.array([np.cos(np.radians(200)), np.sin(np.radians(200))])
    ax.plot([0, q[0]], [0, q[1]], color="k", lw=1)
    ax.text(q[0] / 2, q[1] / 2 + .15, "$r$", fontsize=12)
    ax.plot(0, 0, "k+", ms=8)
    ax.add_patch(Circle(p, .15, color="k", zorder=4))
    tang = np.array([-np.sin(ph), np.cos(ph)])
    arrow(ax, *p, *(p + 1.5 * tang), color=BLUE)
    ax.text(*(p + 1.6 * tang), "$\\vec{v}$ (tangent)", color=BLUE)
    arrow(ax, *p, *(p * 0.35), color=RED)
    ax.text(0.8, 0.35, "$\\vec{F}_c,\\ \\vec{a}_c$\nmod centrum", color=RED, fontsize=10, va="top")
    ax.text(2.8, -1.0, "$a_c = \\dfrac{v^2}{r} = \\omega^2 r$\n\n$F_c = m\\cdot\\dfrac{v^2}{r}$", fontsize=12)
    ax.text(2.8, -2.4, "Ingen kraft udad – centrifugal-\nkraften er en skinkraft.", fontsize=9, color=GREY)
    ax.set_xlim(-2.3, 6.5); ax.set_ylim(-2.6, 3.4)
    save(fig, "cirkelbevaegelse.svg")


def b_felt():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 4))
    for ax in (a1, a2):
        ax.set_aspect("equal"); ax.axis("off")
    # (a) ladet partikel i B ud af papiret
    for xx in np.arange(-2.5, 2.6, 1):
        for yy in np.arange(-2.5, 2.6, 1):
            a1.add_patch(Circle((xx, yy), .09, fill=False, color=GREY))
            a1.plot(xx, yy, ".", color=GREY, ms=2)
    a1.add_patch(Circle((0, 0), 1.8, fill=False, color=BLUE, lw=2))
    p = np.array([1.8, 0])
    a1.add_patch(Circle(p, .17, color=RED, zorder=4))
    a1.text(*p, "+", color="white", ha="center", va="center", fontsize=10, zorder=5)
    arrow(a1, *p, p[0], p[1] - 1.2, color=BLUE)
    a1.text(p[0] + .15, p[1] - 1.1, "$\\vec{v}$", color=BLUE, fontsize=12)
    arrow(a1, *p, p[0] - 1.1, p[1], color=RED)
    a1.text(p[0] - 0.9, p[1] + .2, "$\\vec{F}$", color=RED, fontsize=12)
    a1.set_title("Ladet partikel, $\\vec{B}$ ud af papiret (⊙)\n$F = q\\,v\\,B$,   $r = \\dfrac{m\\,v}{q\\,B}$", fontsize=10)
    a1.set_xlim(-3, 3); a1.set_ylim(-3, 3)
    # (b) lang lige leder
    for r in [0.7, 1.4, 2.1]:
        a2.add_patch(Circle((0, 0), r, fill=False, color=BLUE, lw=1.4))
        arrow(a2, r * np.cos(0.5), r * np.sin(0.5), r * np.cos(0.62), r * np.sin(0.62), color=BLUE, lw=1.4, ms=10)
    a2.add_patch(Circle((0, 0), .25, fc="white", ec="k", lw=1.5, zorder=4))
    a2.plot(0, 0, "k.", ms=6, zorder=5)
    a2.text(0.35, -0.35, "$I$ ud af\npapiret", fontsize=9)
    a2.set_title("Felt om lang lige leder (højrehåndsreglen)\n$B = \\dfrac{\\mu_0\\, I}{2\\pi\\, r}$", fontsize=10)
    a2.set_xlim(-3, 3); a2.set_ylim(-3, 3)
    save(fig, "b_felt.svg")


def harmonisk():
    fig, ax = plt.subplots(figsize=(7, 2.8))
    t = np.linspace(0, 2.4, 400)
    ax.plot(t, np.cos(2 * np.pi * t), color=BLUE, lw=2.2)
    ax.axhline(0, color=GREY, lw=.8)
    dim(ax, 0, 1.2, 1, 1.2, "")
    ax.text(0.5, 1.35, "periode $T$", ha="center", color=GREY)
    dim(ax, 1.5, 0, 1.5, -1, "", color=GREEN)
    ax.text(1.55, -0.5, "amplitude $A$", color=GREEN, va="center")
    ax.set_title("$x(t) = A\\cos(\\omega t + \\varphi)$", fontsize=11)
    ax.set_xlabel("tid $t$"); ax.set_ylabel("udsving $x$")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-1.2, 1.6)
    save(fig, "harmonisk.svg")


# ---------------------------------------------------------------- KEMI
def ph_skala():
    fig, ax = plt.subplots(figsize=(9, 2.5))
    cmap = plt.get_cmap("RdYlBu")
    for i in range(14):
        ax.add_patch(Rectangle((i, 0), 1, 1, color=cmap(i / 13)))
        ax.text(i + .5, .5, str(i + 1 - 1 if False else i), ha="center", va="center", fontsize=9)
    ax.text(14 + .5 - 1 + 1, .5, "", fontsize=9)
    ex = [(1.5, "mavesyre ≈ 1–2"), (2.3, "citronsaft ≈ 2–2,5"), (2.6, "cola ≈ 2,5"), (5, "kaffe ≈ 5"),
          (7, "rent vand 7 (25 °C)"), (7.4, "blod ≈ 7,4"), (8.1, "havvand ≈ 8,1"),
          (11.5, "husholdn.-ammoniak ≈ 11–12"), (13.5, "afløbsrens ≈ 13–14")]
    for k, (v, s) in enumerate(ex):
        up = k % 2 == 0
        y0, y1 = (1, 1.35 + 0.3 * (k % 4 == 0)) if up else (0, -0.35 - 0.3 * (k % 4 == 1))
        ax.plot([v, v], [y0, y1], color=GREY, lw=.8)
        ax.text(v, y1, s, ha="center", va="bottom" if up else "top", fontsize=8)
    ax.text(0, -1.25, "← surt", color=RED, fontsize=10)
    ax.text(14, -1.25, "basisk →", color=BLUE, fontsize=10, ha="right")
    ax.set_xlim(-0.2, 14.2); ax.set_ylim(-1.4, 2.0)
    ax.axis("off")
    fig.suptitle("pH-skalaen (tallene i felterne er pH; eksempler er cirkaværdier)", fontsize=9, color=GREY, y=0.02)
    save(fig, "ph_skala.svg")


def titrerkurve():
    Ka, Kw = 10 ** -4.76, 1e-14
    ca, Va, cb = 0.100, 25.0, 0.100
    Vb = np.linspace(0.01, 50, 1000)
    pH = []
    for vb in Vb:
        Ct = ca * Va / (Va + vb)
        Na = cb * vb / (Va + vb)
        lo, hi = 0.0, 14.0
        for _ in range(80):  # halveringsmetode på ladningsbalancen
            m = (lo + hi) / 2
            h = 10 ** -m
            f = h + Na - Kw / h - Ct * Ka / (Ka + h)
            if f > 0:
                lo = m
            else:
                hi = m
        pH.append((lo + hi) / 2)
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(Vb, pH, color=BLUE, lw=2.4)
    ph_half = np.interp(12.5, Vb, pH)
    ph_eq = np.interp(25, Vb, pH)
    ax.plot([12.5, 12.5, 0], [0, ph_half, ph_half], color=RED, ls="--", lw=1)
    ax.text(13.3, 2.6, f"halvækvivalens: pH = p$K_a$ = 4,76", color=RED, fontsize=9)
    ax.plot([25, 25], [0, ph_eq], color=GREEN, ls="--", lw=1)
    ax.plot(25, ph_eq, "o", color=GREEN)
    ax.text(26, ph_eq - .6, f"ækvivalenspunkt\npH ≈ {ph_eq:.1f}".replace(".", ","), color=GREEN, fontsize=9)
    ax.set_xlabel("tilsat 0,100 M NaOH / mL"); ax.set_ylabel("pH")
    ax.set_title("25,0 mL 0,100 M eddikesyre titreret med NaOH", fontsize=10)
    ax.set_ylim(0, 14); ax.set_xlim(0, 50)
    save(fig, "titrerkurve.svg")
    return ph_eq


def alkan_kogepunkter():
    names = ["methan", "ethan", "propan", "butan", "pentan", "hexan", "heptan", "octan", "nonan", "decan"]
    bp = [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7, 98.4, 125.7, 150.8, 174.1]
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    n = np.arange(1, 11)
    ax.plot(n, bp, "o-", color=BLUE, lw=2)
    ax.axhline(20, color=RED, ls="--", lw=1)
    ax.text(1.1, 28, "stuetemperatur (20 °C)", color=RED, fontsize=9)
    ax.set_xticks(n); ax.set_xlabel("antal C-atomer $n$")
    ax.set_ylabel("kogepunkt / °C (ved 1 atm)")
    ax.text(5.6, -120, "gas ved stuetemperatur: $n$ ≤ 4\nvæske: $n$ = 5–16 (ca.)", fontsize=9, color=GREY)
    save(fig, "alkan_kogepunkter.svg")


def alkan(n, name):
    """Strukturformel med alle H (lineær, 'Lewis-agtig')."""
    fig, ax = plt.subplots(figsize=(0.55 * n + 0.9, 1.35))
    ax.set_aspect("equal"); ax.axis("off")
    d = 1.0
    for i in range(n):
        x = i * d
        ax.text(x, 0, "C", ha="center", va="center", fontsize=13, fontweight="bold")
        for dy in (1, -1):
            ax.plot([x, x], [dy * .22, dy * .62], color="k", lw=1.1)
            ax.text(x, dy * .82, "H", ha="center", va="center", fontsize=11)
        if i < n - 1:
            ax.plot([x + .22, x + d - .22], [0, 0], color="k", lw=1.1)
    ax.plot([-.22, -.62], [0, 0], color="k", lw=1.1); ax.text(-.82, 0, "H", ha="center", va="center", fontsize=11)
    xe = (n - 1) * d
    ax.plot([xe + .22, xe + .62], [0, 0], color="k", lw=1.1); ax.text(xe + .82, 0, "H", ha="center", va="center", fontsize=11)
    ax.set_xlim(-1.05, xe + 1.05); ax.set_ylim(-1.05, 1.05)
    save(fig, f"alkan_{n:02d}_{name}.svg")


if __name__ == "__main__":
    nyttevirkning(); boelge(); staaende(); gitter(); em_spektrum(); tidslinje()
    skraaplan(); archimedes(); gaslove(); kredsloeb(); henfald(); energiniveauer()
    skraat_kast(); cirkel(); b_felt(); harmonisk()
    ph_skala(); print("pH ækv:", titrerkurve()); alkan_kogepunkter()
    for i, nm in enumerate(["methan", "ethan", "propan", "butan", "pentan", "hexan", "heptan", "octan", "nonan", "decan"], 1):
        alkan(i, nm)
