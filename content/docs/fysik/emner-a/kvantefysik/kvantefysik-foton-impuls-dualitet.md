---
title: "Kvantefysik – fotonenergi, impuls og dualitet"
weight: 10
---

**Niveau: Fysik A** · **Emne: Kvantefysik** · **Bygger på: Bohrs atommodel, emission/absorption, spektre, isotoper**

Dette forløb tager fat, hvor I slap: I kender Bohrs model, hvordan atomer
udsender og optager lys, Balmer-linjerne og isotoper. Nu kvantificerer vi selve
**fotonen** – dens energi og dens bevægelsesmængde – og udvider til
**partikel-bølge-dualiteten**, som binder lys og stof sammen.

## Fra Bohr til fotonen

I Bohrs model springer elektronen mellem energiniveauer. Når den falder fra et
højt til et lavt niveau, udsendes en foton med netop energiforskellen:

$$E_{\text{foton}} = E_2 - E_1 = h \cdot f$$

Det er denne sammenhæng, der giver de skarpe spektrallinjer, I har set i
Balmer-serien. Indtil nu har fotonen mest været "lyspakken, der bærer
energiforskellen". Nu ser vi nærmere på, hvad den selv kan.

## Fotonens energi

En foton med frekvens $f$ og bølgelængde $\lambda$ har energien

$$E = h \cdot f = \frac{h \cdot c}{\lambda}$$

med Plancks konstant $h = 6{,}63 \cdot 10^{-34}$ J·s og lysets fart
$c = 3{,}00 \cdot 10^{8}$ m/s.

Energier på atomar skala er små i joule, så vi bruger ofte **elektronvolt**:

$$1 \text{ eV} = 1{,}602 \cdot 10^{-19} \text{ J}$$

> **Praktisk regnegenvej:** Med $\lambda$ i nanometer og $E$ i eV gælder
> $$E_{\text{foton}} \approx \frac{1240}{\lambda}$$
> fordi $h \cdot c \approx 1240$ eV·nm. Den er guld værd til hurtige overslag.

**Eksempel – Balmer-α (H-α), $\lambda = 656$ nm:**

$$E = \frac{1240}{656} \approx 1{,}89 \text{ eV}$$

eller i joule: $E = \dfrac{6{,}63 \cdot 10^{-34} \cdot 3{,}00 \cdot 10^{8}}{656 \cdot 10^{-9}} \approx 3{,}03 \cdot 10^{-19}$ J.

## Den fotoelektriske effekt (energi i spil)

Når lys rammer en metaloverflade, kan fotonerne slå elektroner løs – men kun
hvis hver foton har energi nok. Energibevarelse giver:

$$h \cdot f = W + E_{\text{kin,max}}$$

hvor $W$ er **løsrivelsesarbejdet** (metallets bindingsenergi for elektronen) og
$E_{\text{kin,max}}$ den maksimale kinetiske energi af den løsrevne elektron.
Pointen, som Einstein fik Nobelprisen for i 1921: det er fotonens **frekvens**,
ikke lysets intensitet, der afgør, om elektroner rives løs. Under en vis
tærskelfrekvens sker der intet, uanset hvor kraftigt man lyser.

