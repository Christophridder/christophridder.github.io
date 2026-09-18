---
title: "Magnetisk felt"
weight: 10
---

**Niveau: Fysik A** · **Emne: Magnetiske felter** · **Eksperiment: strømvægt (Laplace)**

Forløbet behandler det magnetiske felt, kraften på en strømførende leder
(Laplace-kraften) og kraften på en bevægelig ladning. Emnet er svært, fordi
kræfterne står **vinkelret** på både strøm/fart og felt – derfor er
retningsbestemmelsen lige så vigtig som formlerne.

## De centrale formler

> **Kraft på en strømførende leder (Laplace):**
> $$F = B \cdot I \cdot L$$
> når strømmen står vinkelret på feltet ($F = B \cdot I \cdot L \cdot \sin\theta$ ellers).
>
> **Kraft på en bevægelig ladning:**
> $$F = q \cdot v \cdot B$$
> når farten står vinkelret på feltet. (En strøm *er* ladninger i bevægelse, så
> de to formler er samme fysik.)
>
> **Ladning i cirkelbane (magnetkraft = centripetalkraft):**
> $$q \cdot v \cdot B = \frac{m \cdot v^2}{r} \quad\Longrightarrow\quad r = \frac{m \cdot v}{q \cdot B}$$
>
> **Højrehåndsreglen (tre fingre, positiv ladning/strøm):**
> tommelfinger = strøm/fart, pegefinger = magnetfelt **B**, langefinger = kraft
> **F**. For en elektron vender kraften modsat.

Magnetfeltets styrke $B$ måles i **tesla (T)**. Jordens magnetfelt er omkring
$5 \cdot 10^{-5}$ T; en kraftig laboratoriemagnet kan give nogle få tesla.

## Del 1 – Magnetfeltet

Et magnetfelt omgiver permanente magneter og strømførende ledere. **Feltlinjerne**
løber uden for magneten fra nordpol mod sydpol og viser feltets retning. Mellem
polerne på en hesteskomagnet er feltet næsten **homogent** – lige stort og
ensrettet.

To ting, eleverne skal holde fast i:
- Feltet har en **retning** (det er en vektor).
- Magnetkraften virker kun på **bevægede** ladninger og på **strøm** – ikke på en
  ladning, der ligger stille.

## Del 2 – Kraften på en strømførende leder

En leder med strømmen $I$ og længden $L$ i et felt $B$ påvirkes af kraften

$$F = B \cdot I \cdot L$$

(når strøm og felt er vinkelrette). **Retningen** findes med højrehåndsreglen:
peg tommelfingeren langs strømmen, pegefingeren langs feltet – så peger
langefingeren langs kraften. Kraften står altså vinkelret på *både* strøm og felt.

> **Regneeksempel:** En leder på $L = 0{,}15$ m fører strømmen $I = 3{,}0$ A
> vinkelret på et felt $B = 0{,}40$ T. Kraften er
> $F = 0{,}40 \cdot 3{,}0 \cdot 0{,}15 = 0{,}18$ N.

Det er præcis denne kraft, der får en **elektromotor** til at dreje –  det skal vi bruge senere 
til emnet elbilens fysik.

## Del 3 – Bevægelig ladning og cirkelbevægelse

Da en strøm er ladninger i bevægelse, må en enkelt ladning $q$ med farten $v$
også mærke en kraft:

$$F = q \cdot v \cdot B$$

Det specielle: kraften står altid **vinkelret på farten**. En kraft vinkelret på
bevægelsen ændrer kun retningen, ikke farten – det er jo netop en
**centripetalkraft**. En ladning, der flyver vinkelret ind i et homogent felt,
løber derfor i en **cirkel**:

$$q \cdot v \cdot B = \frac{m \cdot v^2}{r} \quad\Longrightarrow\quad r = \frac{m \cdot v}{q \cdot B}$$

