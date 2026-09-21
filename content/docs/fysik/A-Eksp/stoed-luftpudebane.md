---
title: "Stød på luftpudebane"
weight: 10
pdf: "pdfs/stoed-luftpudebane.pdf"
pdf_ny_fane: true
---

**Niveau: Fysik A** · **Emne: Mekanik – bevægelsesmængde og stød** · **Eksperiment: luftpudebane med fotoceller**

[Tilbage til Eksperimenter A](/docs/fysik/a-eksp/) · Teori og opgaver:
[Stød og bevægelsesmængde]({{< relref "stoed-bevaegelsesmaengde" >}}) og
[Opgaver: bevægelsesmængde og kraftens impuls]({{< relref "stoed-opgaver" >}})

## Formål

Undersøge om **bevægelsesmængden** $p = m \cdot v$ er bevaret ved tre typer stød, og om den **kinetiske energi** er bevaret:

1. Elastisk stød
2. Fuldstændig uelastisk stød
3. Et projektil fra et luftgevær, der bliver siddende i en træklods på en vogn

## Udstyr

- Luftpudebane med to vogne (lav gnidning) og kompressor
- To **fotoceller** med tidsmåling (gate-tilstand, dvs. tiden strålen er afbrudt)
- En **strimmel på 10 cm** på hver vogn, der kører gennem fotocellen
- Fjederbøjler til elastiske stød
- Velcro til fuldstændig uelastiske stød
- Lodder til at ændre vognenes masse
- Vægt (til vognene) og skydelære (til strimlen)
- Til forsøg 3: luftgevær, træklods med plads til projektilet, **beskyttelsesbriller** og en kuglefanger bag banen

## Målemetode

Strimlen på vognen afbryder fotocellens stråle i tiden $\Delta t$, og fartens størrelse er

$$v = \frac{\ell}{\Delta t}$$

hvor $\ell$ er strimlens længde (ca. $0{,}100$ m, mål den med skydelære).

- Fortegn: Vælg højre som positiv retning. Passerer en vogn fotocellen mod venstre, sættes fortegnet til $-$.
- Vogne på luftpudebanen: Vej begge vogne inklusive strimmel og velcro, som de sidder under forsøget.
- Opstilling: Sæt fotocelle A til venstre for stødstedet og fotocelle B til højre for stødstedet.
  - Vogn 1 passerer A på vej ind (fart $v_1$) og igen på vej tilbage, hvis den støder tilbage (fart $u_1$).
  - Vogn 2 ligger i ro til at starte med og passerer B efter stødet (fart $u_2$).
- Hvis en vogn efter stødet står stille eller kun bevæger sig ganske langsomt, kan farten ikke måles med fotocellen. Skriv i så fald $u \approx 0$ og notér, at du har observeret, at vognen blev stående.

> **Tjek banen:** Løft ikke banen til luftpuden er tændt, og kontrollér, at banen er vandret. Læg en vogn i ro midt på banen. Den skal blive liggende. Hvis den driver, skal banen justeres, inden du går videre.

## Forsøg 1 – Elastisk stød

Vogn 2 ligger i ro på banen, og vogn 1 skydes ind i den. Begge vogne har fjederbøjler i enderne, så de støder elastisk.

### 1a) To lige store masser

- Vælg $m_1 \approx m_2$.
- **Hypotese (før du måler):** Brug formlerne for elastisk stød med $v_2 = 0$ fra teorisiden. Hvad forudsiger de for $u_1$ og $u_2$, når $m_1 = m_2$?
- Mål $v_1$, $u_1$ og $u_2$. Gentag mindst 3 gange.

### 1b) Lille masse mod stor masse

- Lad vogn 1 være den lette vogn ($m_1 \approx 0{,}20$ kg), og læg lodder på vogn 2, så $m_2$ er mindst to gange så stor.
- **Hypotese:** Beregn $u_1$ og $u_2$ ud fra $m_1$, $m_2$ og $v_1$ med
$$u_1 = \frac{m_1 - m_2}{m_1 + m_2} \cdot v_1 \qquad u_2 = \frac{2 \cdot m_1}{m_1 + m_2} \cdot v_1$$
  Hvilken retning har vogn 1 efter stødet?
- Mål $v_1$, $u_1$ og $u_2$. Gentag mindst 3 gange.

## Forsøg 2 – Fuldstændig uelastisk stød

Sæt velcro på begge vognes stødende ender, så de hænger sammen efter stødet. Vogn 2 ligger i ro.

- Vogn 1 skydes ind i vogn 2. Mål $v_1$ ved fotocelle A og den fælles fart $u$ ved fotocelle B.
- **Hypotese:** Brug
$$u = \frac{m_1 \cdot v_1}{m_1 + m_2}$$
  til at forudsige $u$.
- Gentag med ekstra lodder på vogn 2, så masseforholdet ændres. Prøv mindst to forskellige masseforhold.

## Forsøg 3 – Projektil i træklods (luftgevær)

Træklodsen sidder fast på en vogn, og et projektil fra et luftgevær skydes ind i den og bliver siddende. Det er et fuldstændig uelastisk stød, hvor projektilet har meget lille masse og meget stor fart.

