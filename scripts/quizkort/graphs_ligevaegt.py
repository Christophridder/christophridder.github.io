"""Grafer og glas-billeder til flashcards om ligevægt.
Kør fra crsite-roden:  python3 scripts/quizkort/graphs_ligevaegt.py
Gemmer .svg (web) og .pdf (print) i static/img/quiz-ligevaegt/"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, AutoMinorLocator
from matplotlib.patches import FancyBboxPatch, Rectangle, Wedge, FancyArrowPatch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "static", "img", "quiz-ligevaegt")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans", "axes.titlesize": 11})
KOMMA = FuncFormatter(lambda v, p: f"{v:g}".replace(".", ","))
GUL, GRAA, ROED = "#D4A017", "#7F8C8D", "#C0392B"
BLAA, GROEN, MOERKBLAA, LYSBLAA = "#2E86C1", "#7DAF3C", "#1B2A9C", "#8EC9F0"


def akser(ax, xl="t / s", yl="koncentration / mM"):
    ax.set_xlabel(xl); ax.set_ylabel(yl)
    ax.xaxis.set_major_formatter(KOMMA); ax.yaxis.set_major_formatter(KOMMA)
    ax.xaxis.set_minor_locator(AutoMinorLocator(2)); ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.grid(which="major", color="#bbb", lw=0.6); ax.grid(which="minor", color="#e3e3e3", lw=0.5)
    ax.set_xlim(left=0); ax.set_ylim(bottom=0)


def gem(fig, navn):
    fig.tight_layout()
    for ext in ("svg", "pdf"):
        fig.savefig(os.path.join(OUT, f"{navn}.{ext}"))
    plt.close(fig)


def sim(c0, rate, t_end, events=(), dt=0.01):
    """c0: dict, rate(c)->dict med dc/dt. events: liste af (t, funktion(c)->c)."""
    t = np.arange(0, t_end + dt, dt)
    c = dict(c0); res = {k: [] for k in c}
    ev = sorted(events, key=lambda e: e[0]); i = 0
    for ti in t:
        while i < len(ev) and ti >= ev[i][0]:
            c = ev[i][1](dict(c)); i += 1
        for k in c: res[k].append(c[k])
        d = rate(c)
        for k in c: c[k] = max(c[k] + d[k] * dt, 0)
    return t, {k: np.array(v) for k, v in res.items()}


def fe_rate(k1=0.05, k2=0.05):
    def r(c):
        v = k1 * c["Fe"] * c["SCN"] - k2 * c["FeSCN"]
        return {"Fe": -v, "SCN": -v, "FeSCN": v}
    return r


def fe_plot(navn, events, titel, t_end=120):
    t, c = sim({"Fe": 2.0, "SCN": 1.5, "FeSCN": 0.0}, fe_rate(), t_end, events)
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    ax.plot(t, c["Fe"], color=GUL, lw=2.2); ax.plot(t, c["SCN"], color=GRAA, lw=2.2); ax.plot(t, c["FeSCN"], color=ROED, lw=2.2)
    y = {"Fe": c["Fe"][-1], "SCN": c["SCN"][-1], "FeSCN": c["FeSCN"][-1]}
    for k, lab, col in (("Fe", r"Fe$^{3+}$", GUL), ("SCN", r"SCN$^{-}$", GRAA), ("FeSCN", r"FeSCN$^{2+}$", ROED)):
        ax.text(t_end * 1.01, y[k], lab, color=col, va="center", fontsize=10, fontweight="bold")
    for te, _ in events:
        ax.axvline(te, color="k", ls=":", lw=1)
    ax.set_title(titel); akser(ax); ax.set_xlim(0, t_end); ax.set_ylim(0, max(3.2, max(c["Fe"]) * 1.1))
    gem(fig, navn)


# ---------- g01: ligevægt indstiller sig, A <=> B ----------
k1, k2 = 0.10, 0.05
t, c = sim({"A": 1.0, "B": 0.0}, lambda c: {"A": -(k1*c["A"]-k2*c["B"]), "B": k1*c["A"]-k2*c["B"]}, 80)
fig, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot(t, c["A"], color=BLAA, lw=2.2, label="[A]"); ax.plot(t, c["B"], color=ROED, lw=2.2, label="[B]")
ax.legend(loc="center right"); ax.set_title(r"A $\rightleftharpoons$ B"); akser(ax, yl="koncentration / M")
ax.set_xlim(0, 80); ax.set_ylim(0, 1.05); gem(fig, "g01-indstilling")

# ---------- g02: hastigheder frem og tilbage ----------
fig, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot(t, k1*c["A"], color="#16A085", lw=2.2, label="kurve 1"); ax.plot(t, k2*c["B"], color="#8E44AD", lw=2.2, label="kurve 2")
ax.legend(loc="center right"); ax.set_title(r"Reaktionshastigheder for A $\rightleftharpoons$ B"); akser(ax, yl="hastighed / (M/s)")
ax.set_xlim(0, 80); gem(fig, "g02-hastigheder")

# ---------- g03-g05: jernthiocyanat med indgreb ved t = 60 s ----------
def add_fe(c): c["Fe"] += 1.2; return c
def fjern_scn(c): c["SCN"] *= 0.35; return c
def fortynd(c): return {k: v / 2 for k, v in c.items()}
fe_plot("g03-fe-indgreb", [(60, add_fe)], r"Fe$^{3+}$ + SCN$^{-}$ $\rightleftharpoons$ FeSCN$^{2+}$")
fe_plot("g04-scn-indgreb", [(60, fjern_scn)], r"Fe$^{3+}$ + SCN$^{-}$ $\rightleftharpoons$ FeSCN$^{2+}$")
fe_plot("g05-fortynding", [(60, fortynd)], r"Fe$^{3+}$ + SCN$^{-}$ $\rightleftharpoons$ FeSCN$^{2+}$")

# ---------- g06: N2O4 <=> 2NO2, volumen halveres ved t = 60 s ----------
ka, kb = 0.02, 0.05   # K = ka/kb = 0,4 M
def r_n(c):
    v = ka*c["N2O4"] - kb*c["NO2"]**2
    return {"N2O4": -v, "NO2": 2*v}
t, c = sim({"N2O4": 0.75, "NO2": 0.548}, r_n, 120, [(60, lambda c: {k: 2*v for k, v in c.items()})])
fig, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot(t, c["N2O4"], color=GRAA, lw=2.2); ax.plot(t, c["NO2"], color="#A0522D", lw=2.2)
ax.text(121, c["N2O4"][-1], r"N$_2$O$_4$", color=GRAA, va="center", fontweight="bold")
ax.text(121, c["NO2"][-1], r"NO$_2$", color="#A0522D", va="center", fontweight="bold")
ax.axvline(60, color="k", ls=":", lw=1)
ax.set_title(r"N$_2$O$_4$(g) $\rightleftharpoons$ 2NO$_2$(g)"); akser(ax, yl="koncentration / M"); ax.set_xlim(0, 120)
gem(fig, "g06-volumen")

# ---------- g07: temperaturændring (ingen spring) ----------
dt = 0.01; t = np.arange(0, 120 + dt, dt)
A = []; B = []; C = []; a, b, cc = 2.0, 1.5, 0.0
for ti in t:
    kb_ = 0.05 if ti < 60 else 0.25   # højere temperatur: tilbagereaktionen (endoterm) bliver relativt hurtigere
    v = 0.05*a*b - kb_*cc
    A.append(a); B.append(b); C.append(cc)
    a -= v*dt; b -= v*dt; cc += v*dt
fig, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot(t, A, color=BLAA, lw=2.2); ax.plot(t, B, color=GRAA, lw=2.2); ax.plot(t, C, color=ROED, lw=2.2)
for y, lab, col in ((A[-1], "A", BLAA), (B[-1], "B", GRAA), (C[-1], "C", ROED)):
    ax.text(121, y, lab, color=col, va="center", fontweight="bold")
ax.axvline(60, color="k", ls=":", lw=1)
ax.set_title(r"A + B $\rightleftharpoons$ C     (eksoterm mod højre)"); akser(ax); ax.set_xlim(0, 120)
gem(fig, "g07-temperatur")

# ---------- g08: katalysator ----------
fig, ax = plt.subplots(figsize=(5.6, 3.0))
for kf, col, lab in ((0.03, ROED, "uden katalysator"), (0.15, "#E67E22", "med katalysator")):
    t, c = sim({"A": 1.0, "B": 0.0}, lambda c, kf=kf: {"A": -(kf*c["A"]-kf/2*c["B"]), "B": kf*c["A"]-kf/2*c["B"]}, 120)
    ax.plot(t, c["B"], color=col, lw=2.2, label=lab)
ax.legend(loc="lower right"); ax.set_title(r"[B] for A $\rightleftharpoons$ B"); akser(ax, yl="[B] / M"); ax.set_xlim(0, 120); ax.set_ylim(0, 0.8)
gem(fig, "g08-katalysator")

# ---------- g09: A <=> 2B, aflæs og beregn K ----------
kc, kd = 0.08, 0.15   # K = kc/kd = 0,533 M -> ligevægt [A] = 0,30 M, [B] = 0,40 M
t, c = sim({"A": 0.50, "B": 0.0}, lambda c: {"A": -(kc*c["A"]-kd*c["B"]**2), "B": 2*(kc*c["A"]-kd*c["B"]**2)}, 100)
fig, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot(t, c["A"], color=BLAA, lw=2.2, label="[A]"); ax.plot(t, c["B"], color=ROED, lw=2.2, label="[B]")
ax.legend(loc="center right"); ax.set_title(r"A $\rightleftharpoons$ 2B"); akser(ax, yl="koncentration / M")
ax.set_xlim(0, 100); ax.set_ylim(0, 0.55); ax.set_yticks(np.arange(0, 0.55, 0.1)); gem(fig, "g09-beregn-k")


# ---------- glas-billeder ----------
def glas(ax, x, farve, label="", bund=None, top=None):
    """Reagensglas med væske. bund: farve på bundfald."""
    w, h, yb = 0.7, 2.6, 0.3
    ax.add_patch(Rectangle((x - w/2, yb + w/2), w, 1.6, color=farve, zorder=1))
    ax.add_patch(Wedge((x, yb + w/2), w/2, 180, 360, color=farve, zorder=1))
    if bund:   # uklart bundfald: prikker i bunden
        rng = np.random.default_rng(1)
        px = x + rng.uniform(-w/2 + 0.06, w/2 - 0.06, 260); py = yb + rng.uniform(0.04, 0.55, 260)
        ok = (py > yb + w/2) | ((px - x)**2 + (py - yb - w/2)**2 < (w/2 - 0.05)**2)
        ax.scatter(px[ok], py[ok], s=5, color=bund, zorder=2)
    ax.plot([x - w/2, x - w/2], [yb + w/2, yb + h], color="k", lw=1.6, zorder=3)
    ax.plot([x + w/2, x + w/2], [yb + w/2, yb + h], color="k", lw=1.6, zorder=3)
    th = np.linspace(np.pi, 2*np.pi, 60)
    ax.plot(x + w/2*np.cos(th), yb + w/2 + w/2*np.sin(th), color="k", lw=1.6, zorder=3)
    if label:
        ax.text(x, yb - 0.25, label, ha="center", va="top", fontsize=11)


def glas_fig(navn, farver, labels, pile=(), bund=None, figsize=(5.2, 2.9), afst=2.6):
    fig, ax = plt.subplots(figsize=figsize)
    xs = [1 + afst*i for i in range(len(farver))]
    for i, (x, f, l) in enumerate(zip(xs, farver, labels)):
        glas(ax, x, f, l, bund=(bund or {}).get(i))
    for (i, txt) in pile:
        a = FancyArrowPatch((xs[i] + 0.5, 1.6), (xs[i+1] - 0.5, 1.6), arrowstyle="-|>", mutation_scale=18, lw=1.8, color="k")
        ax.add_patch(a); ax.text((xs[i] + xs[i+1]) / 2, 1.85, txt, ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.set_xlim(0, xs[-1] + 1); ax.set_ylim(-0.6, 3.1); ax.set_aspect("equal"); ax.axis("off")
    gem(fig, navn)

RED, MOERKROED, BLEG = "#C0392B", "#7B0D0D", "#F5D76E"
glas_fig("b01-mere-roed", [RED, MOERKROED], ["før", "efter"], pile=[(0, "+ ?")])
glas_fig("b02-bleg", [RED, BLEG], ["før", "efter"], pile=[(0, "+ ?")])
glas_fig("b03-cu-hcl", [BLAA, GROEN], ["før", "efter"], pile=[(0, "+ konc. HCl")], afst=3.2)
glas_fig("b04-cu-vand", [GROEN, BLAA], ["før", "efter"], pile=[(0, "+ vand")])
glas_fig("b05-cu-nh3", [LYSBLAA, MOERKBLAA, LYSBLAA], ["1", "2", "3"], pile=[(0, r"+ NH$_3$"), (1, r"+ H$_2$SO$_4$")], figsize=(6.2, 2.9))
glas_fig("b06-cu-bundfald", [LYSBLAA, LYSBLAA], ["før", "efter"], pile=[(0, r"+ 2 dråber NH$_3$")], bund={1: "#1F618D"}, afst=3.4)
glas_fig("b07-no2-temp", ["#E8C9A6", "#7B3F1D"], ["glas A", "glas B"])
glas_fig("b08-feha", [RED, "#E59866"], ["før", "efter"], pile=[(0, "+ konc. HCl")], afst=3.2)
print("Grafer gemt i", OUT)
