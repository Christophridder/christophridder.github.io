# Laver grafer til nat/lineaer-regression.md. Kør fra denne mappe; output i out/ -> kopiér til static/img/linreg/
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.spines.top":False,"axes.spines.right":False,
  "axes.grid":True,"grid.color":"#e2e8f0","grid.linewidth":0.8,"axes.edgecolor":"#475569","svg.fonttype":"path"})
BLUE="#2563eb"; RED="#dc2626"; GREY="#475569"
komma=FuncFormatter(lambda v,p: (f"{v:g}").replace(".",","))
def mf(v,d): return f"{v:.{d}f}".replace(".","{,}")
def fmt(v,d): return f"{v:.{d}f}".replace(".",",")
def fig(x,y,xl,yl,title,fil,fit=True,deg=1,xlim=None,ylim=None,eq=None):
    f,ax=plt.subplots(figsize=(6.4,3.6))
    ax.plot(x,y,"o",color=BLUE,ms=7,zorder=3,label="målinger")
    if fit:
        a,b=np.polyfit(x,y,1); xx=np.linspace(0 if xlim is None else xlim[0],(xlim or (0,max(x)*1.1))[1],200)
        ax.plot(xx,a*xx+b,"-",color=RED,lw=1.6,label="tendenslinje",zorder=2)
        r2=np.corrcoef(x,y)[0,1]**2
        ax.text(0.03,0.95,eq or f"$y = {mf(a,3)}\\cdot x + {mf(b,2)}$\n$R^2 = {mf(r2,5)}$",transform=ax.transAxes,va="top",fontsize=11,
                bbox=dict(boxstyle="round,pad=0.4",fc="white",ec="#cbd5e1"))
    ax.set_xlabel(xl,color=GREY); ax.set_ylabel(yl,color=GREY); ax.set_title(title,color="#1e293b",fontsize=12,loc="left")
    ax.xaxis.set_major_formatter(komma); ax.yaxis.set_major_formatter(komma)
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    f.tight_layout(); f.savefig("out/"+fil,transparent=False,facecolor="white"); plt.close(f)
# 1 densitet
V=np.array([20,40,60,80,100.]); m=np.array([88.3,108.4,128.3,148.4,168.1])
a,b=np.polyfit(V,m,1); print("densitet a,b,R2",a,b,np.corrcoef(V,m)[0,1]**2)
fig(V,m,"Volumen $V$ (mL)","Samlet masse $m$ (g)","Vand i målekolbe (vægten ikke nulstillet)","linreg-densitet.svg",xlim=(0,110),ylim=(0,180))
# 2 terninger
k=np.array([1,2,3,4,5.]); n=k**3
fig(k,n,"Kantlængde $a_{akse}$ (antal terninger)","Antal terninger $a_{tot}$","Terninger – ikke lineært","linreg-terninger.svg",fit=False,xlim=(0,5.5),ylim=(0,135))
fig(k**3,n,"$a_{akse}^3$","Antal terninger $a_{tot}$","Terninger – efter aksetransformation","linreg-terninger-lineariseret.svg",xlim=(0,135),ylim=(0,135),
    eq="$y = 1\\cdot x + 0$\n$R^2 = 1$")
# 3 gnidning (facit)
FN=np.array([3.0,5.5,8.0,10.0,12.0,15.0,17.0]); Fg=np.array([0.92,1.49,2.11,2.55,3.05,3.73,4.23])
a,b=np.polyfit(FN,Fg,1); print("gnid a,b,R2",a,b,np.corrcoef(FN,Fg)[0,1]**2)
fig(FN,Fg,"Normalkraft $F_N$ (N)","Gnidningskraft $F_{gnid}$ (N)","Gnidning – facit","linreg-gnidning.svg",xlim=(0,18),ylim=(0,4.6))
# 4 varmekapacitet (fysik/Metoder/lineaer-regression.md): vand i elkedel, m = 0,888 kg, T_start = 22 °C
mv=0.888; T=np.array([22.0,29.6,35.1,43.8,51.9,60.7,72.3,83.4]); E=np.array([0,31600,53800,88400,120500,156000,202100,247100.])
xv=mv*(T-22.0); a,b=np.polyfit(xv,E,1); r2=np.corrcoef(xv,E)[0,1]**2; print("varmekap a,b,R2",a,b,r2)
fig(xv,E,"$m\\cdot\\Delta T$ (kg·K)","Tilført energi $E$ (J)","Vand i elkedel","linreg-varmekapacitet.svg",xlim=(0,58),ylim=(0,270000),
    eq=f"$y = {mf(a,0)}\\cdot x + {mf(b,0)}$\n$R^2 = {mf(r2,5)}$")
# 5 E/(m·ΔT) for hver måling: "den dumme løsning"
f,ax=plt.subplots(figsize=(6.4,3.4)); dT=T[1:]-22.0; q=E[1:]/(mv*dT)
ax.plot(dT,q,"o",color=BLUE,ms=7,zorder=3,label="$E/(m\\cdot\\Delta T)$ for hver måling")
ax.axhline(a,color=RED,lw=1.6,label=f"hældning fra regression: {fmt(a,0)}")
ax.axhline(4180,color=GREY,lw=1.2,ls="--",label="tabelværdi for vand: 4180")
ax.set_xlabel("$\\Delta T$ (K)",color=GREY); ax.set_ylabel("J/(kg·K)",color=GREY); ax.set_xlim(0,65); ax.set_ylim(4100,4750)
ax.set_title("Divider hver måling for sig",color="#1e293b",fontsize=12,loc="left"); ax.xaxis.set_major_formatter(komma)
ax.legend(fontsize=9,loc="upper right",frameon=True); f.tight_layout(); f.savefig("out/linreg-varmekapacitet-division.svg",facecolor="white"); plt.close(f)
# 6 gnidning med masser (facit til opgaven på fysik/Metoder/lineaer-regression.md)
mg_=np.array([0.30,0.55,0.80,1.05,1.30,1.55,1.80])*9.82; Fg2=np.array([0.92,1.37,2.05,2.61,3.20,3.80,4.33])
a,b=np.polyfit(mg_,Fg2,1); print("gnid-masse a,b,R2",a,b,np.corrcoef(mg_,Fg2)[0,1]**2)
fig(mg_,Fg2,"$m\\cdot g$ (N)","Gnidningskraft $F_{gnid}$ (N)","Gnidning – facit","linreg-gnidning-masse.svg",xlim=(0,19),ylim=(0,4.8))
