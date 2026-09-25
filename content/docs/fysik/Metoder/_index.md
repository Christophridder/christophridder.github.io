---
title: "Faglige metoder i fysik"
weight: 30
bookCollapseSection: true
---

**Niveau: Fysik C–A** · **Emne: Faglige metoder**

Her samles de faglige metoder, vi bruger i fysik – kort forklaret, med eksempler og forslag til forsøg. Metoder uden link er på vej.

## To niveauer af metode

**1. De overordnede metoder** – sådan skaber fysik ny viden. Dem kan du læse om under [Naturvidenskabelig metode]({{< relref "/docs/nat/naturvidenskabelig-metode" >}}).

| Metode | Kort fortalt |
|---|---|
| Eksperimentel metode | Du måler, ændrer én variabel ad gangen og gentager ([Variabelkontrol]({{< relref "/docs/nat/variabelkontrol" >}})) |
| Teoretisk modellering | Du opstiller en model ud fra kendte love og udleder, hvad der må ske |
| Numerisk simulering | Du lader computeren regne modellen ud trin for trin, når den ikke kan løses med papir og blyant |
| Model mod data | Du sammenligner model og målinger og vurderer, hvor langt modellen holder |

**2. De konkrete teknikker** – fysikkens svar på kemiens titrering og spektrofotometri. Dem finder du nedenfor.

## Dataopsamling – sådan får du målingerne

| Metode | Kort fortalt | Bruges fx i |
|---|---|---|
| [Videoanalyse]({{< relref "/docs/fysik/Metoder/videoanalyse" >}}) | Position frame for frame ud fra en video → $(t, x, y)$-data | [Kasteparabel]({{< relref "/docs/fysik/A-Eksp/kasteparabel" >}}) |
| Sensorer og dataopsamling | Kraft, position, temperatur eller spænding logget automatisk med LoggerPro | [Hop på kraftplatform]({{< relref "/docs/fysik/A-Eksp/kraftplatform-hop" >}}), [Hookes lov]({{< relref "/docs/fysik/A-Eksp/Hookes-lov" >}}) |
| GM-rør og tællinger | Radioaktiv stråling målt som tælletal – med baggrund og tællestatistik | [Afstandskvadratloven]({{< relref "/docs/fysik/C-Eksp/afstandskvadratloven" >}}), [Halveringstid]({{< relref "/docs/fysik/C-Eksp/halveringstid" >}}), [Halveringstykkelse]({{< relref "/docs/fysik/C-Eksp/halveringstykkelse" >}}) |
| Spektroskopi med gitter | Bølgelængder bestemt ud fra afbøjningsvinkler | [Gitterligningen]({{< relref "/docs/fysik/C-Eksp/gitterligningen" >}}) |
| Lydoptagelse og frekvensanalyse (FFT) | Grundtone og overtoner fundet i en lydoptagelse | [Klang]({{< relref "/docs/fysik/C-Eksp/klang" >}}), [Lydens hastighed]({{< relref "/docs/fysik/C-Eksp/lydens-hastighed" >}}) |
| Kalorimetri | Energi bestemt ud fra temperaturændringer | [Varmekapacitet]({{< relref "/docs/fysik/C-Eksp/varmekapacitet" >}}) |

## Databehandling – sådan får du mening i målingerne

| Metode | Kort fortalt |
|---|---|
| [Lineær regression]({{< relref "/docs/nat/lineaer-regression" >}}) | Hældningen på en ret linje giver en fysisk størrelse, fx $g$ eller en fjederkonstant |
| [Linearisering (aksetransformation)]({{< relref "/docs/nat/lineaer-regression" >}}) | Du omskriver en potens- eller eksponentialsammenhæng, så den bliver lineær |
| Usikkerhed og fejlforplantning | Hvor sikkert er resultatet? Se også [Fejlkilder]({{< relref "/docs/nat/fejlkilder" >}}) og [Betydende cifre]({{< relref "/docs/nat/betydendecifre" >}}) |
| Enhedsanalyse | Passer enhederne? Et hurtigt tjek af formler og resultater |
| Numeriske metoder | Euler og Runge-Kutta til bevægelser med fx luftmodstand |
