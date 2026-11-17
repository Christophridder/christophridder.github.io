---
title: "Speciel relativitetsteori"
weight: 7
---

**Niveau: Fysik A (supplerende stof)** · **Emne: Speciel relativitet** · **3 moduler**

Et af fysikkens mærkeligste og sjoveste hjørner: tiden går forskelligt for folk i
bevægelse, afstande skrumper, og man kan faktisk rejse ind i fremtiden. Vi holder
det simpelt – to formler, et paradoks og et rigtigt eksperiment med myoner fra
rummet.

## To simple postulater – og alt det mærkelige følger

Einstein byggede hele teorien på bare to antagelser:

1. **Relativitetsprincippet:** Fysikkens love er de samme i alle systemer, der
   bevæger sig med konstant fart. Der findes ikke et "rigtigt stillestående" sted
   i universet.
2. **Lysets fart er konstant:** Alle måler lysets fart til $c = 3{,}00 \cdot 10^{8}$
   m/s – uanset hvor hurtigt de selv bevæger sig, og uanset hvordan lyskilden
   bevæger sig.

Det andet postulat er det vilde. Hvis lyset altid har samme fart for alle, må
**tid og længde** give efter i stedet. Det er det, formlerne fanger.

Begge formler indeholder den samme kvadratrod:

$$\sqrt{1 - \frac{v^2}{c^2}}$$

Den er altid mellem $0$ og $1$. Ved hverdagsfarter er $v^2/c^2$ næsten $0$, så
kvadratroden er næsten $1$, og intet mærkeligt sker. Når $v$ nærmer sig $c$,
bliver kvadratroden lille.

## Del 1 – Tidsforlængelse: bevægede ure går langsommere

Et ur, der bevæger sig forbi dig, tikker **langsommere**, end dit eget gør:

$$\Delta t = \frac{\Delta t_0}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

Her er $\Delta t_0$ **egentiden** – tiden målt i det system, hvor uret er i hvile
(urets "egen" tid). $\Delta t$ er den længere tid, du måler udefra. Du dividerer
med et tal mindre end $1$, så $\Delta t$ bliver større end $\Delta t_0$.

> **Eksempel:** Et rumskib flyver med $v = 0{,}80c$. Om bord går der
> $\Delta t_0 = 5{,}0$ år. Kvadratroden er $\sqrt{1 - 0{,}80^2} = \sqrt{0{,}36} = 0{,}60$.
> På Jorden går der $\Delta t = \dfrac{5{,}0\ \text{år}}{0{,}60} = 8{,}3$ år. Rejsende ældes 5 år,
> Jorden 8,3 år. **At rejse hurtigt er at rejse ind i fremtiden.**

## Del 2 – Længdekontraktion: bevægede genstande forkortes

En genstand i bevægelse er **kortere** i bevægelsesretningen, end når den er i
hvile:

$$L = L_0 \cdot \sqrt{1 - \frac{v^2}{c^2}}$$

$L_0$ er **hvilelængden** – længden målt, når genstanden er i hvile.

> **Læg mærke til modsætningen:** Tiden bliver **længere**, fordi du **dividerer**
> med kvadratroden. Længden bliver **kortere**, fordi du **ganger** med den.

> **Eksempel:** Et $100$ m langt rumskib ($L_0 = 100$ m) flyver forbi med
> $0{,}80c$. En observatør i hvile måler det til $L = 100\ \text{m} \cdot 0{,}60 = 60$ m.

## Del 3 – Tvillingeparadokset og tidsrejser

Forestil dig to tvillinger. Den ene bliver hjemme; den anden flyver afsted med
næsten lysets fart til en fjern stjerne og vender tilbage. Når de mødes igen, er
**den rejsende tvilling yngre**.

"Men vent" – siger eleverne – "bevægelse er da relativ? Set fra raketten er det
jo Jorden, der farer afsted!" Det er pointen i *paradokset*. Opløsningen er, at
situationen **ikke er symmetrisk**: den rejsende tvilling skal bremse op, vende om
og accelerere tilbage. Det er den rejsende, der skifter system – og derfor er det
entydigt den rejsende, der ældes mindst.

