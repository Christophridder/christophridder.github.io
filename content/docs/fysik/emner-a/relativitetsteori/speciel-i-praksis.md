---
title: "Speciel relativitet i praksis"
weight: 8
---

**Niveau: Fysik A (supplerende stof)** · **Emne: Speciel relativitet** · **1 modul**

På siden [Speciel relativitetsteori]({{< relref "speciel-relativitetsteori" >}}) så du, at ure i bevægelse går langsommere. Her regner du på to *rigtige* situationer, hvor man har målt det: atomure i rutefly og en astronaut, der boede et år på ISS.

## Formlerne

Begge formler indeholder den samme kvadratrod:

$$\Delta t = \frac{\Delta t_0}{\sqrt{1 - \dfrac{v^2}{c^2}}} \qquad\qquad L = L_0 \cdot \sqrt{1 - \frac{v^2}{c^2}}$$

- $\Delta t_0$ er tiden på uret, der bevæger sig (egentiden).
- $\Delta t$ er tiden, der går hos dem, der står stille.
- $L_0$ er længden målt af en, der følger med genstanden (hvilelængden).

### Når farten er lille: brug tilnærmelsen

Et fly flyver med ca. $250$ m/s. Så er $\dfrac{v^2}{c^2} \approx 7 \cdot 10^{-13}$, og $\sqrt{1 - 7 \cdot 10^{-13}}$ bliver $1$ på en lommeregner, fordi den ikke har decimaler nok. Derfor bruger vi denne tilnærmelse, der gælder, når $v$ er meget mindre end $c$:

$$\boxed{\ \Delta t - \Delta t_0 \approx \Delta t_0 \cdot \frac{1}{2} \cdot \frac{v^2}{c^2}\ }$$

Venstresiden $\Delta t - \Delta t_0 $ er, hvor meget uret i bevægelse **kommer bagud**.

<details>
<summary><strong>Hvorfor virker tilnærmelsen?</strong></summary>

**Problemet.** Hvor meget uret kommer bagud, er

$$\Delta t - \Delta t_0 = \Delta t_0 \cdot \left(\frac{1}{\sqrt{1 - \dfrac{v^2}{c^2}}} - 1\right)$$

I parentesen trækker vi to tal fra hinanden, som er *næsten ens*. Ved flyfarter er forskellen så lille, at lommeregneren ikke har cifre nok til at se den.

**Find mønsteret.** Regn selv parentesen ud på lommeregneren for nogle farter, hvor den stadig kan følge med:

| Fart $v$ | $\dfrac{v^2}{c^2}$ | $\dfrac{1}{\sqrt{1 - v^2/c^2}} - 1$ | $\dfrac{1}{2} \cdot \dfrac{v^2}{c^2}$ |
|---|---|---|---|
| $0{,}1\,c$ | $0{,}01$ | $0{,}00504$ | $0{,}005$ |
| $0{,}01\,c$ | $0{,}0001$ | $0{,}0000500$ | $0{,}00005$ |
| $0{,}001\,c$ | $0{,}000001$ | $0{,}000000500$ | $0{,}0000005$ |

- Når farten bliver $10$ gange mindre, bliver parentesen $100$ gange mindre.
- Parentesen er hele tiden (næsten præcis) **halvdelen af** $\dfrac{v^2}{c^2}$ – og jo mindre farten er, jo bedre passer det.

Et fly flyver under $0{,}000001\,c$, så her kan vi trygt erstatte parentesen med $\tfrac{1}{2} \cdot \dfrac{v^2}{c^2}$. Det er hele tilnærmelsen.

**Kort bevis (kun kvadratsætningen).** Kald $x = \dfrac{v^2}{c^2}$ og $s = \sqrt{1 - x}$, så $s^2 = 1 - x$. Gang tæller og nævner med $1 + s$, og brug $(1 - s)(1 + s) = 1 - s^2 = x$:

$$\frac{1}{s} - 1 = \frac{1 - s}{s} = \frac{(1 - s)(1 + s)}{s \cdot (1 + s)} = \frac{x}{s \cdot (1 + s)}$$

Det er **helt præcist**. Nu trækker vi ikke længere to næsten ens tal fra hinanden. Ved flyfarter er $s = 1$ (det viser lommeregneren selv), så nævneren er $1 \cdot (1 + 1) = 2$, og parentesen bliver $\dfrac{x}{2} = \dfrac{1}{2} \cdot \dfrac{v^2}{c^2}$.

</details>

Konstanter: $c = 3{,}00 \cdot 10^{8}$ m/s, $G = 6{,}674 \cdot 10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_\text{Jord} = 5{,}972 \cdot 10^{24}$ kg, $R_\text{Jord} = 6371$ km.

