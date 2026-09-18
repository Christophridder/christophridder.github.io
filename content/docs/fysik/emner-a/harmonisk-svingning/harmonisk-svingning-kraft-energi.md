---
title: "Harmonisk svingning – kraft og energi"
weight: 6
---

**Niveau: Fysik A** · **Emne: Mekanik – harmonisk svingning** · **Eksperiment: pendul**

Dette forløb **gentager ikke** Hookes lov (blok 1, kraftloven F = k · x) eller
dynamikken og dæmpningen fra det eksisterende svingningsmodul. Fokus her er at
binde **kraft- og energiforholdet** sammen og udvide med **det matematiske
pendul** som et andet harmonisk system. Dækker du allerede dele af det i dit
svingningsmodul, så klip det ud.

## Del 1 – Fra Hookes kraftlov til harmonisk svingning

I kender fjederkraften som F = k · x. Det afgørende er **fortegnet**: kraften
peger altid *modsat* udsvinget, tilbage mod ligevægt. Det kaldes en
**tilbagedrivende kraft**:

$$F = -k \cdot x$$

Sætter vi den ind i Newtons 2. lov, $F = m \cdot a$:

$$m \cdot a = -k \cdot x \quad\Longrightarrow\quad a = -\frac{k}{m} \cdot x$$

Accelerationen er proportional med udsvinget og modsat rettet – det er selve
**definitionen på en harmonisk svingning**. Løsningen er en cosinus-bevægelse
(den kender I fra svingningsmodulet):

$$x(t) = A \cdot \cos(\omega \cdot t + \varphi) \qquad \omega = \sqrt{\frac{k}{m}} \qquad T = 2\pi \cdot \sqrt{\frac{m}{k}}$$

hvor $A$ er amplituden og $\omega$ vinkelfrekvensen. **Pointen i denne blok:**
det er den tilbagedrivende kraft, der *skaber* svingningen – og den samme kraft
gemmer energi, som vi nu ser på.

## Del 2 – Energien i svingningen

Under svingningen veksler energien hele tiden mellem to former:

- **Potentiel energi i fjederen:** $E_{\text{pot}} = \tfrac{1}{2} \cdot k \cdot x^2$
- **Kinetisk energi:** $E_{\text{kin}} = \tfrac{1}{2} \cdot m \cdot v^2$

Uden tab er den **mekaniske energi bevaret**:

$$E_{\text{mek}} = E_{\text{pot}} + E_{\text{kin}} = \text{konstant}$$

To nøglepositioner gør regnestykket nemt:

| Position | $x$ | $v$ | Energien er ren |
|---|---|---|---|
| Yderpunkt (vendepunkt) | $\pm A$ | $0$ | potentiel: $E = \tfrac{1}{2} k A^2$ |
| Ligevægt (midten) | $0$ | $v_{\text{max}}$ | kinetisk: $E = \tfrac{1}{2} m v_{\text{max}}^2$ |

Da energien er den samme begge steder, fås en pæn sammenhæng:

$$\tfrac{1}{2} \cdot k \cdot A^2 = \tfrac{1}{2} \cdot m \cdot v_{\text{max}}^2 \quad\Longrightarrow\quad v_{\text{max}} = A \cdot \sqrt{\frac{k}{m}} = A \cdot \omega$$

> **Bemærk om energiens rytme:** $E_{\text{pot}}$ og $E_{\text{kin}}$ svinger med
> **dobbelt frekvens** af selve bevægelsen – på én hel svingning er bolden to
> gange i ligevægt og to gange i yderpunkt. Det er præcis det mønster, man ser i
> et $E$-$t$-diagram (jf. energiomsætning i en hoppende bold).

