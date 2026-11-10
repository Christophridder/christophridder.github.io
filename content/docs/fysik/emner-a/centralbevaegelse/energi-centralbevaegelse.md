---
title: "Energi i centralbevægelse"
weight: 4
pdf: "pdfs/energi-centralbevaegelse.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Centralbevægelse – energi i tyngdefeltet**

Nær jordoverfladen bruger du $E_{\text{pot}} = m \cdot g \cdot h$. Men $g$ er ikke
konstant, når du kommer langt væk (se [Newtons gravitationslov]({{< relref "gravitationsloven" >}})).
Her finder du det rigtige udtryk og bruger det på satellitter, undvigelseshastighed
og banetyper. Slå *Energi* til i simuleringen på siden om
[Keplers love]({{< relref "keplers-love" >}}), mens du læser.

## Del 1 – Potentiel energi langt fra Jorden

Vi vælger **nulpunktet i det uendelige**: langt væk fra Jorden er $E_{\text{pot}} = 0$.

### Hvorfor et integral?

Ved $m \cdot g \cdot h$ er kraften konstant, så arbejdet er bare kraft gange vej. Her aftager kraften med afstanden: Kommer du dobbelt så langt væk, er den kun en fjerdedel så stor. Derfor deler du vejen op i små stykker $\mathrm{d}r$. På hvert lille stykke er kraften næsten konstant, og arbejdet er $\mathrm{d}A = F \cdot \mathrm{d}r$. Integralet lægger alle de små arbejder sammen – det er arealet under grafen for $F(r)$.

### Trin 1 – Træk legemet helt væk

Forestil dig, at du trækker legemet langsomt ud fra afstanden $r_0$ og helt ud i det uendelige. Du trækker med en kraft, der er lige så stor som tyngdekraften, $F = G \cdot \dfrac{M \cdot m}{r^2}$, så farten ikke ændrer sig undervejs.

Du starter i $r_0$ og slutter i det uendelige. **Den nederste grænse er der, hvor du starter, og den øverste er der, hvor du slutter:** 

$$A = \int_{r_0}^{\infty} G \cdot \frac{M \cdot m}{r^2}\,\mathrm{d}r$$

$G$, $M$ og $m$ er konstanter og kan sættes uden for integralet. En stamfunktion til $\dfrac{1}{r^2} = r^{-2}$ er $-\dfrac{1}{r}$:

$$A = G M m \left[-\frac{1}{r}\right]_{r_0}^{\infty} = G M m \left( \underbrace{-\frac{1}{\infty}}_{=\,0} - \left(-\frac{1}{r_0}\right) \right) = \frac{G \cdot M \cdot m}{r_0}$$

Arbejdet er **positivt**: Du skal tilføre energi for at få legemet væk fra Jorden.

### Trin 2 – Fra arbejde til potentiel energi

Dit arbejde bliver til potentiel energi. Den potentielle energi stiger altså med $A$ på vejen ud:

$$E_{\text{pot}}(\infty) - E_{\text{pot}}(r_0) = \frac{G \cdot M \cdot m}{r_0}$$

Vi har valgt $E_{\text{pot}}(\infty) = 0$, så $0 - E_{\text{pot}}(r_0) = \dfrac{GMm}{r_0}$. Fra nu af skriver vi bare $r$ for afstanden:

$$E_{\text{pot}} = -\frac{G \cdot M \cdot m}{r}$$

**Minus betyder "under nulpunktet".** Det er ligesom en kælder: Sætter du nulpunktet ved gadeniveau, har en kasse i kælderen negativ potentiel energi, og du skal tilføre energi for at få den op til $0$. Her ligger nulpunktet uendeligt langt væk, så alle steder nær Jorden ligger "i kælderen".

- $E_{\text{pot}}$ er **negativ** overalt og stiger mod $0$, når du kommer længere væk.
- Tættere på Jorden betyder **lavere** (mere negativ) potentiel energi – præcis som ved $mgh$.

### Hvilke grænser skal integralet have?

| Integral | Hvad det betyder | Resultat |
|---|---|---|
| $\displaystyle\int_{r_0}^{\infty} \frac{GMm}{r^2}\,\mathrm{d}r$ | Dit arbejde, når du trækker legemet **ud** fra $r_0$ | $+\dfrac{GMm}{r_0}$ |
| $\displaystyle\int_{\infty}^{r_0} \frac{GMm}{r^2}\,\mathrm{d}r$ | Dit arbejde, når legemet glider **ind** til $r_0$, og du holder igen. Bytter du grænserne, skifter fortegnet | $-\dfrac{GMm}{r_0}$ |
| $\displaystyle\int_{0}^{r_0} \frac{GMm}{r^2}\,\mathrm{d}r$ | Giver ikke mening: $\tfrac{1}{0}$ er uendelig, og inde i Jorden gælder loven ikke, fordi kun massen inden for $r$ trækker | – |

