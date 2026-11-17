import numpy as np
import matplotlib.pyplot as plt

c = 299792.458  # km/s

# Farter i km/s (myonerne er angivet som brøkdel af c)
legemer = [
    ("Månen om Jorden",           1.02,      "#64748b"),
    ("Voyager 2",                 15.4,      "#0891b2"),
    ("Merkur om Solen",           47.4,      "#a16207"),
    ("Helios 2 (1976)",           70.2,      "#7c3aed"),
    ("Parker Solar Probe (2024)", 192,       "#db2777"),
    ("Stjernen S2 ved Sgr A*",    7650,      "#ea580c"),
    ("Myoner",                    0.998 * c, "#dc2626"),
]

def pæn(b):
    """v/c som dansk tal, fx 3,4·10⁻⁶ eller 0,998."""
    if b >= 0.01:
        return f"{b:.3g}".replace(".", ",")
    eks = int(np.floor(np.log10(b)))
    sup = str(eks).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{b / 10**eks:.1f}".replace(".", ",") + "·10" + sup

def lorentzfaktor(beta):
    return 1 / np.sqrt(1 - beta**2)

plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none"})
fig, (v, h) = plt.subplots(1, 2, figsize=(11, 4.6))

# Venstre: samme plot som koden på siden, med lineære akser
beta = np.linspace(0, 0.999, 800)
v.plot(beta, lorentzfaktor(beta), color="#1e3a8a", lw=2)
for navn, fart, farve in legemer:
    b = fart / c
    v.axvline(b, color=farve, ls="--", lw=1.4, label=f"{navn}: v = {pæn(b)} c")
v.set_xlim(0, 1); v.set_ylim(0, 20)
v.set_xlabel("v / c"); v.set_ylabel("Lorentz-faktor γ")
v.set_title("Lineære akser: næsten alle streger ligger i 0", fontsize=10.5)
v.legend(fontsize=7.6, loc="upper left", frameon=False)

# Højre: logaritmiske akser, så alle legemer kan skelnes. Vi viser γ − 1.
beta = np.logspace(-6.5, np.log10(0.9999), 800)
h.loglog(beta, lorentzfaktor(beta) - 1, color="#1e3a8a", lw=2)
for navn, fart, farve in legemer:
    b = fart / c
    g1 = lorentzfaktor(b) - 1 if b > 1e-3 else b**2 / 2   # undgår afrundingsfejl ved små farter
    h.plot(b, g1, "o", color=farve, ms=7, zorder=3)
    op = navn.startswith("Helios")      # Helios og Merkur ligger tæt: Helios-teksten sættes over punktet
    h.annotate(navn, (b, g1), textcoords="offset points", xytext=(-8, 8) if op else (7, -10),
               ha="right" if op else "left", fontsize=8, color=farve)
h.axhspan(1e-3, 1e3, color="#fee2e2", alpha=.5, lw=0)
h.text(2e-6, 3e-3, "Relativitet tydelig (γ − 1 > 0,001)", fontsize=8, color="#b91c1c")
h.set_xlim(2.5e-7, 2); h.set_ylim(1e-13, 1e2)
h.set_xlabel("v / c (logaritmisk)"); h.set_ylabel("γ − 1 (logaritmisk)")
h.set_title("Logaritmiske akser: γ − 1 viser, hvor meget relativitet betyder", fontsize=10.5)

fig.tight_layout()
fig.savefig("lorentzfaktor-legemer.svg")
fig.savefig("lorentzfaktor-legemer.png", dpi=110)
for navn, fart, _ in legemer:
    b = fart / c
    print(f"{navn:28s} v/c = {b:.3g}   γ-1 = {(lorentzfaktor(b)-1 if b>1e-3 else b*b/2):.3g}")
