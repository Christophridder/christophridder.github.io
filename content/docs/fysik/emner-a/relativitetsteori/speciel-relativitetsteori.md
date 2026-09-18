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

Nøglestørrelsen er **Lorentz-faktoren**:

$$\gamma = \frac{1}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

Den er altid $\geq 1$. Ved hverdagsfarter er $\gamma \approx 1$ (intet mærkeligt
sker), men når $v$ nærmer sig $c$, vokser den eksplosivt.

## Del 1 – Tidsforlængelse: bevægede ure går langsommere

Et ur, der bevæger sig forbi dig, tikker **langsommere**, end dit eget gør:

$$\Delta t = \gamma \cdot \Delta t_0$$

Her er $\Delta t_0$ **egentiden** – tiden målt i det system, hvor uret er i hvile
(urets "egen" tid). $\Delta t$ er den længere tid, du måler udefra.

> **Eksempel:** Et rumskib flyver med $v = 0{,}80c$. Om bord går der
> $\Delta t_0 = 5{,}0$ år. Med $\gamma = \dfrac{1}{\sqrt{1 - 0{,}80^2}} = 1{,}67$
> går der på Jorden $\Delta t = 1{,}67 \cdot 5{,}0 = 8{,}3$ år. Rejsende ældes 5 år,
> Jorden 8,3 år. **At rejse hurtigt er at rejse ind i fremtiden.**

## Del 2 – Længdekontraktion: bevægede genstande forkortes

En genstand i bevægelse er **kortere** i bevægelsesretningen, end når den er i
hvile:

$$L = \frac{L_0}{\gamma} = L_0 \cdot \sqrt{1 - \frac{v^2}{c^2}}$$

$L_0$ er **hvilelængden** – længden målt, når genstanden er i hvile.

> **Læg mærke til modsætningen:** Tiden bliver **længere** (gang med $\gamma$),
> mens længden bliver **kortere** (divider med $\gamma$).

> **Eksempel:** Et $100$ m langt rumskib ($L_0 = 100$ m) flyver forbi med
> $0{,}80c$. En observatør i hvile måler det til $L = 100 / 1{,}67 = 60$ m.

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

Plottet viser Lorentz-faktoren som funktion af farten. Pointen: indtil man kommer
helt tæt på $c$, er $\gamma \approx 1$, og alt er som vanligt. Den røde linje
markerer myonernes fart. (Lærerdemo til forståelse – ikke et eksamensværktøj.)

```python
import numpy as np
import matplotlib.pyplot as plt

def lorentzfaktor(beta):
    """Lorentz-faktoren gamma som funktion af v/c (= beta)."""
    return 1 / np.sqrt(1 - beta**2)

beta = np.linspace(0, 0.999, 500)     # v/c fra 0 op mod 1
gamma = lorentzfaktor(beta)

plt.plot(beta, gamma)
plt.axvline(0.998, color="red", linestyle="--", label="myoner: v = 0,998c")
plt.xlabel("v / c"); plt.ylabel("Lorentz-faktor γ")
plt.ylim(0, 20); plt.legend(); plt.show()
```

## Opgaver

1. **Myonerne (hovedopgave).** Myoner dannes i $h = 15$ km højde og farer mod
   Jorden med $v = 0{,}998c$. Deres gennemsnitlige levetid i eget system er
   $\tau_0 = 2{,}2$ μs. Brug $c = 3{,}00 \cdot 10^{8}$ m/s.
   - a) Hvor langt ville en myon nå på én levetid, hvis man regner **klassisk**
     (uden relativitet)? Kommentér.
   - b) Bestem Lorentz-faktoren $\gamma$ for $v = 0{,}998c$.
   - c) **Set fra Jorden:** myonens levetid forlænges til $\tau = \gamma \cdot \tau_0$.
     Find $\tau$ og den tilbagelagte strækning $v \cdot \tau$.
   - d) **Set fra myonen:** atmosfærens tykkelse er længdekontraheret. Find den
     kontraherede tykkelse $L = h / \gamma$.
   - e) Forklar, hvorfor begge synsvinkler fører til, at myonerne når jorden.
2. Et rumskib flyver med $0{,}90c$. Bestem $\gamma$. Hvor lang tid går der på
   Jorden, mens der om bord går $1{,}0$ år?
3. En astronaut måler sit $120$ m lange rumskib. Hvor langt er det for en
   observatør, der ser det passere med $0{,}60c$?
4. **Diskussion:** Forklar med dine egne ord, hvorfor tvillingeparadokset *ikke*
   er en selvmodsigelse.

> **Facit til opgave 1:** a) $d = v \cdot \tau_0 \approx 6{,}6 \cdot 10^{2}$ m
> (ca. 660 m – langt fra de 15 km). b) $\gamma \approx 15{,}8$.
> c) $\tau \approx 35$ μs, $v \cdot \tau \approx 1{,}0 \cdot 10^{4}$ m (ca. 10 km –
> og da mange myoner lever flere levetider, når rigeligt med dem ned).
> d) $L \approx 9{,}5 \cdot 10^{2}$ m (ca. 950 m), som myonen sagtens krydser på
> sin egen levetid.

## Det skal I kunne efter forløbet

- Forklare de to postulater og hvad de medfører.
- Bruge Lorentz-faktoren og regne med tidsforlængelse $\Delta t = \gamma \Delta t_0$.
- Bruge længdekontraktion $L = L_0 / \gamma$ og kende forskellen på de to effekter.
- Forklare tvillingeparadokset og hvorfor det ikke er en modsigelse.
- Anvende relativitet på myonerne fra to synsvinkler og se, at de stemmer overens.