Nulpunktet kan altså ikke ligge i $r = 0$. Det uendelige er det naturlige valg, fordi kraften er $0$ dér.

> **Helt formelt:** Potentiel energi er defineret ved $\Delta E_{\text{pot}} = -A_{\text{tyngde}}$. Lægger du en $r$-akse udad fra Jordens centrum, peger tyngdekraften den modsatte vej, så $F_r = -\dfrac{GMm}{r^2}$. Det giver
> $$E_{\text{pot}}(r) - E_{\text{pot}}(\infty) = -\int_{\infty}^{r} F_r\,\mathrm{d}r' = \int_{\infty}^{r} \frac{GMm}{r'^2}\,\mathrm{d}r' = GMm\left[-\frac{1}{r'}\right]_{\infty}^{r} = -\frac{GMm}{r}$$
> Her kommer minus'et af sig selv, fordi tyngdekraften peger ind, mens aksen peger ud.

### Sammenhæng med $m \cdot g \cdot h$

Løft en masse fra jordoverfladen ($r = R$) til højden $h$:

$$\Delta E_{\text{pot}} = GMm\left(\frac{1}{R} - \frac{1}{R + h}\right) = GMm \cdot \frac{h}{R \cdot (R + h)}$$

Når $h \ll R$, er $R + h \approx R$, og så er $\Delta E_{\text{pot}} \approx \dfrac{GM}{R^2} \cdot m \cdot h = m \cdot g \cdot h$.

> **Model:** $m \cdot g \cdot h$ er en tilnærmelse, der kun gælder, når højden er lille
> i forhold til Jordens radius. Løfter du $1000$ kg op til ISS ($408$ km), giver
> $mgh$ $4{,}0 \cdot 10^{9}$ J, men det præcise udtryk giver $3{,}8 \cdot 10^{9}$ J.
> Fejlen er $6{,}5$ %, fordi $g$ aftager undervejs.

### Undvigelseshastighed

Hvor stor fart skal et legeme have ved jordoverfladen for at slippe helt væk fra Jorden? Det kaldes **undvigelseshastigheden** $v_{\text{undv}}$. Vi regner uden luftmodstand og bruger energibevarelse: $E_{\text{kin}} + E_{\text{pot}}$ er den samme hele vejen.

| Sted | $E_{\text{kin}}$ | $E_{\text{pot}}$ |
|---|---|---|
| Ved jordoverfladen ($r = R$) | $\tfrac{1}{2} m v_{\text{undv}}^2$ | $-\dfrac{GMm}{R}$ |
| Uendeligt langt væk | $0$ | $0$ |

Vi leder efter den mindste fart, der lige akkurat rækker. Så når legemet det uendelige med farten $0$, og den samlede energi er $0$ begge steder:

$$\tfrac{1}{2} \cdot m \cdot v_{\text{undv}}^2 - \frac{G \cdot M \cdot m}{R} = 0$$

Massen $m$ går ud, så en kugle og en rumfærge skal have samme fart. Vi isolerer farten:

$$v_{\text{undv}} = \sqrt{\frac{2 \cdot G \cdot M}{R}}$$

Med tal for Jorden:

$$v_{\text{undv}} = \sqrt{\frac{2 \cdot 6{,}67 \cdot 10^{-11}\ \text{N·m}^2/\text{kg}^2 \cdot 5{,}97 \cdot 10^{24}\ \text{kg}}{6{,}37 \cdot 10^{6}\ \text{m}}} = 1{,}12 \cdot 10^{4}\ \text{m/s} = 11{,}2\ \text{km/s}$$

**Tjek med energien for 1 kg:** Legemet skal bruge $GM/R = 62{,}5$ MJ for at komme op af brønden. Med en decimal mere er farten $11{,}18$ km/s, og den giver netop $\tfrac{1}{2} \cdot 1\ \text{kg} \cdot (11{,}18\ \text{km/s})^2 = 62{,}5$ MJ.

> **Model:** Beregningen ignorerer luftmodstand og Jordens rotation, og den antager, at legemet får hele farten på én gang. En raket behøver ikke at nå $11{,}2$ km/s ved overfladen. Den fortsætter med at accelerere undervejs, og længere ude er undvigelseshastigheden mindre.

### Tyngdebrønden

