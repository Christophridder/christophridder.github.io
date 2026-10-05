---
title: "Lydanalyse (FFT)"
weight: 20
---

# Lydanalyse – frekvensspektrum med FFT

**Niveau: Fysik C** · **Emne: Lyd og bølger – metode**

Med [lydanalyseprogrammet](/lydanalyse.html) kan du se, hvilke frekvenser en lyd består af. Programmet laver en **FFT** (Fast Fourier Transformation) af din optagelse og tegner et **frekvensspektrum**: frekvens $f$ ud ad x-aksen og amplitude op ad y-aksen.

[Åbn lydanalyseprogrammet](/lydanalyse.html) · [Om programmet]({{< relref "lydanalyseprogram" >}})

## Lidt teori

- En **tone** fra et musikinstrument eller en stemme er en periodisk svingning. Den består af en **grundtone** $f_1$ og **overtoner** (harmoniske) med frekvenserne

$$f_n = n \cdot f_1, \qquad n = 1, 2, 3, \dots$$

- Grundtonen bestemmer, **hvilken tone** du hører.
- Overtonernes indbyrdes styrke bestemmer **klangfarven** – derfor lyder en trompet og en klarinet forskelligt, selv om de spiller samme tone.
- En klarinet har næsten kun **ulige** harmoniske ($n = 1, 3, 5, \dots$), fordi røret virker som et rør, der er lukket i den ene ende.
- Et metalrør, der bankes på, har **ikke** harmoniske overtoner: Forholdene er ca. $1 : 2{,}76 : 5{,}40$.

## 1. Optag lyden i Audacity

1. Sæt optagelsen til **mono** og **44100 Hz** (det er normalt standard).
2. Hold mikrofonen 20–50 cm fra instrumentet. Spil eller syng en **rolig, lang tone** i ca. 3 sekunder.
3. Se på bølgeformen: Den må **ikke ramme toppen** af vinduet (klipning giver falske overtoner). Optag igen og lidt svagere, hvis den gør.
4. Gem som **WAV**: *Fil → Eksportér lyd → WAV* (menupunkterne kan hedde lidt forskelligt i forskellige versioner af Audacity).

Programmet kan også åbne MP3, FLAC, OGG og M4A (fx fra en telefon). Virker en fil ikke i din browser, så gem den som WAV.

## 2. Analysér lyden

1. **Åbn lydfil** – eller træk filen ind på siden. Du kan have op til **4 lyde** åbne på én gang.
2. **Vælg udsnit** i bølgeformen: Træk hen over den del, du vil analysere. Programmet foreslår selv et udsnit, der springer **anslaget** over – tjek, at det passer. Brug *Afspil udsnit* for at høre det.
3. Vælg **frekvensområde** (*Fra/Til* eller knapperne *0–1 kHz*, *0–2 kHz* …), så toppene fylder grafen.
4. Hold musen over grafen: Under grafen kan du aflæse frekvensen ved markøren og den nærmeste top.
5. Træk den **røde tærskellinje** (eller slideren til højre) op, til kun de rigtige toppe er markeret. Støj og små toppe forsvinder fra tabellen.
6. **Klik på grundtonen** i grafen (eller i tabellen). Så viser tabellen $f/f_1$ og hvor langt hver top ligger fra $n \cdot f_1$.
7. *Sammenlign alle* viser alle lyde under hinanden med **samme frekvensakse**.

## 3. Eksportér

| Knap | Hvad får du? |
|---|---|
| **Excel (.xlsx)** | Et ark pr. lyd med toppene over tærsklen: $f$, relativ amplitude, $f/f_1$, $n$ og afvigelse. Tallene er rigtige tal, så Excel viser dansk decimalkomma. Sæt flueben, hvis du også vil have hele spektret med. |
| **Python (.py)** | Et færdigt script med dine data: Spektrene plottes under hinanden med identisk x-akse, og overtonemønstret vises som søjlediagram. Ret `FMIN` og `FMAX` øverst i filen og kør igen. |

## Eksempellyde

Vælg dem i menuen *Eksempellyde* i programmet, eller hent dem som WAV-filer:

| Lyd | Hvad kan du se? |
|---|---|
| [Stemmegaffel 440 Hz](/lyd/lydanalyse/stemmegaffel_440Hz.wav) | Næsten en ren sinustone – én top |
| [Klarinet-lignende 220 Hz](/lyd/lydanalyse/klarinet_220Hz.wav) | Næsten kun ulige harmoniske |
| [Trompet-lignende 466 Hz](/lyd/lydanalyse/trompet_466Hz.wav) | Mange stærke overtoner – 2. harmoniske er stærkest |
| [Guitar-lignende 110 Hz](/lyd/lydanalyse/guitar_110Hz.wav) | Overtonerne dør hurtigere ud end grundtonen – prøv et tidligt og et sent udsnit |
| [Sang – stemme A, 262 Hz](/lyd/lydanalyse/sang_stemmeA_262Hz.wav) og [stemme B](/lyd/lydanalyse/sang_stemmeB_262Hz.wav) | Samme tone, forskelligt overtonemønster |
| [Metalrør, slået 4 gange](/lyd/lydanalyse/metalroer_4slag.wav) | Ikke-harmoniske overtoner, og toppene "flækker", hvis udsnittet indeholder flere slag |
| [Svævning 440 Hz + 443 Hz](/lyd/lydanalyse/svaevning_440_443Hz.wav) | To toner tæt på hinanden – kræver et langt udsnit og lille *min. afstand* |

## Hvornår kan du stole på resultatet?

- **Frekvensopløsning:** Programmet kan kun skelne frekvenser, der ligger mere end ca. $\Delta f = 1/T$ fra hinanden, hvor $T$ er udsnittets varighed. Et udsnit på $0{,}5\ \mathrm{s}$ giver $\Delta f \approx 2\ \mathrm{Hz}$. Programmet viser $\Delta f$ ved udsnittet. Længere udsnit giver skarpere toppe – men kun hvis tonen er stabil hele vejen.
- **Anslaget:** I starten af en tone (anslag, tungestød, slag) er lyden ikke periodisk. Tager du anslaget med, får du en bred, rodet bund.
- **Flere slag i udsnittet:** Bankes et rør flere gange inden for udsnittet, kan én top dele sig i flere tætliggende toppe. Vælg et udsnit med kun ét slag.
- **Tonen ændrer sig:** Vibrato eller en tone, der glider, giver brede toppe – frekvensen er jo ikke konstant.
- **Klipning:** En optagelse, der rammer loftet, får falske overtoner.
- **Mikrofonen** er ikke lige følsom for alle frekvenser, så de relative amplituder er kun omtrentlige. Frekvenserne er derimod meget præcise.
- **Relativ amplitude:** Den største top sættes til 1. Du kan sammenligne toppe *inden for* samme lyd, men ikke lydstyrken mellem to optagelser.

## Opgaveforslag

1. Optag din egen stemme og en klassekammerats, der synger **samme tone**. Bestem $f_1$ for begge, og sammenlign overtonemønstrene i Python-eksporten.
2. Optag et instrument, og undersøg, om overtonerne passer med $f_n = n \cdot f_1$. Hvor stor er afvigelsen i procent?
3. Analysér *Metalrør*-lyden. Bestem forholdet mellem overtonerne og grundtonen. Er de harmoniske?
4. Analysér *Guitar*-lyden med et udsnit fra starten og et udsnit fra slutningen. Hvad sker der med overtonerne?
