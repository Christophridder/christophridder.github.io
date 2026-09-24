"""Tegner graferne til quiz-og-byt kortene om integration.
Kør fra crsite-roden:  python3 scripts/quizkort/graphs_integration.py
Gemmer SVG (web) og PDF (print) i static/img/quiz-integration/"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "static", "img", "quiz-integration")
BLUE, FILL, RED = "#2471A3", "#AED6F1", "#F5B7B1"
comma = FuncFormatter(lambda v, p: f"{v:g}".replace(".", ","))

def ax_setup(xlabel, ylabel, xmax, ymax, xstep, ystep, ymin=0, xlab=None, ylab=None):
    fig, ax = plt.subplots(figsize=(3.9, 2.05))
    ax.set_xlim(0, xmax); ax.set_ylim(ymin, ymax)
    ax.xaxis.set_minor_locator(MultipleLocator(xstep)); ax.yaxis.set_minor_locator(MultipleLocator(ystep))
    ax.xaxis.set_major_locator(MultipleLocator(xlab or xstep)); ax.yaxis.set_major_locator(MultipleLocator(ylab or ystep))
    ax.xaxis.set_major_formatter(comma); ax.yaxis.set_major_formatter(comma)
    ax.grid(which="both", color="#cbd5e1", lw=0.7)
    ax.set_axisbelow(True)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xlabel(xlabel, fontsize=9, labelpad=1); ax.set_ylabel(ylabel, fontsize=9, labelpad=2)
    ax.tick_params(labelsize=7.5, pad=2)
    if ymin < 0: ax.axhline(0, color="black", lw=1.2)
    return fig, ax

def save(fig, name):
    fig.tight_layout()
    for ext in ("svg", "pdf"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), facecolor="white")
    plt.close(fig)

def plot(ax, x, y, fill=True, color=FILL, where=None):
    ax.plot(x, y, color=BLUE, lw=1.8)
    if fill:
        ax.fill_between(x, y, 0, color=color, alpha=0.8, where=where, interpolate=True, lw=0)

# 1 impuls: F = 6 N i 4 s
fig, ax = ax_setup("$t$ (s)", "$F$ (N)", 5, 8, 1, 1)
x = np.array([0, 4]); plot(ax, x, [6, 6]); ax.plot([4, 4], [0, 6], color=BLUE, lw=1.8); save(fig, "g01-impuls")

# 2 trekant: v = 2t
fig, ax = ax_setup("$t$ (s)", "$v$ (m/s)", 6, 12, 1, 1, ylab=2)
x = np.linspace(0, 5); plot(ax, x, 2*x); save(fig, "g02-trekant")

# 3 trapez: 3 -> 9 m/s på 4 s
fig, ax = ax_setup("$t$ (s)", "$v$ (m/s)", 5, 10, 1, 1)
x = np.linspace(0, 4); plot(ax, x, 3 + 1.5*x); ax.plot([4, 4], [0, 9], color=BLUE, lw=1.2, ls="--"); save(fig, "g03-trapez")

# 4 a til b: v = 3t, farv 2-4 s
fig, ax = ax_setup("$t$ (s)", "$v$ (m/s)", 5, 15, 1, 1, ylab=3)
x = np.linspace(0, 5); ax.plot(x, 3*x, color=BLUE, lw=1.8)
xs = np.linspace(2, 4); ax.fill_between(xs, 3*xs, 0, color=RED, alpha=0.9, lw=0); save(fig, "g04-a-til-b")

# 5 fjeder: F = 50 x
fig, ax = ax_setup("$x$ (m)", "$F$ (N)", 0.5, 25, 0.05, 2.5, xlab=0.1, ylab=5)
x = np.linspace(0, 0.4); plot(ax, x, 50*x); save(fig, "g05-fjeder")

# 6 elkedel: 2,0 kW i 3,0 min
fig, ax = ax_setup("$t$ (min)", "$P$ (kW)", 4, 2.5, 0.5, 0.5, xlab=1)
plot(ax, np.array([0, 3]), [2, 2]); ax.plot([3, 3], [0, 2], color=BLUE, lw=1.8); save(fig, "g06-elkedel")

# 7 ladning: 500 mA i 2 h, så lineært til 0 ved 3 h
fig, ax = ax_setup("$t$ (h)", "$I$ (mA)", 3.5, 600, 0.5, 100, xlab=1)
plot(ax, np.array([0, 2, 3]), np.array([500, 500, 0])); save(fig, "g07-ladning")

# 8 sammensat: 0->8 på 4 s, 8 i 6 s, 8->0 på 2 s
fig, ax = ax_setup("$t$ (s)", "$v$ (m/s)", 13, 10, 1, 1, xlab=2, ylab=2)
plot(ax, np.array([0, 4, 10, 12]), np.array([0, 8, 8, 0])); save(fig, "g08-sammensat")

# 9 spark: F = 300 sin(pi t / 0.1), t i ms
fig, ax = ax_setup("$t$ (ms)", "$F$ (N)", 110, 350, 10, 50, xlab=20, ylab=100)
x = np.linspace(0, 100, 300); plot(ax, x, 300*np.sin(np.pi*x/100)); save(fig, "g09-spark")

# 10 negativ: v = 6 - 2t
fig, ax = ax_setup("$t$ (s)", "$v$ (m/s)", 6, 8, 1, 1, ymin=-6, ylab=2)
x = np.linspace(0, 5, 200); y = 6 - 2*x
ax.plot(x, y, color=BLUE, lw=1.8)
ax.fill_between(x, y, 0, where=y >= 0, color=FILL, alpha=0.8, interpolate=True, lw=0)
ax.fill_between(x, y, 0, where=y <= 0, color=RED, alpha=0.9, interpolate=True, lw=0)
save(fig, "g10-negativ")
print("ok")