> **Tidsrejser, kort fortalt:** Ind i fremtiden? **Ja** – flyv hurtigt nok, og du
> springer fremad i tid i forhold til alle andre. Tilbage til fortiden? **Nej** –
> det tillader den specielle relativitetsteori ikke.

## Simulering: rejsen til Proxima Centauri

Den nærmeste stjerne efter Solen er Proxima Centauri, $4{,}25$ lysår væk. Vælg et
rumskib, og se, hvor lang tid rejsen tager. Den blå kurve er tiden målt på Jorden,
$t = d/v$. Den orange kurve er tiden om bord, $t_0 = t \cdot \sqrt{1 - v^2/c^2}$.

{{< sim proxima.html 640 >}}

**Undersøg selv**

1. **Vores hurtigste.** Vælg Voyager 2, Helios 2 og Parker Solar Probe. Hvor mange
   år tager rejsen? Kan du se forskel på den blå og den orange værdi?
2. **Et menneskeliv.** Hvor hurtigt skal rumskibet mindst flyve, for at rejsen
   tager under $80$ år? Er det relativitet, der gør det muligt?
3. **Avatar.** I filmen *Avatar* flyver rumskibet *Venture Star* med $0{,}7c$.
   Hvor lang tid går der om bord og på Jorden? Hvor mange år yngre er
   passagererne, når de lander, end deres tvilling derhjemme?
4. **Zoom ind.** Tryk på *Zoom*, og skru farten op mod $c$. Hvad sker der med de
   to kurver? Hvorfor kan tiden om bord blive kortere end $4{,}25$ år, selvom
   intet kan flyve hurtigere end lyset?

<details>
<summary><strong>Se svar</strong></summary>

1. Voyager 2: ca. $83\,000$ år. Helios 2: ca. $18\,000$ år. Parker Solar Probe:
   ca. $6600$ år. Tiden om bord er den samme med alle viste cifre – relativitet
   betyder intet ved de farter.
2. Farten skal mindst være $4{,}25/80 = 0{,}053c$, altså ca. $16\,000$ km/s. Det er
   ca. $80$ gange hurtigere end Parker Solar Probe. Ved $0{,}053c$ er kvadratroden
   $0{,}9986$, så relativitet sparer kun ca. en måned. Det er farten, der er
   problemet, ikke tiden.
3. På Jorden: $6{,}1$ år. Om bord: $6{,}1 \cdot \sqrt{1 - 0{,}7^2} = 4{,}3$ år.
   Passagererne er ca. $1{,}7$ år yngre end tvillingen. I filmen er rejsen lidt
   længere, fordi Pandora ligger ved Alpha Centauri A ($4{,}37$ lysår), og skibet
   bruger tid på at accelerere og bremse.
4. Tiden på Jorden nærmer sig $4{,}25$ år, men bliver aldrig mindre. Tiden om bord
   går mod $0$. Set fra rumskibet er afstanden til Proxima længdekontraheret, så
   turen *er* kortere for passagererne. Begge forklaringer giver samme resultat.

</details>

## Et rigtigt bevis: myonerne fra atmosfæren

Myoner er små partikler, der hele tiden dannes højt oppe i atmosfæren (ca. 15 km
oppe), når kosmisk stråling rammer luften. De farer ned mod Jorden med næsten
lysets fart – men de henfalder lynhurtigt, med en gennemsnitlig levetid på kun
$\tau_0 = 2{,}2$ μs i deres eget system.

Regner man **klassisk**, når de slet ikke ned: på 2,2 μs kan de kun nå nogle få
hundrede meter. Alligevel **måler vi masser af myoner ved jordoverfladen**. Det
kan kun forklares med relativitet – og det er præcis en opgave værd (se nedenfor).
Begge forklaringer (tidsforlængelse set fra Jorden, længdekontraktion set fra
myonen) giver samme svar: myonerne når ned. Det er et af de smukkeste daglige
beviser for, at teorien er rigtig.

## Simulering: hvornår bliver relativitet vigtig?