> **Eksperiment til delprøven:** Bestem Plancks konstant med lysdioder (LED'er).
> En LED begynder først at lyse, når spændingen $U$ er stor nok til, at hver
> elektron leverer energien til en foton: $e \cdot U \approx \dfrac{h \cdot c}{\lambda}$.
> Måler man tændspændingen $U$ for LED'er med forskellig bølgelængde og plotter
> $U$ mod $1/\lambda$, bliver hældningen $\dfrac{h \cdot c}{e}$ – og dermed kan
> $h$ bestemmes. Metoden giver et fint overslag (tændspændingen er ikke helt
> eksakt $hc/e\lambda$ pga. båndstrukturen, men afvigelsen er lille).

## Fotonens bevægelsesmængde (impuls)

Selvom fotonen er masseløs, bærer den **bevægelsesmængde**. Det følger af
relativitetsteorien, hvor en masseløs partikel opfylder $E = p \cdot c$. Sammen
med $E = h \cdot f$ giver det:

$$p = \frac{E}{c} = \frac{h \cdot f}{c} = \frac{h}{\lambda}$$

Lys kan altså "skubbe": det er princippet bag strålingstryk og solsejl.

**Eksempel – samme H-α-foton ($\lambda = 656$ nm):**

$$p = \frac{h}{\lambda} = \frac{6{,}63 \cdot 10^{-34}}{656 \cdot 10^{-9}} \approx 1{,}01 \cdot 10^{-27} \text{ kg·m/s}$$

> **For de skarpe – Compton-spredning:** At fotonen har impuls, ses direkte, når
> en foton "støder" ind i en fri elektron som to billardkugler. Fotonen taber
> energi og får større bølgelængde, afhængigt af spredningsvinklen $\theta$:
> $$\Delta\lambda = \frac{h}{m_e \cdot c}\left(1 - \cos\theta\right)$$
> Faktoren $\dfrac{h}{m_e \cdot c} = 2{,}43 \cdot 10^{-12}$ m kaldes elektronens
> Compton-bølgelængde. Forsøget (Compton, 1923) er et rent stødproblem, hvor
> både energi og bevægelsesmængde er bevaret – et flot bevis for fotonens
> partikelnatur.

## Partikel-bølge-dualitet

Hvis lys (en bølge) kan opføre sig som partikler, kan partikler så opføre sig
som bølger? Ja. de Broglie foreslog i 1924, at enhver partikel med
bevægelsesmængde $p$ har en bølgelængde:

$$\lambda = \frac{h}{p} = \frac{h}{m \cdot v}$$

Det blev bekræftet ved, at elektroner kan **diffraktere** ligesom lys.

**Eksempel – elektron med $v = 1{,}0 \cdot 10^{6}$ m/s:**

$$\lambda = \frac{6{,}63 \cdot 10^{-34}}{9{,}11 \cdot 10^{-31} \cdot 1{,}0 \cdot 10^{6}} \approx 7{,}3 \cdot 10^{-10} \text{ m} = 0{,}73 \text{ nm}$$

– altså på atomar skala, hvor bølgenaturen tydeligt slår igennem.

> **Model og gyldighed (A-niveau):** Regn de Broglie-bølgelængden for en
> fodbold (fx 0,4 kg ved 20 m/s). Du får noget i størrelsesordenen
> $10^{-34}$ m – uendeligt mindre end alt målbart. Derfor mærker vi ikke
> bølgenaturen i hverdagen: den bliver kun relevant, når $\lambda$ er
> sammenlignelig med systemets størrelse. Det er et godt eksempel på en models
> gyldighedsområde.

## Python: energi og impuls for spektrallinjer

Snippet'et regner fotonenergi og -impuls for Balmer-linjerne, så I kan koble de
nye begreber til det spektrum, I allerede kender.

```python
import numpy as np

h = 6.626e-34      # Plancks konstant [J·s]
c = 2.998e8        # lysets fart [m/s]
eV = 1.602e-19     # 1 elektronvolt [J]

def fotonenergi(lambda_m):
    """Fotonens energi (J) ud fra bølgelængden i meter."""
    return h * c / lambda_m

def fotonimpuls(lambda_m):
    """Fotonens bevægelsesmængde (kg·m/s) ud fra bølgelængden i meter."""
    return h / lambda_m

# Balmer-linjer (nm) -> meter
balmer_nm = np.array([656.3, 486.1, 434.0, 410.2])
balmer_m = balmer_nm * 1e-9

for lam_nm, lam_m in zip(balmer_nm, balmer_m):
    E = fotonenergi(lam_m)
    p = fotonimpuls(lam_m)
    print(f"{lam_nm:6.1f} nm:  E = {E/eV:5.3f} eV,  p = {p:.3e} kg*m/s")
```

## Opgaver

1. En natriumlampe udsender gult lys med $\lambda = 589$ nm. Bestem fotonens
   energi i både joule og eV, samt dens bevægelsesmængde.
2. Løsrivelsesarbejdet for cæsium er $W = 2{,}1$ eV. Bestem tærskelbølgelængden,
   og afgør om synligt grønt lys ($\lambda = 530$ nm) kan løsrive elektroner.
3. En elektron accelereres gennem en spændingsforskel på $100$ V. Bestem dens
   bevægelsesmængde og de Broglie-bølgelængde. (Hjælp: $E_{\text{kin}} = e \cdot U$.)
4. **For de skarpe:** En foton med $\lambda = 0{,}050$ nm (røntgen) Compton-spredes
   $90^\circ$ på en elektron. Bestem den spredte fotons bølgelængde og energitab.

## Samling – det skal I kunne efter forløbet

- Beregne en fotons energi ud fra frekvens eller bølgelængde, i J og eV.
- Forklare og anvende den fotoelektriske effekt, herunder tærskelfrekvens.
- Beregne fotonens bevægelsesmængde og forklare, at masseløst lys kan bære impuls.
- Anvende de Broglie-relationen og diskutere, hvornår bølgenaturen er relevant
  (modellens gyldighedsområde).
