# Tegner tolkningsskemaer (teori over y = a*x + b) som SVG. Tilføj egne med skema([...],(a,b),"navn.svg")
# Tolkningsskema: teori (øverst) over y = a·x + b (nederst), med "Derfor"-bokse
import re
def lbl(t,cx,cy,size,color,italic=True):
    """Tegner fx 'a_{akse}^{3}' centreret om cx uden tspans (robust i alle renderere)."""
    m=re.match(r"^([^_^]*)(?:_\{([^}]*)\})?(?:\^\{([^}]*)\})?$",t)
    base,sub,sup=m.group(1),m.group(2) or "",m.group(3) or ""
    k=0.56; ss=round(size*0.6)
    cw=lambda c:0.9 if c in 'mwMW' else (0.35 if c in 'il1t' else k)
    wb=size*sum(cw(c) for c in base); ws=k*ss*max(len(sub),len(sup))
    x0=cx-(wb+ws)/2; st=' font-style="italic"' if italic else ''
    out=[f'<text x="{x0:.1f}" y="{cy}" font-size="{size}"{st} fill="{color}">{base}</text>']
    if sub: out.append(f'<text x="{x0+wb+1:.1f}" y="{cy+size*0.28:.1f}" font-size="{ss}"{st} fill="{color}">{sub}</text>')
    if sup: out.append(f'<text x="{x0+wb+1:.1f}" y="{cy-size*0.42:.1f}" font-size="{ss}"{st} fill="{color}">{sup}</text>')
    return "".join(out)
def skema(top,derfor,fil):
    W,H=700,210; X=90
    cols=[(X,"y"),(X+120,"a"),(X+205,"x"),(X+325,"b")]; ops=[(X+86,"="),(X+192,"·"),(X+297,"+")]
    colr={"y":"#2563eb","a":"#ea580c","x":"#2563eb","b":"#7c3aed"}
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="\'Segoe UI\', system-ui, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#fafafa" rx="8"/>',
       '<defs><marker id="ar" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,3.5 L0,7 z" fill="#475569"/></marker></defs>',
       '<text x="16" y="80" font-size="13" fill="#64748b">Teori</text>',
       '<text x="16" y="150" font-size="13" fill="#64748b">Regneark</text>']
    for (x,k),t in zip(cols,top):
        c=colr[k]
        s.append(f'<rect x="{x}" y="25" width="62" height="160" rx="14" fill="white" stroke="{c}" stroke-width="2"/>')
        if t: s.append(lbl(t,x+31,80,24,"#0f172a",italic=not t[0].isdigit()))
        s.append(f'<line x1="{x+10}" y1="105" x2="{x+52}" y2="105" stroke="#e2e8f0"/>')
        s.append(lbl(k,x+31,150,24,c))
    for x,o in ops:
        for yy in (80,150): s.append(f'<text x="{x}" y="{yy}" text-anchor="middle" font-size="24" fill="#334155">{o}</text>')
    s.append(f'<text x="{X+405}" y="112" font-size="14" fill="#475569">Derfor</text>')
    for yy,k,txt in [(35,"a",derfor[0]),(125,"b",derfor[1])]:
        c=colr[k]; bx=X+440
        s.append(f'<rect x="{bx}" y="{yy}" width="150" height="50" rx="12" fill="white" stroke="{c}" stroke-width="2"/>')
        s.append(f'<text x="{bx+22}" y="{yy+33}" font-size="22" font-style="italic" fill="{c}">{k}</text>')
        s.append(f'<text x="{bx+44}" y="{yy+33}" font-size="22" fill="#334155">=</text>')
        if txt: s.append(lbl(txt,bx+100,yy+33,22,"#0f172a",italic=not txt[0].isdigit()))
    s.append(f'<path d="M{X+151},25 C{X+180},0 {X+400},0 {X+437},55" fill="none" stroke="#475569" stroke-width="1.4" marker-end="url(#ar)"/>')
    s.append(f'<path d="M{X+356},185 C{X+370},205 {X+420},202 {X+437},165" fill="none" stroke="#475569" stroke-width="1.4" marker-end="url(#ar)"/>')
    s.append('</svg>')
    open("out/"+fil,"w",encoding="utf-8").write("\n".join(s))
skema(["m","ρ","V","m_{1}"],("ρ","m_{1}"),"tolkning-densitet.svg")
skema(["a_{tot}","1","a_{akse}^{3}","0"],("1","0"),"tolkning-terninger.svg")
skema(["","","",""],("",""),"tolkning-tom.svg")
skema(["F_{gnid}","μ","F_{N}","F_{fejl}"],("μ","F_{fejl}"),"tolkning-gnidning.svg")