> **Sikkerhed:** DET HER ER FARLIGT !!!! TAG SIKKERHED MEGET SERIØST
>
> - Luftgeværet bruges kun **under lærerens opsyn**.
> - **ALLE** bærer **beskyttelsesbriller**.
> - Ingen står foran eller ved siden af banen. Bag banen skal der være en kuglefanger.
> - Skyd kun mod klodsen, og kun når banen er klar.

### Opstilling og måling

- Vej **projektilet**: Vej fx 10 projektiler på én gang, og divider med 10. Så er usikkerheden på $m_p$ lille.
- Vej vognen med træklods ($M$).
- Sigt, så projektilet rammer klodsen **vandret og midt på klodsen**, så vognen ikke vipper eller drejer.
- Mål vognens fart $u$ lige efter skuddet med fotocelle B.

### Beregning

Bevægelsesmængden er bevaret under selve skuddet:

$$m_p \cdot v_p = (M + m_p) \cdot u \quad\Longrightarrow\quad v_p = \frac{(M + m_p) \cdot u}{m_p}$$

- Beregn projektilets fart $v_p$ ud fra dine målinger.
- Beregn den kinetiske energi lige før ($\tfrac{1}{2} m_p v_p^2$) og lige efter ($\tfrac{1}{2}(M + m_p)u^2$). Hvor mange procent tabes?
- Sammenlign $v_p$ med fabrikantens opgivne mundingsfart, hvis den kendes. Det vil ofte ligge i størrelsesordenen 100–200 m/s, men tjek databladet for dit gevær og din projektiltype.

## Databehandling (Excel)

Lav et regneark med **en række pr. måling**. Tabellens første kolonne er **overskrifterne** i regnearket: skriv dem i række 2 (A2, B2, C2 osv.), og skriv hver måling i sin egen række nedenunder (række 3, 4, 5 osv.). Fx kan række 3 være forsøg 1a, række 4 forsøg 1b og række 5 forsøg 2.

| Kolonne overskrift | Indhold |
|---|---|
| $m_1$, $m_2$ | Vognenes masser (kg) |
| $\ell$ | Strimlens længde (m) |
| $\Delta t_1$ før, $\Delta t_1$ efter, $\Delta t_2$ efter | Målt tid for hver passage (s) |
| $v_1$, $u_1$, $u_2$ | $\ell / \Delta t$ med fortegn (m/s) |
| $p_{\text{før}}$ | $m_1 \cdot v_1 + m_2 \cdot v_2$ |
| $p_{\text{efter}}$ | $m_1 \cdot u_1 + m_2 \cdot u_2$ |
| $E_{\text{før}}$ | $\tfrac{1}{2} m_1 v_1^2 + \tfrac{1}{2} m_2 v_2^2$ |
| $E_{\text{efter}}$ | $\tfrac{1}{2} m_1 u_1^2 + \tfrac{1}{2} m_2 u_2^2$ |
| $\dfrac{p_{\text{efter}}}{p_{\text{før}}}$ | Kvotient, skal ligge tæt på 1 |
| $\dfrac{E_{\text{efter}}}{E_{\text{før}}}$ | Elastisk: tæt på 1. Uelastisk: tydeligt under 1 |

Husk at det der står her nedad i kolonnen skal være **overskrifter** i dit regneark. 

|Forsøg|$m_1$|$m_2$|$\Delta t_1$|$v_1$|...|$\dfrac{E_{\text{efter}}}{E_{\text{før}}}$ |
|---|---|---|---|---|---|---|
|1a) elastisk stød 1|||||||
|1b) elastisk stød 2|||||||
|2) uelastisk stød|||||||
|3) luftgevær|||||||

## Spørgsmål til journalen

1. **Bevarelse:** Er bevægelsesmængden bevaret i alle tre forsøg inden for måleusikkerheden? Hvor stor er afvigelsen i procent?
2. **Energi:** Hvilke stød er elastiske, og hvilke er uelastiske ud fra kvotienten $E_{\text{efter}}/E_{\text{før}}$? Hvor blev energien af i de uelastiske stød?
3. **Hypotesen:** Passer de målte $u_1$ og $u_2$ i forsøg 1a og 1b med formlerne? Hvad sker der med den lette vogn i 1b, og hvorfor?
4. **Usikkerhed:** Skriv, hvad usikkerheden på $v$ er. Overvej, hvor stor betydning usikkerheden på $\ell$ (længden på skydelæren) og på $\Delta t$ (fotocellen) har.
5. **Virker modellen?:** Bevarelsessætningen kræver et lukket system uden ydre kræfter langs banen. Diskutér, hvor godt det gælder her:
   - Restgnidning i luftpuden og luftmodstand
   - Banen er ikke helt vandret
   - Strimlens 10 cm måler en gennemsnitsfart over strimlen, ikke farten i selve stødet
   - Fjederbøjlerne er ikke perfekt elastiske, og velcro sikrer måske ikke, at vognene hænger helt sammen
   - Forsøg 3: projektilet rammer ikke nøjagtigt vandret og midt på klodsen, og noget af projektilets bevægelsesmængde kan gå til at få vognen til at vippe
6. **Forsøg 3:** Hvorfor er næsten hele den kinetiske energi tabt, selv om bevægelsesmængden er bevaret? Kan du bruge energibevarelse i stedet for bevarelse af bevægelsesmængde til at finde $v_p$? Begrund svaret.