Her møder magnetfeltet cirkelbevægelsen fra mekanikken. Det er princippet bag
massespektrometre, og det er forklaringen på **nordlys**: ladede partikler fra
Solen fanges i Jordens magnetfelt og spiraler ned mod polerne.

## Del 4 – Eksperiment: strømvægt

**Formål:** Eftervise $F = B \cdot I \cdot L$ og bestemme feltstyrken $B$.

### Gennemførelse
- En strømførende leder anbringes vinkelret på feltet fra en magnet, der står på
  en følsom vægt.
- Vægtens udslag (kraften) måles for forskellige strømstyrker $I$ ved fast længde
  $L$.

### Databehandling (Excel)
- Plot $F$ mod $I$. Sammenhængen er lineær gennem $(0,0)$, fordi
  $F = (B \cdot L) \cdot I$. Hældningen er $B \cdot L$ → bestem $B$.
- Eventuelt gentages med forskellig effektiv længde $L$.

> **Prøverelevant:** Hold analysen i Excel. Forsøget er samtidig et flot forvarsel
> til elektromotoren i elbil-forløbet.

## Opgaver

1. En leder på $0{,}25$ m fører en strøm på $4{,}0$ A vinkelret på et homogent
   felt med $B = 0{,}30$ T. Bestem kraften på lederen, og angiv dens retning med
   højrehåndsreglen, hvis strømmen går mod højre og feltet ind i papiret.
2. En elektron flyver vinkelret ind i et felt $B = 0{,}020$ T med farten
   $v = 5{,}9 \cdot 10^{6}$ m/s (samme fart som efter $100$ V-accelerationen fra
   feltforløbet). Bestem radius i dens cirkelbane.
3. **Kombineret – ladet partikel i Jordens magnetfelt.** I Van Allen-bælterne
   omkring Jorden – samme rumområde, som satellitter passerer – fanges ladede
   partikler i Jordens magnetfelt. En proton bevæger sig vinkelret på et felt
   $B = 5{,}0 \cdot 10^{-5}$ T med farten $v = 1{,}0 \cdot 10^{6}$ m/s, og
   magnetkraften leverer centripetalkraften.
   - a) Vis, at banens radius er $r = \dfrac{m \cdot v}{q \cdot B}$, og beregn den.
   - b) Bestem omløbstiden $T$, og vis, at den er **uafhængig** af farten.
   - *Givet:* $m_{\text{proton}} = 1{,}67 \cdot 10^{-27}$ kg,
     $q = 1{,}602 \cdot 10^{-19}$ C.
4. **Diskussion:** Forklar ud fra $F = q v B$, hvorfor en magnetkraft aldrig kan
   ændre en ladnings fart (kun dens retning) – og hvad det betyder for partiklens
   kinetiske energi.

> **Facit:** Opg. 1: $F = 0{,}30 \cdot 4{,}0 \cdot 0{,}25 = 0{,}30$ N.
> Opg. 2: $r = \dfrac{9{,}11 \cdot 10^{-31} \cdot 5{,}9 \cdot 10^{6}}{1{,}602 \cdot 10^{-19} \cdot 0{,}020} \approx 1{,}7 \cdot 10^{-3}$ m (ca. 1,7 mm).
> Opg. 3: $r \approx 2{,}1 \cdot 10^{2}$ m, og $T = \dfrac{2\pi m}{qB} \approx 1{,}3 \cdot 10^{-3}$ s (uafhængig af $v$, da $v$ går ud).

## Det skal I kunne efter forløbet

- Beskrive et magnetfelt og dets retning, og kende enheden tesla.
- Bruge $F = B \cdot I \cdot L$ for en strømførende leder og finde retningen med
  højrehåndsreglen.
- Bruge $F = q \cdot v \cdot B$ for en bevægelig ladning.
- Forklare, at en ladning vinkelret på et felt løber i en cirkel, og bruge
  $r = m v / (q B)$.
- Bestemme $B$ eksperimentelt med strømvægten.