Tegner du $E_{\text{pot}}$ som funktion af $r$, ser det ud som en brønd med Jorden i bunden. Du starter dybt nede, og kurven flader ud mod $0$ langt væk. Derfor kaldes den en **tyngdebrønd**. Undvigelseshastigheden er den fart, der lige akkurat bringer dig op over kanten.

{{< sim tyngdebroend.html 900 >}}

Rummet øverst og kurven nederst har samme $r$-akse, så prikkerne står lige over hinanden. Alle energier gælder for $1$ kg.

| I animationen | Betydning |
|---|---|
| Blå kurve | Den potentielle energi $E_{\text{pot}} = -GMm/r$ |
| Hvid linje | Nulpunktet, som svarer til uendeligt langt væk |
| Gul linje | Den mekaniske energi $E_{\text{mek}} = E_{\text{kin}} + E_{\text{pot}}$. Den er konstant |
| Grøn pil | Den kinetiske energi: afstanden fra kurven op til den gule linje |

**Undersøg selv**

1. **Træk selv.** Tryk på *Træk selv*, og træk legemet ud fra Jorden. Hvorfor koster det første stykke meget mere energi end det sidste?
2. **Hele vejen ud.** Hvor meget energi koster det at få $1$ kg helt væk fra Jorden? Find tallet på kurven.
3. **$m \cdot g \cdot h$.** Slå modellen til. Hvor på kurven passer den, og hvornår bliver den for stor? Forklar sammenhængen med afsnittet ovenfor.
4. **Vendepunktet.** Affyr med $7{,}9$ km/s. Hvor vender legemet? Hvor er den grønne pil henne dér?
5. **Undslip.** Prøv $10$ km/s og $11{,}2$ km/s. Hvad sker der med den gule linje? Forklar med tegnet på $E_{\text{mek}}$, hvorfor legemet ikke kommer tilbage ved $11{,}2$ km/s.
6. **Mere end nok.** Affyr med $13$ km/s. Hvor stor fart har legemet langt væk? Hvor kan du aflæse dens energi i diagrammet?

> **Model:** Legemet skydes lodret op uden luftmodstand, og Jordens rotation er ignoreret. Brønden viser energi, ikke form: Rummet er ikke krummet som en tragt, og legemet ruller ikke på kurven.

## Del 2 – Energi i en cirkulær bane

Her viser du to sammenhænge, der gælder for alle cirkulære baner:

$$E_{\text{kin}} = -\tfrac{1}{2} \cdot E_{\text{pot}} \qquad\qquad E_{\text{mek}} = -E_{\text{kin}} = \tfrac{1}{2} \cdot E_{\text{pot}}$$

### Trin 1 – Start i kraftligningen

I en cirkulær bane er tyngdekraften netop den kraft, der holder legemet i cirklen. Centripetalkraften og tyngdekraften er lige store (se [gravitationsloven]({{< relref "gravitationsloven" >}})):

$$\frac{m \cdot v^2}{r} = \frac{G \cdot M \cdot m}{r^2}$$

### Trin 2 – Gang med $\tfrac{r}{2}$

Venstre side ligner næsten $E_{\text{kin}} = \tfrac{1}{2} m v^2$. Gang begge sider med $\tfrac{r}{2}$:

$$\tfrac{1}{2} \cdot m \cdot v^2 = \tfrac{1}{2} \cdot \frac{G \cdot M \cdot m}{r} \qquad\Longrightarrow\qquad E_{\text{kin}} = \frac{G \cdot M \cdot m}{2r}$$

### Trin 3 – Sammenlign med den potentielle energi

Begge energier indeholder brøken $\dfrac{GMm}{r}$. Mål dem i den:

| Energi | Udtryk | I enheder af $\dfrac{GMm}{r}$ |
|---|---|---|
| $E_{\text{pot}}$ | $-\dfrac{GMm}{r}$ | $-1$ |
| $E_{\text{kin}}$ | $+\dfrac{GMm}{2r}$ | $+\tfrac{1}{2}$ |
| $E_{\text{mek}} = E_{\text{kin}} + E_{\text{pot}}$ | $-\dfrac{GMm}{2r}$ | $-\tfrac{1}{2}$ |

Nu kan du læse sammenhængene direkte i sidste søjle:

- $E_{\text{kin}}$ er halvt så stor som $E_{\text{pot}}$ og har modsat fortegn: $E_{\text{kin}} = -\tfrac{1}{2} E_{\text{pot}}$.
- $E_{\text{mek}}$ er lige så stor som $E_{\text{kin}}$ og har modsat fortegn: $E_{\text{mek}} = -E_{\text{kin}}$.