## Opgave 1: Atomure jorden rundt (1971)

<figure>
<svg viewBox="0 0 640 300" width="100%" style="max-width:640px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
<defs><marker id="pil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<circle cx="320" cy="150" r="125" fill="none" stroke="#999" stroke-dasharray="6 5"/>
<circle cx="320" cy="150" r="88" fill="#3d7cc9"/>
<path d="M285,95 q20,-15 40,0 t30,20 q-10,25 -35,15 t-35,-35 z M300,175 q25,-10 45,8 q5,20 -20,22 q-20,-5 -25,-30 z" fill="#5fa55a"/>
<text x="320" y="152" text-anchor="middle" fill="white" font-weight="bold">Jorden</text>
<path d="M260,232 A90,90 0 0 0 380,232" fill="none" stroke="white" stroke-width="2" marker-end="url(#pil)"/>
<text x="320" y="268" text-anchor="middle" fill="#333">Jorden drejer mod øst (set fra Nordpolen)</text>
<path d="M395,40 A125,125 0 0 1 440,75" fill="none" stroke="#1f6f43" stroke-width="3" marker-end="url(#pil)"/>
<text x="452" y="62" fill="#1f6f43" font-weight="bold">Vestgående fly</text>
<text x="452" y="80" fill="#1f6f43">uret vandt ca. 273 ns</text>
<path d="M245,40 A125,125 0 0 0 200,75" fill="none" stroke="#c0392b" stroke-width="3" marker-end="url(#pil)"/>
<text x="188" y="62" text-anchor="end" fill="#c0392b" font-weight="bold">Østgående fly</text>
<text x="188" y="80" text-anchor="end" fill="#c0392b">uret tabte ca. 59 ns</text>
<rect x="497" y="200" width="125" height="46" rx="6" fill="#f4f1ea" stroke="#999"/>
<text x="559" y="219" text-anchor="middle" fill="#333">Sammenlignet med</text>
<text x="559" y="237" text-anchor="middle" fill="#333">ure på jorden (USA)</text>
</svg>
<figcaption>Hafele og Keating fløj atomure jorden rundt med rutefly – én gang mod øst og én gang mod vest. 1 ns = 10⁻⁹ s.</figcaption>
</figure>

I oktober 1971 tog fysikeren **Joseph Hafele** og astronomen **Richard Keating** fire atomure med på almindelige rutefly jorden rundt. Bagefter sammenlignede de urene med atomure, der var blevet på jorden. Det var første gang, man målte tidsforlængelse med rigtige ure i et rigtigt fly.

Vi forenkler: Et fly flyver med $900$ km/h, og uret er i luften i $40$ timer.

**a)** Omregn flyets fart til m/s.

**b)** Beregn $\dfrac{v^2}{c^2}$.

**c)** Prøv at beregne $\sqrt{1 - \dfrac{v^2}{c^2}}$ på lommeregneren eller i Python. Hvad sker der?

**d)** Brug tilnærmelsen til at bestemme, hvor meget flyets ur kommer bagud på de $40$ timer. Angiv svaret i nanosekunder.

**e)** Det rigtige forsøg gav ca. $-59$ ns for det østgående fly og ca. $+273$ ns for det vestgående. Dit resultat fra d) har den rigtige *størrelsesorden*, men hvorfor kan de to fly give så forskellige resultater? *(Tænk på, at Jorden selv drejer.)*

## Opgave 2: Tvillingerne Kelly (2015–2016)

Astronauten **Scott Kelly** boede $340$ døgn på den internationale rumstation ISS, mens hans enæggede tvillingebror **Mark Kelly** var på Jorden. ISS kredser i ca. $408$ km's højde.

**a)** Bestem ISS' fart med $v = \sqrt{\dfrac{G \cdot M_\text{Jord}}{r}}$. Husk, at $r$ regnes fra Jordens centrum.

**b)** Bestem, hvor meget Scotts ur er kommet bagud efter $340$ døgn. Angiv svaret i millisekunder.

**c)** Hvem af tvillingerne er ældst, da Scott lander, og hvor meget?

**d)** Hvor længe skulle Scott blive på ISS for at blive ét helt sekund yngre end Mark?

## Modelgyldighed