Plottet viser, hvor mange gange længere tid der går udefra end om bord,
$\Delta t / \Delta t_0 = 1/\sqrt{1 - v^2/c^2}$, som funktion af farten. Pointen:
indtil man kommer helt tæt på $c$, er forholdet næsten $1$, og alt er som vanligt.
Den røde linje markerer myonernes fart.

```python
import numpy as np
import matplotlib.pyplot as plt

def tidsfaktor(beta):
    """Δt / Δt₀ = 1 / √(1 − v²/c²) som funktion af v/c (= beta)."""
    return 1 / np.sqrt(1 - beta**2)

beta = np.linspace(0, 0.999, 500)     # v/c fra 0 op mod 1
forhold = tidsfaktor(beta)

plt.plot(beta, forhold)
plt.axvline(0.998, color="red", linestyle="--", label="myoner: v = 0,998c")
plt.xlabel("v / c"); plt.ylabel("Δt / Δt₀")
plt.ylim(0, 20); plt.legend(); plt.show()
```

Herunder er plottet tegnet med syv legemer, fra Månen til myonerne.

![Tidsforlængelsen for Månen, Voyager 2, Merkur, Helios 2, Parker Solar Probe, stjernen S2 og myoner](/img/relativitet/tidsforlaengelse-legemer.svg)

| Legeme | Fart | $v/c$ | Ekstra tid udefra, $\Delta t/\Delta t_0 - 1$ |
|---|---|---|---|
| Månen om Jorden | $1{,}02$ km/s | $3{,}4 \cdot 10^{-6}$ | $6 \cdot 10^{-12}$ |
| Voyager 2 (i forhold til Solen) | $15{,}4$ km/s | $5{,}1 \cdot 10^{-5}$ | $1 \cdot 10^{-9}$ |
| Merkur om Solen (middelfart) | $47{,}4$ km/s | $1{,}6 \cdot 10^{-4}$ | $1 \cdot 10^{-8}$ |
| Helios 2, rekord fra 1976 | $70{,}2$ km/s | $2{,}3 \cdot 10^{-4}$ | $3 \cdot 10^{-8}$ |
| Parker Solar Probe, rekord fra 2024 | $192$ km/s | $6{,}4 \cdot 10^{-4}$ | $2 \cdot 10^{-7}$ |
| Stjernen S2 tættest på det sorte hul Sgr A* (2018) | $7650$ km/s | $0{,}0255$ | $3 \cdot 10^{-4}$ |
| Myoner fra atmosfæren | $0{,}998c$ | $0{,}998$ | $15$ |

**Sådan læser du figuren**

- **Til venstre** er akserne lineære, ligesom i koden ovenfor. Seks af de syv streger ligger klemt sammen ved $v/c \approx 0$, hvor $\Delta t/\Delta t_0 = 1$. Kun myonerne ligger, hvor kurven stiger.
- **Til højre** er begge akser logaritmiske, og der er vist $\Delta t/\Delta t_0 - 1$: hvor stor en brøkdel ekstra tid der går udefra. For Månen er det $6 \cdot 10^{-12}$: et ur på Månen sakker ca. $0{,}5$ μs bagud pr. døgn på grund af farten.
- **Selv det hurtigste, mennesker har bygget**, Parker Solar Probe, giver kun $2 \cdot 10^{-7}$. Det kan måles med atomure, men det kan ikke ses i en bane.
- **Stjernen S2** når op på $2{,}5$ % af lysets fart, når den passerer tættest på det sorte hul i Mælkevejens centrum. Her har man målt både den specielle og den generelle relativitetsteoris effekter i lyset fra stjernen.
- På en ret linje i højre graf er $\Delta t/\Delta t_0 - 1 \approx \tfrac{1}{2} \cdot \left(\tfrac{v}{c}\right)^2$. Dobbelt fart giver fire gange så stor effekt.

<details>
<summary><strong>Koden bag figuren</strong></summary>

Koden ligger i `scripts/figurer/tidsforlaengelse_legemer.py`. Den vigtigste idé er at bruge logaritmiske akser og plotte $\Delta t/\Delta t_0 - 1$:

```python
c = 299792.458                                   # km/s
farter = {"Månen": 1.02, "Voyager 2": 15.4, "Merkur": 47.4, "Helios 2": 70.2,
          "Parker Solar Probe": 192, "S2": 7650, "Myoner": 0.998 * c}
for navn, v in farter.items():
    beta = v / c
    print(navn, beta, tidsfaktor(beta) - 1)

beta = np.logspace(-6.5, np.log10(0.9999), 800)
plt.loglog(beta, tidsfaktor(beta) - 1)
plt.xlabel("v / c"); plt.ylabel("Δt/Δt₀ − 1"); plt.show()
```

Ved meget små farter regner Python $\Delta t/\Delta t_0 - 1$ forkert, fordi forholdet er så tæt på $1$, at forskellen forsvinder i afrundingen. Brug i stedet $\tfrac{1}{2} \cdot (v/c)^2$, når $v/c < 0{,}001$.

</details>

## Opgaver

### Opgave 1: Myoner fra rummet

Se filmen, før du regner opgaven. Den er på engelsk.

{{< yt id="rQXXtolNTcw" >}}

*Hard Science Explained: "Muons: Super Electrons?" (2023).*

Når kosmisk stråling rammer atmosfæren, dannes der myoner. Myoner er ustabile partikler, som henfalder til en elektron og to neutrinoer. Halveringstiden for myoner målt i myonernes eget hvilesystem er $T_{1/2} = 1{,}52\ \mu\text{s}$.

En stor del af myonerne dannes i en højde af ca. $15$ km over jordoverfladen. Vi ser på myoner, der bevæger sig lodret ned mod Jorden med farten $v = 0{,}998 \cdot c$.

**a)** Bestem den strækning, en myon tilbagelægger på én halveringstid, hvis der ses bort fra relativistiske effekter.

Målinger viser, at en betydelig del af myonerne når ned til jordoverfladen.

**b)** Bestem myonernes halveringstid målt fra Jorden.

**c)** Bestem den andel af myonerne, som når ned til jordoverfladen. Sammenlign med den andel, man får, hvis der ses bort fra relativistiske effekter.

Set fra myonernes hvilesystem er det atmosfæren, der bevæger sig.

**d)** Bestem tykkelsen af det $15$ km tykke luftlag målt i myonernes hvilesystem. Forklar, hvordan resultatet stemmer overens med resultatet i spørgsmål c.

**e)** Diskutér de forudsætninger, der er gjort i opgaven.

### Opgave 2: Rumskibet

Et rumskib flyver med farten $0{,}90 \cdot c$. Om bord går der $1{,}0$ år.

**a)** Bestem den tid, der går på Jorden.

### Opgave 3: Det forkortede rumskib

En astronaut måler sit rumskib til at være $120$ m langt.

**a)** Bestem rumskibets længde målt af en observatør, der ser det passere med farten $0{,}60 \cdot c$.

### Opgave 4: Tvillingeparadokset

**a)** Forklar med dine egne ord, hvorfor tvillingeparadokset *ikke* er en selvmodsigelse.

## Det skal I kunne efter forløbet

- Forklare de to postulater og hvad de medfører.
- Regne med tidsforlængelse $\Delta t = \Delta t_0 / \sqrt{1 - v^2/c^2}$.
- Regne med længdekontraktion $L = L_0 \cdot \sqrt{1 - v^2/c^2}$ og kende forskellen på de to effekter.
- Forklare tvillingeparadokset og hvorfor det ikke er en modsigelse.
- Anvende relativitet på myonerne fra to synsvinkler og se, at de stemmer overens.

## Hints og løsninger

<details>
<summary><strong>Hints</strong></summary>

**1a)** Strækning er fart gange tid. Brug $c = 3{,}00 \cdot 10^{8}$ m/s.

**1b)** Ure i bevægelse går langsommere. Halveringstiden målt fra Jorden er $T_{1/2,\text{Jord}} = \dfrac{T_{1/2}}{\sqrt{1 - v^2/c^2}}$.