**Med tal for ISS** ($r = 6{,}78 \cdot 10^{6}$ m) pr. kg: $E_{\text{pot}} = -58{,}7$ MJ, $E_{\text{kin}} = 29{,}4$ MJ og $E_{\text{mek}} = -29{,}4$ MJ.

### Hvorfor minus i energien, men ikke i kraftligningen?

Det er to forskellige slags størrelser:

| | Kraftligningen | Energien |
|---|---|---|
| Hvad er det? | Størrelsen (længden) af to vektorer | Et tal, der måles fra et nulpunkt, du selv har valgt |
| Fortegn | Begge sider er positive. Retningen – ind mod centrum – står i ord, ikke i fortegnet | Negativt, fordi nulpunktet ligger i det uendelige, og legemet er "under" det |
| Hvis du flytter nulpunktet | Ændrer sig ikke | Ændrer sig, men forskelle i energi gør ikke |

Kraften hænger sammen med **hældningen** på grafen for $E_{\text{pot}}$, ikke med dens værdi. Differentierer du $E_{\text{pot}} = -\dfrac{GMm}{r}$, får du $\dfrac{GMm}{r^2}$ – præcis tyngdekraftens størrelse. Kraften peger mod lavere energi, altså ind mod Jorden.

Minus'et i $E_{\text{kin}} = -\tfrac{1}{2}E_{\text{pot}}$ er der kun, fordi $E_{\text{pot}}$ er negativ, mens $E_{\text{kin}}$ altid er positiv. Det vender fortegnet, så begge sider bliver positive.

### Hvad betyder det?

- **Bunden bane.** $E_{\text{mek}} < 0$, så satellitten kan ikke nå det uendelige, hvor den samlede energi mindst skal være $0$.
- **Energi for at slippe væk.** Satellitten mangler $|E_{\text{mek}}| = E_{\text{kin}}$. Den skal altså have **fordoblet** sin kinetiske energi, og det kræver $\sqrt{2}$ gange så stor fart. Det er $v_{\text{undv}} = \sqrt{2} \cdot v_{\text{bane}}$ fra Del 4.
- **Lavere bane.** Flytter satellitten så meget ned, at $E_{\text{pot}}$ falder med $2$ enheder, så stiger $E_{\text{kin}}$ med $1$ enhed, og $E_{\text{mek}}$ falder med $1$ enhed. Halvdelen af den tabte potentielle energi bliver til fart. Den anden halvdel skal fjernes, fx af luftmodstanden som varme.

> **Paradokset med ISS:** Luftmodstanden i den tynde atmosfære tager energi fra
> ISS. Så falder $E_{\text{mek}}$, og stationen kommer længere ned – hvor den
> bevæger sig **hurtigere**. Luftmodstanden gør altså rumstationen hurtigere!
> Den taber hele tiden lidt højde og skal derfor løbende løftes med raketmotorer.

> **Model:** Sammenhængene gælder for en cirkulær bane, hvor kun tyngdekraften virker, og hvor centrallegemet er så tungt, at det står stille ($M \gg m$). Legemerne regnes som punkter eller kugler. I en ellipsebane gælder $E_{\text{kin}} = -\tfrac{1}{2}E_{\text{pot}}$ kun som gennemsnit over et helt omløb.

## Del 3 – Energi i en ellipsebane

I en ellipse skifter afstanden hele tiden. Men tyngdekraften er en
**bevarende kraft**, så den mekaniske energi er konstant:

- Tæt på Jorden: lav $E_{\text{pot}}$, stor $E_{\text{kin}}$ (høj fart).
- Langt væk: høj $E_{\text{pot}}$, lille $E_{\text{kin}}$ (lav fart).

Man kan vise, at den mekaniske energi kun afhænger af den store halvakse:

$$E_{\text{mek}} = -\frac{G \cdot M \cdot m}{2a}$$

Sætter du det lig $\tfrac{1}{2}mv^2 - \dfrac{GMm}{r}$, får du farten overalt i banen:

$$v^2 = G \cdot M \cdot \left(\frac{2}{r} - \frac{1}{a}\right)$$

For en cirkel ($r = a$) giver det igen $v^2 = GM/r$.

## Del 4 – Banetyper

I Del 1 fandt du undvigelseshastigheden ved jordoverfladen. Det samme gælder i enhver afstand $r$: Et legeme kommer kun helt væk, hvis $E_{\text{mek}} \geq 0$.

$$\tfrac{1}{2} m v^2 - \frac{G M m}{r} \geq 0 \quad\Longrightarrow\quad v \geq v_{\text{undv}} = \sqrt{\frac{2 \cdot G \cdot M}{r}}$$