- **Tilnærmelsen** $\Delta t - \Delta t_0 \approx \Delta t_0 \cdot \tfrac{1}{2} v^2/c^2$ er meget præcis, når $v$ er langt mindre end $c$. Ved $v = 0{,}1\,c$ er fejlen under $1$ %.
- **Speciel relativitet** gælder i systemer, der bevæger sig med konstant fart. Jorden drejer, og ISS bevæger sig i en cirkel, så vi forenkler.
- **Tyngdekraften** er helt udeladt. Ure højt oppe går faktisk *hurtigere* – det er den **almene** relativitetsteori. Den regner du på i [Almen relativitet i praksis]({{< relref "almen-i-praksis" >}}).

## Hints og løsninger

<details>
<summary><strong>Hints</strong></summary>

**1a)** Divider med $3{,}6$.

**1c)** Prøv at skrive tallet med alle decimaler. Hvor mange cifre har din lommeregner?

**1d)** $\Delta t_0 = 40$ timer i sekunder. $1\ \text{ns} = 10^{-9}$ s.

**1e)** Set ude fra rummet bevæger jordoverfladen sig mod øst med ca. $465$ m/s ved ækvator. Hvilket fly bevæger sig så hurtigst set ude fra rummet – og hvad med urene på jorden?

**2a)** $r = 6371\ \text{km} + 408\ \text{km}$. Husk at regne i meter.

**2b)** $340$ døgn $= 340 \cdot 86\,400$ s.

**2d)** Hvor meget kommer uret bagud *pr. sekund*? Det er $\tfrac{1}{2} \cdot v^2/c^2$.

</details>

<details>
<summary><strong>Løsninger</strong></summary>

**1a)** $v = \dfrac{900}{3{,}6}\ \mathrm{m/s} = 250\ \mathrm{m/s}$

**1b)** $\dfrac{v^2}{c^2} = \dfrac{(250\ \mathrm{m/s})^2}{(3{,}00 \cdot 10^{8}\ \mathrm{m/s})^2} = 6{,}94 \cdot 10^{-13}$

**1c)** Lommeregneren giver $1$ (eller $0{,}9999999999997$, hvis den har mange cifre). Forskellen fra $1$ forsvinder i afrundingen. Derfor bruger vi tilnærmelsen.

**1d)** $\Delta t_0 = 40 \cdot 3600\ \mathrm{s} = 144\,000\ \mathrm{s}$

$$\Delta t - \Delta t_0 \approx 144\,000\ \mathrm{s} \cdot \frac{1}{2} \cdot 6{,}94 \cdot 10^{-13} = 5{,}0 \cdot 10^{-8}\ \mathrm{s} = 50\ \mathrm{ns}$$

Flyets ur kommer altså $50$ milliardtedele af et sekund bagud.

**1e)** Formlen gælder for ure, der bevæger sig i forhold til et system, der *ikke* drejer. Set ude fra rummet bevæger urene på jorden sig også (mod øst). Det østgående fly har *større* fart end jordurene og går derfor langsommere end dem (tab). Det vestgående fly flyver imod Jordens rotation, har *mindre* fart end jordurene og går derfor hurtigere (gevinst). Desuden går alle flyurene lidt hurtigere, fordi de er højt oppe – det er almen relativitet (næste side).

**2a)** $r = 6{,}779 \cdot 10^{6}$ m

$$v = \sqrt{\frac{6{,}674 \cdot 10^{-11} \cdot 5{,}972 \cdot 10^{24}}{6{,}779 \cdot 10^{6}}}\ \mathrm{m/s} = 7668\ \mathrm{m/s} \approx 7{,}67\ \mathrm{km/s}$$

**2b)** $\Delta t_0 = 340 \cdot 86\,400\ \mathrm{s} = 2{,}94 \cdot 10^{7}\ \mathrm{s}$ og $\tfrac{1}{2} \cdot \dfrac{v^2}{c^2} = \tfrac{1}{2} \cdot \dfrac{7668^2}{(3{,}00 \cdot 10^{8})^2} = 3{,}27 \cdot 10^{-10}$

$$\Delta t - \Delta t_0 \approx 2{,}94 \cdot 10^{7}\ \mathrm{s} \cdot 3{,}27 \cdot 10^{-10} = 9{,}6 \cdot 10^{-3}\ \mathrm{s} = 9{,}6\ \mathrm{ms}$$

**2c)** Scotts ur er kommet bagud, så **Scott er blevet ca. $0{,}01$ s yngre** end Mark – Mark er nu den ældste. (Tyngdeeffekten trækker lidt fra, se næste side.)

**2d)** Uret taber $3{,}27 \cdot 10^{-10}$ s pr. sekund. For at tabe $1$ s:

$$t = \frac{1\ \mathrm{s}}{3{,}27 \cdot 10^{-10}} = 3{,}06 \cdot 10^{9}\ \mathrm{s} \approx 97\ \text{år}$$

</details>
