---
title: "Raketligningen"
weight: 5
---

**Niveau: Fysik A** · **Emne: Centralbevægelse – raketter, motorkraft og raketligningen**

En raket har intet at skubbe fra i det tomme rum. Alligevel kan den sætte farten op. Her finder du ud af hvordan, og hvordan du regner på det. Det hele bygger på noget, du kender: [bevægelsesmængde og kraftens impuls]({{< relref "/docs/fysik/emner-a/stoed/stoed-bevaegelsesmaengde" >}}) og Newtons 2. og 3. lov.

## Del 1 – Hvorfor flytter en raket sig?

Forestil dig, at du står på et skateboard med fire tunge sten. Du og skateboardet vejer $60$ kg, og hver sten vejer $10$ kg. Du kaster stenene bagud, én ad gangen, med farten $u = 10$ m/s i forhold til dig selv.

Hver sten får bevægelsesmængde bagud, så du må få lige så meget fremad. Når du vejer $m$ lige før kastet, øges din fart med

$$\Delta v = u \cdot \frac{\Delta m}{m}$$

hvor $\Delta m = 10$ kg er stenens masse. Sådan går de fire kast:

| Kast | Masse $m$ før kastet | Fartøgning $\Delta v$ |
|---|---|---|
| 1 | $100$ kg | $1{,}00$ m/s |
| 2 | $90$ kg | $1{,}11$ m/s |
| 3 | $80$ kg | $1{,}25$ m/s |
| 4 | $70$ kg | $1{,}43$ m/s |
| **Samlet** | | **$4{,}79$ m/s** |

**Læg mærke til:** Kastene er ens, men hvert kast giver mere fart end det forrige, fordi du er blevet lettere.

En raket gør præcis det samme. Den kaster bare mange, ganske små portioner gas bagud i stedet for fire sten. Derfor skubber raketten ikke fra på noget. Den skubber til sin egen udstødning.

## Del 2 – Motorkraften

Lad os finde den kraft, der skubber raketten.

- På tiden $\Delta t$ sender motoren massen $\Delta m$ ud bagud med **udstødningsfarten** $u$ i forhold til raketten.
- Den portion får bevægelsesmængden $\Delta p = \Delta m \cdot u$.
- Kraftens impuls er $F \cdot \Delta t = \Delta p$. Det giver kraften på gassen.
- Efter Newtons 3. lov er kraften på raketten lige så stor og modsat rettet.

$$F = u \cdot \frac{\Delta m}{\Delta t}$$

Brøken $\dfrac{\Delta m}{\Delta t}$ fortæller, hvor mange kg gas motoren sender ud pr. sekund. Den måles i kg/s.

**Eksempel.** En motor sender $5{,}0$ kg gas ud pr. sekund med $u = 2000$ m/s. Så er motorkraften $F = 2000\ \text{m/s} \cdot 5{,}0\ \text{kg/s} = 1{,}0 \cdot 10^{4}$ N.

## Del 3 – Raket i det tomme rum

Vi starter med det enkleste tilfælde: en raket langt ude i rummet. Der er ingen luft, og vi ser bort fra tyngdekraften. Motorkraften er den eneste kraft, så Newtons 2. lov giver

$$m(t) \cdot a = u \cdot \frac{\Delta m}{\Delta t}$$

Højresiden er motorkraften fra Del 2. Når $u$ og $\Delta m/\Delta t$ er konstante, er kraften konstant. Men massen falder hele tiden. Efter tiden $t$ er den

$$m(t) = m_0 - \frac{\Delta m}{\Delta t} \cdot t$$

Her er $m_0$ massen ved start. Derfor bliver accelerationen større og større, selvom kraften ikke ændrer sig:

$$a(t) = \frac{F}{m(t)}$$

{{< sim raket-rum.html 710 >}}

Raketten flyver vandret mod højre. Den grønne tank tømmes, og pilen for motorkraften er lige lang hele vejen. Se på graferne:

- **Acceleration:** Den grå linje er vandret, fordi massen er konstant i den tænkte raket. Den blå linje stiger, fordi raketten bliver lettere.
- **Fart:** Den grå linje er ret. Den blå linje krummer opad og ender langt over den grå.
- **Det lyseblå felt** $u \cdot \ln(m_0/m)$ viser hele tiden det samme som farten. Det er raketligningen, som vi nu udleder.

### Udledning af raketligningen

Vi går ud fra ligningen ovenfor og skriver accelerationen som $a = \Delta v/\Delta t$:

$$m \cdot \frac{\Delta v}{\Delta t} = u \cdot \frac{\Delta m}{\Delta t}$$

Vi ganger på begge sider med $\Delta t$. Så forsvinder tiden:

$$m \cdot \Delta v = u \cdot \Delta m$$

Dernæst dividerer vi med $m$:

$$\Delta v = u \cdot \frac{\Delta m}{m}$$

Det er den samme formel som på skateboardet. Den siger, at en lille portion brændstof $\Delta m$ giver en lille fartøgning $\Delta v$, og at fartøgningen er størst, når raketten er let.

Den samlede fartændring er summen af alle portionerne. Massen er ikke den samme for hver portion, så vi kan ikke bare gange. Når portionerne bliver uendeligt små, bliver summen et integral over massen, fra slutmassen $m_{\text{slut}}$ til startmassen $m_0$:

$$\Delta v = u \cdot \int_{m_{\text{slut}}}^{m_0} \frac{1}{m}\ dm = u \cdot (\ln m_0 - \ln m_{\text{slut}})$$

Resultatet er **raketligningen**, hvor vi fra nu af bare skriver $m$ for slutmassen:

$$\Delta v = u \cdot \ln\left(\frac{m_0}{m}\right)$$

| Symbol | Betydning |
|---|---|
| $\Delta v$ | Fartændringen |
| $u$ | Udstødningsfarten i forhold til raketten |
| $m_0$ | Massen ved start |
| $m$ | Massen til sidst |

Tjek med skateboardet: $10\ \text{m/s} \cdot \ln(100/60) = 5{,}11$ m/s. Det er lidt mere end de $4{,}79$ m/s, fordi fire store kast ikke er helt det samme som mange små.

### Sådan læser du ligningen

Det er **forholdet** $m_0/m$, der tæller:

| Forhold $m_0/m$ | Andel af startmassen, der er brændstof | $\Delta v/u$ |
|---|---|---|
| $2$ | $50$ % | $0{,}69$ |
| $3$ | $67$ % | $1{,}10$ |
| $6$ | $83$ % | $1{,}79$ |
| $10$ | $90$ % | $2{,}30$ |
| $20$ | $95$ % | $3{,}00$ |

- Hver gang raketten halverer sin masse, får den samme fartøgning: $0{,}69 \cdot u$.
- Du kan få dobbelt fart ved at fordoble $u$. Men hvis du vil gøre det med mere brændstof, skal $m_0/m$ sættes i **anden**.

**Undersøg selv**

1. **Tjek ligningen.** Vælg $80$ t brændstof og $u = 3{,}0$ km/s. Beregn slutfarten med raketligningen, og sammenlign med animationen.
2. **Mere brændstof.** Hvad sker der med slutfarten, når du går fra $40$ t til $80$ t brændstof? Bliver den dobbelt så stor?
3. **Større $u$.** Fordobl $u$ fra $1{,}5$ til $3{,}0$ km/s. Hvad sker der med slutfarten?

## Del 4 – Raket, der starter fra Jorden

Nu starter raketten lodret fra jordoverfladen. Så virker der to kræfter: motorkraften $F$ opad og tyngdekraften $m(t) \cdot g$ nedad. Den resulterende kraft er forskellen mellem dem:

$$F_{\text{res}} = F - m(t) \cdot g$$

Newtons 2. lov siger $m(t) \cdot a = F_{\text{res}}$, så

$$m(t) \cdot a = F - m(t) \cdot g$$

| Led | Betydning |
|---|---|
| $m(t) \cdot a$ | Massen på det tidspunkt gange accelerationen |
| $F$ | Motorkraften. Den er konstant og peger opad |
| $m(t) \cdot g$ | Tyngdekraften. Den peger nedad og bliver mindre, fordi massen falder |

Vi vil gerne have $a$ alene, så vi dividerer hele ligningen med $m(t)$:

$$a(t) = \frac{F}{m(t)} - g$$

Det er en vigtig formel:

- Brøken vokser, fordi nævneren bliver mindre.
- $g$ er konstant, fordi massen går ud i det sidste led.
- Accelerationen er altså **ikke** konstant, og du må ikke bruge formlerne for jævnt accelereret bevægelse under hele opsendelsen.
- Raketten letter kun, hvis $F > m \cdot g$, så brøken er større end $g$.

{{< sim raket.html 690 >}}

Raketten står nu lodret, og der er kommet en pil for tyngdekraften.