Sammenlign med farten i en cirkulær bane, $v_{\text{bane}} = \sqrt{GM/r}$ fra Del 2:

$$v_{\text{undv}} = \sqrt{2} \cdot v_{\text{bane}}$$

Lige over jordoverfladen er $v_{\text{bane}} = 7{,}9$ km/s og $v_{\text{undv}} = 11{,}2$ km/s. Fra ISS-banen skal satellitten kun op fra $7{,}7$ km/s til $10{,}8$ km/s.

Fortegnet på $E_{\text{mek}}$ bestemmer banetypen:

| $E_{\text{mek}}$ | Banetype | Eksempel |
|---|---|---|
| $< 0$ | Ellipse (cirkel som specialtilfælde) – bunden | Månen, satellitter, planeter |
| $= 0$ | Parabel – undslipper lige akkurat | Grænsetilfælde |
| $> 0$ | Hyperbel – undslipper | Rumsonder på vej ud af solsystemet |

## Opgaver

*Brug* $G = 6{,}67 \cdot 10^{-11}$ N·m²/kg², $M_{\text{Jord}} = 5{,}97 \cdot 10^{24}$ kg,
$R_{\text{Jord}} = 6{,}37 \cdot 10^{6}$ m.

1. **Energi pr. kg.** Bestem den potentielle, kinetiske og samlede mekaniske energi
   pr. kg for en satellit i en cirkulær bane i højden $350$ km. Kommentér fortegnet
   på den samlede energi.
2. **Fra ISS til geostationær bane.** En satellit på $1000$ kg flyttes fra ISS-banen
   ($r = 6{,}78 \cdot 10^{6}$ m) til den geostationære bane ($r = 4{,}22 \cdot 10^{7}$ m).
   Hvor meget skal den mekaniske energi øges?
3. **$mgh$ eller ej?** Beregn arbejdet for at løfte $1000$ kg fra jordoverfladen op i
   højden $408$ km, både med $m \cdot g \cdot h$ og med $-GMm/r$. Hvor stor er
   fejlen i procent? Hvornår er $mgh$ en god model?
4. **Undvigelse fra Månen.** Månen har massen $7{,}35 \cdot 10^{22}$ kg og radius
   $1{,}74 \cdot 10^{6}$ m. Bestem undvigelseshastigheden fra Månens overflade, og
   sammenlign med Jordens.
5. **Luftmodstand gør hurtigere.** Forklar med energi, hvorfor ISS bevæger sig
   *hurtigere*, når luftmodstanden bremser den.
6. **Simuleringen.** Vælg *Geostationær*, ellipsefaktor $0{,}6$, og slå *Energi* til.
   Beskriv, hvordan $E_{\text{kin}}$, $E_{\text{pot}}$ og $E_{\text{mek}}$ ændrer sig rundt i banen.

## Facit

| Opgave | Facit |
|---|---|
| 1 | $E_{\text{pot}} = -5{,}93 \cdot 10^{7}$ J/kg, $E_{\text{kin}} = 2{,}96 \cdot 10^{7}$ J/kg, $E_{\text{mek}} = -2{,}96 \cdot 10^{7}$ J/kg. Negativ: bunden bane |
| 2 | $\Delta E_{\text{mek}} = 2{,}5 \cdot 10^{10}$ J |
| 3 | $mgh$: $4{,}0 \cdot 10^{9}$ J. Præcist: $3{,}8 \cdot 10^{9}$ J. Fejl $6{,}5$ %. God når $h \ll R$ |
| 4 | Månen: $2{,}4$ km/s. Jorden: $11{,}2$ km/s |
| 5 | $E_{\text{mek}} = -GMm/(2r)$ falder → $r$ bliver mindre → $E_{\text{kin}} = GMm/(2r)$ bliver større |
| 6 | $E_{\text{kin}}$ og $E_{\text{pot}}$ bytter energi. $E_{\text{mek}}$ er konstant og negativ |

## Det skal du kunne efter forløbet

- Bruge $E_{\text{pot}} = -GMm/r$ med nulpunkt i det uendelige og forklare fortegnet.
- Vise, at $mgh$ er en tilnærmelse for $h \ll R$, og vurdere hvornår den holder.
- Opstille integralet for $E_{\text{pot}}$ med de rigtige grænser og forklare, hvorfor der er minus foran.
- Udlede $E_{\text{kin}} = -\tfrac{1}{2}E_{\text{pot}}$ og $E_{\text{mek}} = -E_{\text{kin}} = -GMm/(2r)$ for en cirkulær bane.
- Bestemme undvigelseshastigheden og forbinde fortegnet på $E_{\text{mek}}$ med banetypen.
