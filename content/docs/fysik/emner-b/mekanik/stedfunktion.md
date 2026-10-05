---
title: "Stedfunktionen"
weight: 1
---

**Niveau: Fysik B** · **Emne: Mekanik**

[Tilbage til Mekanik]({{< relref "/docs/fysik/emner-b/mekanik" >}})

## Kort forklaret

- **Stedfunktionen** $x(t)$ fortæller, *hvor* et legeme er til tiden $t$.
- $x$ måles i meter ud fra et valgt **origo** og en valgt **positiv retning**. Begge dele vælger du selv – men du skal skrive valget ned.
- Ud fra $x(t)$ kan du finde alt andet om bevægelsen:

| Størrelse | Sammenhæng | Grafisk betydning |
|---|---|---|
| Hastighed $v(t)$ | $v(t) = x'(t)$ | Hældningen af tangenten til $x(t)$-grafen |
| Acceleration $a(t)$ | $a(t) = v'(t) = x''(t)$ | Hældningen af tangenten til $v(t)$-grafen |
| Forskydning $\Delta x$ | $\Delta x = \int_{t_1}^{t_2} v(t)\,\mathrm{d}t$ | Arealet under $v(t)$-grafen |

## To vigtige stedfunktioner

| Bevægelse | Stedfunktion | Hastighed | Graf for $x(t)$ |
|---|---|---|---|
| Konstant hastighed | $x(t) = v \cdot t + x_0$ | $v$ (konstant) | Ret linje |
| Konstant acceleration | $x(t) = \tfrac{1}{2} a \cdot t^2 + v_0 \cdot t + x_0$ | $v(t) = a \cdot t + v_0$ | Parabel |

Her er $x_0$ stedet og $v_0$ hastigheden til $t = 0$.

**Lodret kast og frit fald** er konstant acceleration med $a = -g$, når $y$-aksen peger opad:

$$y(t) = -\tfrac{1}{2} g \cdot t^2 + v_{0y} \cdot t + y_0$$

## Anvendelse: fra målinger til fysik

Med [videoanalyse]({{< relref "/docs/fysik/Metoder/videoanalyse" >}}) får du en tabel med $(t, y)$. Laver du andengradsregression

$$y = a_2 t^2 + a_1 t + a_0,$$

kan du sammenligne leddene med stedfunktionen og aflæse:

| Regressionskonstant | Svarer til | Fysisk størrelse |
|---|---|---|
| $a_2$ | $-\tfrac{1}{2} g$ | $g = -2 \cdot a_2$ |
| $a_1$ | $v_{0y}$ | Starthastighed lodret |
| $a_0$ | $y_0$ | Starthøjde |

### Eksempel

En bold kastes lodret op. Regressionen giver

$$y = -4{,}87\,\tfrac{\mathrm{m}}{\mathrm{s}^2} \cdot t^2 + 6{,}20\,\tfrac{\mathrm{m}}{\mathrm{s}} \cdot t + 1{,}10\,\mathrm{m}$$

- $g = -2 \cdot (-4{,}87\ \mathrm{m/s^2}) = 9{,}74\ \mathrm{m/s^2}$ – ca. 1 % fra tabelværdien $9{,}82\ \mathrm{m/s^2}$.
- Starthastighed: $v_{0y} = 6{,}20\ \mathrm{m/s}$, starthøjde: $y_0 = 1{,}10\ \mathrm{m}$.
- Toppunkt: $v(t) = 0 \Rightarrow t = \dfrac{6{,}20}{9{,}74}\ \mathrm{s} = 0{,}64\ \mathrm{s}$, og $y(0{,}64\ \mathrm{s}) = 3{,}07\ \mathrm{m}$.

## Hvornår holder modellen?

- Parablen forudsætter **konstant acceleration** – altså at kun tyngdekraften virker.
- Ved tunge, kompakte genstande (tennisbold, sten) over korte afstande er **luftmodstanden** lille, og modellen passer fint.
- Ved lette genstande med stor overflade (badmintonbold, papir) bliver luftmodstanden stor. Så er banen ikke en parabel, og $-2 \cdot a_2$ er *ikke* $g$.
- Tjek derfor altid **residualerne**: Ligger punkterne systematisk over og under fittet, holder modellen ikke.

Prøv selv med klassens [tennis- og badmintonvideoer]({{< relref "/docs/fysik/emner-b/mekanik/tennis_badminton" >}}).