**Undersøg selv**

1. **Kræfterne.** Start raketten, og se pilene. Hvilken pil ændrer sig? Hvorfor?
2. **To raketter.** Sammenlign den blå og den grå graf. Hvor stor fejl laver du, hvis du regner med konstant masse?
3. **For svag motor.** Sæt $u$ til $1{,}5$ km/s. Raketten bliver stående i starten og letter først senere. Hvorfor?
4. **Sammenlign med rummet.** Brug samme indstillinger i begge animationer. Hvor meget mindre er slutfarten fra Jorden?

### Raketligningen med tyngdekraft

Accelerationen har nu to led. Det første led giver raketligningen fra Del 3. Det andet led er konstant, og $g$ trækker derfor farten $g \cdot t$ ned i løbet af tiden $t$:

$$\Delta v = u \cdot \ln\left(\frac{m_0}{m}\right) - g \cdot t$$

Du kan tjekke det i animationen: Med $u = 3000$ m/s, $m_0 = 100$ t, $m = 20$ t og $t = 160$ s giver formlen $3257$ m/s. Det er de $4828$ m/s fra rummet minus $1571$ m/s til tyngdekraften.

### Derfor er raketter næsten kun brændstof

ISS har farten $7{,}7$ km/s (se [de tre baner]({{< relref "gravitationsloven" >}})). Med tabene til tyngdekraft og luftmodstand skal en raket typisk have $\Delta v \approx 9{,}4$ km/s. Med $u = 3$ km/s bliver det

$$\frac{m_0}{m} = e^{9{,}4/3} \approx 23$$

Omkring $96$ % af startmassen skal altså være brændstof. Derfor er raketter bygget i **trin**: Når en tank er tom, smider raketten den, så den ikke skal slæbe på den tomme vægt.

> **Model:**
> - **$u$ er konstant.** Det passer godt for en raketmotor, men ikke for en vandraket, hvor trykket falder.
> - **Ingen luftmodstand.** Det er fint i rummet og ved lave farter, men ikke for en rigtig raket i atmosfæren.
> - **$g$ er konstant** i formlen med $g \cdot t$. Det gælder kun tæt på Jorden. Læs om det i [Newtons gravitationslov]({{< relref "gravitationsloven" >}}).
> - **Lodret start.** Går raketten på skrå, eller er den i bane, skal formlen med $g \cdot t$ ændres.

## Del 5 – Sådan griber du en opgave an

Start med at spørge: **Hvad skal jeg finde?** Her er $m_{\text{b}}$ massen af det brændstof, motoren bruger.

| Du skal finde | Brug |
|---|---|
| Motorkraften | $F = u \cdot \dfrac{\Delta m}{\Delta t}$ |
| Hvor længe motoren brænder | $t = \dfrac{m_{\text{b}}}{\Delta m/\Delta t}$ |
| Massen på et bestemt tidspunkt | $m(t) = m_0 - \dfrac{\Delta m}{\Delta t} \cdot t$ |
| Accelerationen på et bestemt tidspunkt | $a(t) = \dfrac{F}{m(t)} - g$ |
| Farten, når motoren slukker | $\Delta v = u \cdot \ln\left(\dfrac{m_0}{m}\right) - g \cdot t$ |
| Højden under brændingen | Numerisk integration, fordi $a$ ikke er konstant |
| Højden, efter motoren er slukket | $h = \dfrac{v^2}{2g}$ |

<details>
<summary><strong>Hvor kommer formlerne fra?</strong></summary>

**Allerede udledt længere oppe:**

| Formel | Udledt i |
|---|---|
| $F = u \cdot \dfrac{\Delta m}{\Delta t}$ | Del 2 |
| $m(t) = m_0 - \dfrac{\Delta m}{\Delta t} \cdot t$ | Del 3 |
| $\Delta v = u \cdot \ln(m_0/m)$ | Del 3 |
| $a(t) = \dfrac{F}{m(t)} - g$ | Del 4 |
| $\Delta v = u \cdot \ln(m_0/m) - g \cdot t$ | Del 4 |

**Brændetiden.** Motoren sender $\Delta m/\Delta t$ kg ud hvert sekund. Efter tiden $t$ er den samlede masse derfor $m_{\text{b}} = \dfrac{\Delta m}{\Delta t} \cdot t$. Isolér $t$:

$$t = \frac{m_{\text{b}}}{\Delta m/\Delta t}$$

