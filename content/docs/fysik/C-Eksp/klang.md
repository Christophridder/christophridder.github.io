---
title: "Klang"
weight: 120
---
**Niveau:** Fysik C · **Emne:** Lyd og bølger


## Introduktion

Hvorfor lyder en guitar og en fløjte forskelligt, selvom de spiller **den samme
tone** — fx samme A på $440\text{ Hz}$? Og hvorfor kan man høre forskel på en
dreng og en pige, der synger nøjagtig samme tone? Svaret er **klang** (på engelsk
*timbre*, på tysk *Klangfarbe*). Tonens **højde** bestemmes af grundtonens
frekvens, men selve "farven" af lyden bestemmes af de **overtoner**, der ligger
oven på grundtonen.

Når en lydkilde frembringer en tone, lyder grundtonen ($f_0$) sjældent alene. Oven
på den ligger en række overtoner:

$$f_n = n \cdot f_0$$

- $f_0$ er grundtonen (laveste frekvens)
- $f_2 = 2 f_0$, $f_3 = 3 f_0$ osv. er overtonerne

Det er **styrkeforholdet** (amplituderne) mellem grundtone og overtoner, der giver
hver lydkilde sin karakteristiske klang.

> Når man splitter en lyd op i dens enkelte frekvenser, laver man en
> **frekvensanalyse** (en Fourier-analyse) — det er præcis, hvad LoggerPro gør med
> sit **FFT**-værktøj. Hver søjle i FFT-billedet er én frekvens, og søjlens højde
> er amplituden af netop den frekvens.

### Hvilke overtoner er til stede?

Det afhænger af lydkilden, hvilke overtoner der overhovedet kan dannes:

- **Streng** (fastgjort i begge ender): **alle** overtoner, $n = 1, 2, 3, 4, \dots$
- **Åbent rør** (åbent i begge ender): **alle** overtoner, $n = 1, 2, 3, 4, \dots$
- **Lukket rør** (lukket i den ene ende): **kun de ulige** overtoner,
  $n = 1, 3, 5, 7, \dots$ — de lige ($2f_0$, $4f_0$ …) mangler helt.

Netop derfor lyder et lukket rør mere "hult" end et åbent rør af samme tone.

---

## Variabelkontrol

- **Uafhængig variabel:** lydkilden (det, vi sammenligner — streng, åbent rør,
  lukket rør, drenge- og pigestemme).
- **Afhængig variabel:** frekvensspektret — hvilke overtoner der er til stede, og
  hvor kraftige de er.
- **Kontrollerede variabler:** samme grundtone (samme spillede/sungne tone, fx A
  på $440\text{ Hz}$), samme mikrofon og opstilling, samme samplingsrate.

---

## Materialer

- mikrofon + LoggerPro (med FFT/frekvensanalyse)
- en streng (guitar)
- et åbent rør og et lukket rør, der kan give en tone
- to sangere (fx en dreng og en pige), der kan synge samme tone

---

## Gennemførelse

For hver lydkilde gør I følgende:

1. Frembring tonen, og optag den i LoggerPro. 
   * spil et **a** på guitaren det er den næsttykkeste streg :-) 
   * når I synger så er det vigtigt at det er stille i lokalet. Start med at synge højt på **aaaaa** tænd og sluk loggerpro imens tonen lyder. 
   * ved rør der det smart at slå stærkt på røret hurtigt og mange gang i træk bum bum bum bum bum .. så optager i flere toner i rap og loggerpro kan analysere dem på en gang 
2. Se på selve **bølgeformen** (lydtrykket over tid): er den en pæn sinuskurve
   eller mere kompliceret?
3. Kør en **frekvensanalyse (FFT)**, så I ser tonens spektrum.
4. Aflæs grundtonens frekvens $f_0$, og notér hvilke overtoner ($2f_0$, $3f_0$ …)
   der dukker op, og hvor høje deres amplituder er.

### Del 1: Streng, åbent rør og lukket rør

Hold den **samme grundtone** for alle tre, og sammenlign spektrene:

- Streng og åbent rør: ses hele overtonerækken?
- Lukket rør: mangler de lige overtoner ($2f_0$, $4f_0$ …)?

### Del 2: Dreng og pige synger samme tone

Lad en dreng og en pige synge **samme tone** — fx A på $440\text{ Hz}$. Optag hver
af dem, og sammenlign FFT-billederne.

> Selvom grundtonen $f_0$ er den samme, vil amplituderne på overtonerne typisk være
> meget forskellige. Det er præcis det, der gør, at man straks kan høre forskel på
> de to stemmer — selvom de rammer den samme tone.

### Måletabel

| Lydkilde | $f_0$ / Hz | Kraftige overtoner (og amplituder) | Bølgeformens udseende |
|------|------|------|------|
| Streng | | | |
| Åbent rør | | | |
| Lukket rør | | | |
| Drengestemme | | | |
| Pigestemme | | | |

---

## Afrapportering

- Skærmbilleder af både bølgeform og FFT-spektrum for hver lydkilde.
- Aflæste grundtoner og overtoner med deres amplituder.
- En forklaring af, hvorfor lydkilderne lyder forskelligt, selvom de frembringer
  samme tone — koblet til overtonernes amplituder.
- En kommentar til det **lukkede rør**: kan I se, at de lige overtoner mangler?
- En kommentar til **drenge- og pigestemmen**: hvordan adskiller deres
  overtonemønstre sig, selvom grundtonen er den samme?