> **Regneeksempel:** Fjeder med $k = 20$ N/m, lod $m = 0{,}50$ kg, amplitude
> $A = 0{,}10$ m. Da er
> $T = 2\pi\sqrt{0{,}50/20} = 0{,}99$ s, den samlede energi
> $E = \tfrac{1}{2} \cdot 20 \cdot 0{,}10^2 = 0{,}10$ J, og
> $v_{\text{max}} = 0{,}10 \cdot \sqrt{20/0{,}50} = 0{,}63$ m/s. Tjek:
> $\tfrac{1}{2} \cdot 0{,}50 \cdot 0{,}63^2 = 0{,}10$ J. ✓

## Del 3 – Det matematiske pendul

Et lod i en snor er også et harmonisk system – for **små udsving**. Den
tilbagedrivende kraft langs banen er tyngdekraftens komposant:

$$F = -m \cdot g \cdot \sin\theta$$

For små vinkler gælder $\sin\theta \approx \theta$, og med buelængden
$s = L \cdot \theta$ bliver kraften $F \approx -\dfrac{m \cdot g}{L} \cdot s$ –
altså igen "kraft = konstant gange udsving, modsat rettet". Det giver en
harmonisk svingning med

$$T = 2\pi \cdot \sqrt{\frac{L}{g}}$$

To resultater, der overrasker eleverne:

1. **Svingningstiden afhænger ikke af loddets masse.** Tungt eller let lod –
   samme $T$.
2. **For små udsving afhænger $T$ heller ikke af amplituden.**

> **Model og gyldighed (A-niveau):** Hele resultatet hviler på $\sin\theta \approx
> \theta$. Ved store udsving holder approksimationen ikke, og svingningstiden
> vokser en smule med amplituden. Det er et fint eksempel på en models
> gyldighedsområde – og noget at lade eleverne undersøge eksperimentelt.

### Eksperiment: pendulets svingningstid

**Formål:** Undersøge hvilke variable der påvirker svingningstiden, og bestemme
$g$.

**Gennemførelse:**
- Mål $T$ for forskellige snorlængder $L$ (tag tid for fx 10 svingninger og
  divider – det mindsker aflæsningsfejlen).
- Hold $L$ fast og varier loddets masse → vis, at $T$ er uændret.
- Hold $L$ fast og varier amplituden → find, hvornår modellen begynder at svigte.

**Databehandling (Excel):**
- Plot $T^2$ mod $L$. Sammenhængen er lineær, fordi
  $T^2 = \dfrac{4\pi^2}{g} \cdot L$. Hældningen er $\dfrac{4\pi^2}{g}$ → bestem $g$
  og sammenlign med $9{,}82$ m/s².

> **Prøverelevant:** Svarer til Egaa-spørgsmål G. Hovedforsøget er
> fjedersvingningen med både kinematiske og energimæssige overvejelser;
> pendulet er den naturlige udvidelse ("hvis tiden tillader det").

## Opgaver

1. En fjeder med $k = 35$ N/m svinger med et lod på $0{,}80$ kg og amplitude
   $0{,}060$ m. Bestem svingningstiden, den maksimale fart og den samlede
   mekaniske energi.
2. I hvilken position er $E_{\text{pot}} = E_{\text{kin}}$? Udtryk udsvinget $x$
   ved amplituden $A$. (Hjælp: sæt de to energiudtryk lig hinanden.)
3. Et pendul har længden $0{,}80$ m. Bestem svingningstiden. Hvor lang skal
   snoren være, for at $T = 2{,}0$ s?
4. **Diskussion:** Forklar ud fra energibevarelse, hvorfor et reelt pendul
   alligevel langsomt mister amplitude – og hvad energien bliver til.

## Det skal I kunne efter forløbet

- Forklare, at en tilbagedrivende kraft $F = -k \cdot x$ giver en harmonisk svingning.
- Opstille energiregnskabet $E_{\text{mek}} = E_{\text{pot}} + E_{\text{kin}}$ og
  bruge bevarelsen til at finde fart, amplitude eller energi.
- Udlede og anvende $T = 2\pi\sqrt{L/g}$ for det matematiske pendul.
- Bestemme $g$ eksperimentelt og diskutere små-vinkel-modellens gyldighedsområde.