**Højden, efter motoren er slukket.** Nu virker kun tyngdekraften, så den mekaniske energi er bevaret. Al bevægelsesenergi bliver til potentiel energi i toppen:

$$\tfrac{1}{2} \cdot m \cdot v^2 = m \cdot g \cdot h \quad\Longrightarrow\quad h = \frac{v^2}{2g}$$

Massen går ud. Husk at lægge højden fra brændingen til.

**Højden under brændingen.** Du kan ikke bruge $s = \tfrac{1}{2} \cdot a \cdot t^2$, for $a$ er ikke konstant. I stedet deler du tiden op i små skridt $\Delta t$, hvor $a$ næsten er konstant. For hvert skridt gør du tre ting:

1. Beregn accelerationen: $a = F/m - g$.
2. Opdatér farten og højden: $v = v + a \cdot \Delta t$ og $s = s + v \cdot \Delta t$.
3. Opdatér massen: $m = m - \dfrac{\Delta m}{\Delta t} \cdot \Delta t$.

Det er præcis det, Python-programmet i Eksempel 1 gør.

**Formlen uden massetab.** Hvis massen næsten er konstant, er $a$ næsten konstant. Så er $a = \Delta v/\Delta t$ over hele brændingen. Newtons 2. lov $F = m \cdot a$ giver

$$F \cdot \Delta t = m \cdot \Delta v$$

</details>

### Må jeg se bort fra massetabet?

Ja, hvis brændstoffet kun er en lille del af massen. Så er $m$ næsten konstant, og du kan regne med kraftens impuls:

$$F \cdot \Delta t = m \cdot \Delta v$$

**Tommelfingerregel:** Beregn $\Delta m/m_0$. Er den under nogle få procent, er fejlen lille. Tjek det altid, og skriv det i din besvarelse.

## Eksempel 1 – Vandraket i klasselokalet

Du har lavet en vandraket af en colaflaske med finner. Den står på gulvet i et lokale med $3{,}0$ m til loftet.

- Den tomme flaske vejer $100$ g.
- Der er $200$ g vand i flasken.
- Vandet sprøjter ud med farten $u = 7{,}0$ m/s i forhold til flasken.
- Alt vandet er ude efter $0{,}10$ s.

{{< sim vandraket.html 500 >}}

**Animationen stopper, når vandet er ude. Regn nu selv:**

**a)** Bestem $\Delta m/\Delta t$ og motorkraften.

**b)** Bestem accelerationen lige efter start og lige før vandet er ude.

**c)** Bestem farten, når vandet er ude.

**d)** Når raketten op til loftet? Du kan regne med, at den når ca. $0{,}3$ m op, mens vandet sprøjter ud.

<details>
<summary><strong>Se løsningen til a</strong></summary>

$$\frac{\Delta m}{\Delta t} = \frac{0{,}200\ \text{kg}}{0{,}10\ \text{s}} = 2{,}0\ \text{kg/s}$$

$$F = u \cdot \frac{\Delta m}{\Delta t} = 7{,}0\ \text{m/s} \cdot 2{,}0\ \text{kg/s} = 14\ \text{N}$$

</details>

<details>
<summary><strong>Se løsningen til b</strong></summary>

Lige efter start er massen $0{,}300$ kg, og lige før vandet er ude er den $0{,}100$ kg:

$$a_{\text{start}} = \frac{14\ \text{N}}{0{,}300\ \text{kg}} - 9{,}82\ \text{m/s}^2 = 37\ \text{m/s}^2$$

$$a_{\text{slut}} = \frac{14\ \text{N}}{0{,}100\ \text{kg}} - 9{,}82\ \text{m/s}^2 = 130\ \text{m/s}^2$$

Accelerationen bliver ca. $3{,}5$ gange større, selvom motorkraften er den samme.

</details>

<details>
<summary><strong>Se løsningen til c</strong></summary>

Massen går fra $0{,}300$ kg til $0{,}100$ kg på $0{,}10$ s:

$$\Delta v = 7{,}0\ \text{m/s} \cdot \ln\left(\frac{0{,}300}{0{,}100}\right) - 9{,}82\ \text{m/s}^2 \cdot 0{,}10\ \text{s} = 7{,}69\ \text{m/s} - 0{,}98\ \text{m/s} = 6{,}7\ \text{m/s}$$

</details>

<details>
<summary><strong>Se løsningen til d</strong></summary>

Efter vandet er ude, virker kun tyngdekraften. Bevægelsesenergien bliver til potentiel energi:

$$h = \frac{v^2}{2g} = \frac{(6{,}7\ \text{m/s})^2}{2 \cdot 9{,}82\ \text{m/s}^2} = 2{,}3\ \text{m}$$

Den samlede højde er ca. $0{,}3\ \text{m} + 2{,}3\ \text{m} = 2{,}6$ m. **Raketten når ikke loftet**, men den mangler kun ca. $40$ cm.

Tryk nu på *Afslør resten af flyvningen* i animationen.

**Hvad hvis du havde glemt massetabet?** Med konstant masse er $a = 37$ m/s² under hele brændingen. Så bliver farten kun $3{,}7$ m/s, og raketten når kun ca. $0{,}9$ m. Massetabet giver altså næsten tre gange så stor højde.

**Hvor kom $0{,}3$ m fra?** Fordi $a$ vokser, skal den findes numerisk. Dette lille program regner tiden igennem i små skridt og giver $v = 6{,}7$ m/s og $s = 0{,}27$ m:

```python
g = 9.82; u = 7.0; dmdt = 2.0; F = u * dmdt
m = 0.300; v = 0; s = 0; t = 0; dt = 0.0001

while t < 0.10:
    a = F / m - g
    v = v + a * dt
    s = s + v * dt
    m = m - dmdt * dt
    t = t + dt

print(v, s)
```

**Modelkommentar:**

- Luftmodstanden er ignoreret. Med et rimeligt skøn koster den ca. $0{,}1$ m.
- $u$ er ikke konstant i en rigtig vandraket, for trykket falder, når vandet forsvinder. $7{,}0$ m/s er en gennemsnitsværdi. Den svarer til ca. $0{,}4$ bar overtryk ved start, hvor $u$ falder fra ca. $9$ m/s til ca. $5$ m/s. En beregning med faldende tryk giver næsten samme højde.

</details>

## Eksempel 2 – Satellit i bane

En satellit med massen $1200$ kg, inklusiv $100$ kg brændstof, skal sætte farten op. Motoren er rettet langs banen, og den bruger $0{,}50$ kg brændstof pr. sekund. Udstødningsfarten er $2800$ m/s. Satellitten bruger alt brændstoffet.

**a)** Bestem motorkraften.

**b)** Hvor længe brænder motoren?

**c)** Bestem fartændringen med raketligningen.

**d)** Bestem fartændringen med $F \cdot \Delta t = m \cdot \Delta v$, hvor du ser bort fra massetabet. Hvor stor er fejlen?

<details>
<summary><strong>Se løsningen</strong></summary>

**a)** $F = u \cdot \dfrac{\Delta m}{\Delta t} = 2800\ \text{m/s} \cdot 0{,}50\ \text{kg/s} = 1{,}4 \cdot 10^{3}$ N

**b)** $t = \dfrac{m_{\text{b}}}{\Delta m/\Delta t} = \dfrac{100\ \text{kg}}{0{,}50\ \text{kg/s}} = 200$ s

**c)** Slutmassen er $1100$ kg. Tyngdekraften står vinkelret på bevægelsen, så den ændrer ikke farten undervejs, og leddet $g \cdot t$ er ikke med:

$$\Delta v = 2800\ \text{m/s} \cdot \ln\left(\frac{1200}{1100}\right) = 244\ \text{m/s}$$

**d)** Med $m = 1200$ kg:

$$\Delta v = \frac{F \cdot \Delta t}{m} = \frac{1400\ \text{N} \cdot 200\ \text{s}}{1200\ \text{kg}} = 233\ \text{m/s}$$

Fejlen er ca. $4$ %. Brændstoffet udgør $8$ % af massen, så i en opgave skal du vurdere, om det er godt nok. Er brændstoffet under $1$ % af massen, kan du roligt bruge den simple metode.

</details>

## Det skal du kunne efter forløbet

- Forklare, hvorfor en raket kan accelerere i det tomme rum.
- Bruge $F = u \cdot \Delta m/\Delta t$ til at finde motorkraften.
- Opstille $m(t) \cdot a = F - m(t) \cdot g$ og forklare, hvorfor accelerationen vokser, når motorkraften er konstant.
- Udlede raketligningen $\Delta v = u \cdot \ln(m_0/m)$ og bruge den, også med leddet $g \cdot t$.
- Vurdere, om du må se bort fra massetabet.
- Diskutere modellens antagelser: konstant $u$, ingen luftmodstand, konstant $g$.