**1c)** Find først den tid, myonerne bruger på de $15$ km, målt fra Jorden. Brug derefter henfaldsloven $\dfrac{N}{N_0} = \left(\dfrac{1}{2}\right)^{t/T_{1/2}}$ to gange: med halveringstiden fra b og med halveringstiden i hvilesystemet.

**1d)** Længden af noget, der bevæger sig, er $L = L_0 \cdot \sqrt{1 - v^2/c^2}$. Find, hvor lang tid myonen selv bruger på den forkortede strækning, og hvor mange halveringstider det svarer til.

**1e)** Tænk over højden, farten, retningen og atmosfærens påvirkning af myonerne.

**2)** Tiden om bord er egentiden $\Delta t_0$.

**3)** Astronauten måler hvilelængden $L_0$.

</details>

<details>
<summary><strong>Løsninger</strong></summary>

Der er regnet med $c = 3{,}00 \cdot 10^{8}$ m/s.

**1a)** $s = v \cdot T_{1/2} = 0{,}998 \cdot 3{,}00 \cdot 10^{8}\ \mathrm{m/s} \cdot 1{,}52 \cdot 10^{-6}\ \mathrm{s} = 455$ m. Det er langt fra de $15$ km.

**1b)** $\sqrt{1 - 0{,}998^2} = 0{,}0632$, så

$$T_{1/2,\text{Jord}} = \frac{1{,}52\ \mu\mathrm{s}}{0{,}0632} = 24{,}0\ \mu\mathrm{s}$$

**1c)** Flyvetiden set fra Jorden er

$$t = \frac{h}{v} = \frac{15 \cdot 10^{3}\ \mathrm{m}}{0{,}998 \cdot 3{,}00 \cdot 10^{8}\ \mathrm{m/s}} = 50{,}1\ \mu\mathrm{s}$$

Relativistisk:

$$\frac{N}{N_0} = \left(\frac{1}{2}\right)^{\frac{50{,}1\ \mu\mathrm{s}}{24{,}0\ \mu\mathrm{s}}} = 0{,}24$$

Uden relativitet:

$$\frac{N}{N_0} = \left(\frac{1}{2}\right)^{\frac{50{,}1\ \mu\mathrm{s}}{1{,}52\ \mu\mathrm{s}}} = 1{,}2 \cdot 10^{-10}$$

Ca. $24$ % når ned. Uden relativitet ville praktisk talt ingen nå ned. Målingerne viser altså, at relativitet er nødvendig.

**1d)** $L = 15\ \mathrm{km} \cdot 0{,}0632 = 948$ m. Myonen bruger

$$t_0 = \frac{948\ \mathrm{m}}{0{,}998 \cdot 3{,}00 \cdot 10^{8}\ \mathrm{m/s}} = 3{,}17\ \mu\mathrm{s}$$

Det er $3{,}17 / 1{,}52 = 2{,}08$ halveringstider – præcis det samme som $50{,}1 / 24{,}0 = 2{,}08$ set fra Jorden. Begge synsvinkler giver derfor samme andel, $24$ %.

**1e)** Forudsætninger:

- Alle myoner er dannet i præcis $15$ km højde. I virkeligheden dannes de i et bredt lag.
- Alle myoner har samme, konstante fart. Myoner taber energi i atmosfæren, og farten varierer.
- Banen er lodret. Skrå myoner skal tilbagelægge en længere vej.
- Jorden er regnet som et inertialsystem. Det er en god tilnærmelse på så kort tid.

**2)** $\sqrt{1 - 0{,}90^2} = 0{,}436$, så $\Delta t = \dfrac{1{,}0\ \text{år}}{0{,}436} = 2{,}3$ år.

**3)** $\sqrt{1 - 0{,}60^2} = 0{,}80$, så $L = 120\ \mathrm{m} \cdot 0{,}80 = 96$ m.

**4)** Situationen er ikke symmetrisk. Den rejsende tvilling skal bremse op, vende om og accelerere tilbage, og skifter dermed referenceramme. Den tvilling, der bliver hjemme, er hele tiden i samme inertialsystem. Derfor er det entydigt den rejsende, der ældes mindst.

</details>
