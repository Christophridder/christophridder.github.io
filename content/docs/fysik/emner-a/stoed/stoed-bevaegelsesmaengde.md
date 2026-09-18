---
title: "Stød og bevægelsesmængde"
weight: 3
---

**Niveau: Fysik A** · **Emne: Mekanik – bevægelsesmængde og stød** · **Eksperiment: luftpudebane**

Forløbet indfører bevægelsesmængde og impuls, bygger bevarelsessætningen op og
bruger den til at analysere elastiske og uelastiske stød i én dimension.
Kerneeksperimentet er luftpudebanen, hvor lav gnidning gør det muligt at se
bevarelsen direkte – præcis som ved den eksperimentelle delprøve.

## Del 1 – Bevægelsesmængde og impuls

Et legemes **bevægelsesmængde** (impuls i daglig tale, men pas på ordet) er

$$p = m \cdot v$$

en vektor med samme retning som farten. Enheden er kg·m/s.

Newtons 2. lov kan skrives elegant med bevægelsesmængde: kraften er den hastighed,
hvormed bevægelsesmængden ændres:

$$F = \frac{\Delta p}{\Delta t}$$

Ganges op, fås **impulssætningen** – kraftstødet er lig ændringen i
bevægelsesmængde:

$$F \cdot \Delta t = \Delta p = m \cdot \Delta v$$

Det forklarer hverdagsfysikken: en airbag forlænger $\Delta t$, så den samme
$\Delta p$ kan opnås med en meget mindre kraft $F$.

## Del 2 – Bevarelse og stødtyper

I et **lukket system** (ingen ydre kræfter langs bevægelsen) er den samlede
bevægelsesmængde **bevaret**. For to legemer i én dimension:

$$p_{\text{før}} = p_{\text{efter}} \quad\Longrightarrow\quad m_1 \cdot v_1 + m_2 \cdot v_2 = m_1 \cdot u_1 + m_2 \cdot u_2$$

hvor $v$ er farten før og $u$ farten efter. **Pas på fortegnene** – farter i
modsat retning indsættes med modsat fortegn.

Den kinetiske energi er derimod *ikke* altid bevaret. Det giver tre stødtyper:

| Stødtype | Bevægelsesmængde | Kinetisk energi | Eksempel |
|---|---|---|---|
| Elastisk | bevaret | bevaret | hårde kugler, magnetstød |
| Uelastisk | bevaret | delvist tabt | de fleste virkelige stød |
| Fuldstændig uelastisk | bevaret | mest tabt | legemerne hænger sammen (ler, velcro) |

Ved et **fuldstændig uelastisk** stød fortsætter de to legemer med samme fart, og
udtrykket bliver enkelt:

$$u = \frac{m_1 \cdot v_1 + m_2 \cdot v_2}{m_1 + m_2}$$

> **Regneeksempel (fuldstændig uelastisk):** $m_1 = 0{,}20$ kg med
> $v_1 = 0{,}50$ m/s rammer $m_2 = 0{,}30$ kg i hvile.
> $$u = \frac{0{,}20 \cdot 0{,}50 + 0}{0{,}20 + 0{,}30} = 0{,}20 \text{ m/s}$$
> Energien før er $E_{\text{kin}} = \tfrac{1}{2} \cdot 0{,}20 \cdot 0{,}50^2 = 0{,}025$ J,
> efter $\tfrac{1}{2} \cdot 0{,}50 \cdot 0{,}20^2 = 0{,}010$ J. Der er altså tabt
> $0{,}015$ J (60 %) til varme og deformation – men bevægelsesmængden er bevaret.

> **For de skarpe (elastisk stød, mål i hvile):** Med både bevægelsesmængde og
> energi bevaret fås for $v_2 = 0$:
> $$u_1 = \frac{m_1 - m_2}{m_1 + m_2} \cdot v_1 \qquad u_2 = \frac{2 \cdot m_1}{m_1 + m_2} \cdot v_1$$
> Ved ens masser giver det $u_1 = 0$ og $u_2 = v_1$ – farten overføres fuldstændigt,
> som i en Newtons vugge. Et tungt legeme mod et let sender det lette afsted med
> næsten dobbelt fart; et let mod et tungt kastes tilbage.

## Del 3 – Eksperiment: stød på luftpudebane

**Formål:** Undersøge om bevægelsesmængde og kinetisk energi er bevaret ved
forskellige stødtyper.

### Udstyr
- Luftpudebane med to vogne (lav gnidning).
- Fotoceller eller bevægelsessensorer til at måle farten før og efter stødet.
- Magneter eller fjederbøjler til **elastiske** stød; velcro eller nål-i-voks til
  **fuldstændig uelastiske** stød.
- Kendte masser (vej vognene, evt. med ekstra lodder).

### Gennemførelse
1. Mål farten af hver vogn umiddelbart før og efter stødet.
2. Gennemfør både et elastisk og et fuldstændig uelastisk stød.
3. Gentag med forskellige masseforhold (fx tung vogn mod let).

### Databehandling (Excel)
- Beregn den samlede bevægelsesmængde **før** og **efter** for hvert stød.
  → Sammenlign: er $p$ bevaret inden for måleusikkerheden?
- Beregn den samlede kinetiske energi **før** og **efter**.
  → Elastisk stød: $E_{\text{kin}}$ omtrent bevaret. Uelastisk: tydeligt fald.
- Diskutér måleusikkerheden – hvorfor passer tallene ikke *helt*? (Restgnidning,
  aflæsning af fart, ikke perfekt elastisk stød.)

> **Udvidelse – kraftmåler (impuls):** Lad en enkelt vogn støde ind i en
> kraftmåler, og registrér både $F(t)$ og vognens bevægelse. **Arealet under
> $F$-$t$-grafen** er kraftstødet $F \cdot \Delta t$, og det skal svare til
> ændringen i bevægelsesmængde $\Delta p = m \cdot \Delta v$ fra
> bevægelsessensoren. En flot direkte verifikation af impulssætningen –
> svarer til "hvis tiden tillader det" i Egaa-spørgsmål D.

> **Prøverelevant:** Hold analysen i fotoceller/sensor + Excel. Det er den
> databehandling, eleverne skal kunne stå på egne ben med til delprøven.

## Opgaver

1. En vogn på $0{,}25$ kg kører med $0{,}40$ m/s ind i en stillestående vogn på
   $0{,}15$ kg, og de hænger sammen. Bestem fællesfarten og det procentvise
   energitab.
2. To vogne kører mod hinanden: $0{,}30$ kg med $0{,}20$ m/s og $0{,}20$ kg med
   $0{,}30$ m/s (modsat retning). De hænger sammen efter stødet. Bestem fart og
   retning bagefter.
3. Forklar ud fra de elastiske stødligninger, hvorfor en kugle i en Newtons vugge
   overfører hele sin fart til den næste.
4. **Impuls:** En kraftmåler registrerer et stød, hvor arealet under $F$-$t$-grafen
   er $0{,}12$ N·s. Vognen vejer $0{,}40$ kg og var i hvile før. Bestem dens fart
   efter stødet.

## Det skal I kunne efter forløbet

- Beregne bevægelsesmængde og bruge impulssætningen $F \cdot \Delta t = \Delta p$.
- Anvende bevarelse af bevægelsesmængde på stød i én dimension med korrekte fortegn.
- Skelne elastiske og uelastiske stød ud fra, om den kinetiske energi er bevaret.
- Eftervise bevarelse eksperimentelt og forholde sig kritisk til måleusikkerheden.
