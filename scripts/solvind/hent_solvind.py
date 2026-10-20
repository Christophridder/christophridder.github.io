#!/usr/bin/env python3
"""Hent solvinddata til static/data/solvind/solvind.json (bruges af static/solvind.html).

Eksempler (kør fra crsite-roden):
    python3 scripts/solvind/hent_solvind.py noaa                 # seneste 7 døgn, 10-min middel
    python3 scripts/solvind/hent_solvind.py omni 2025-03-01 109  # 109 døgn (≈4 solrotationer), timeværdier

Kilder:
    noaa: NOAA SWPC realtid (DSCOVR/ACE ved L1)
          https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json
    omni: NASA OMNI2, timeværdier fra 1963 og frem (årsfiler)
          https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni2_<år>.dat
          Kolonner (1-indekseret): 1 år, 2 dag i året, 3 time, 24 protontæthed [cm^-3], 25 hastighed [km/s].
          Fyldværdier: tæthed 999.9, hastighed 9999.
"""
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

UD = Path("static/data/solvind/solvind.json")
NOAA = [  # prøves i rækkefølge
    "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind.json",
    "https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json",
]
OMNI = "https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni2_{aar}.dat"


def hent(url):
    print("Henter", url)
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def noaa():
    rows = None
    for url in NOAA:
        try:
            rows = json.loads(hent(url))
            break
        except Exception as e:  # noqa: BLE001
            print("  fejl:", e)
    if not rows:
        sys.exit("Kunne ikke hente fra NOAA.")
    h = rows[0]
    iT, iN, iV = h.index("time_tag"), h.index("density"), h.index("speed")
    bins = {}
    for row in rows[1:]:
        try:
            t = datetime.fromisoformat(row[iT].replace(" ", "T").replace("Z", "")).replace(tzinfo=timezone.utc)
            v, n = float(row[iV]), float(row[iN])
        except (TypeError, ValueError):
            continue
        k = int(t.timestamp() // 600)
        b = bins.setdefault(k, [0.0, 0.0, 0])
        b[0] += v; b[1] += n; b[2] += 1
    keys = sorted(bins)
    t = [datetime.fromtimestamp(k * 600 + 300, timezone.utc) for k in keys]
    return t, [bins[k][0] / bins[k][2] for k in keys], [bins[k][1] / bins[k][2] for k in keys], \
        "NOAA SWPC, 10-min middel"


def omni_linjer(tekst):
    for linje in tekst.splitlines():
        f = linje.split()
        if len(f) < 25:
            continue
        aar, doy, time = int(f[0]), int(f[1]), int(f[2])
        n, v = float(f[23]), float(f[24])
        t = datetime(aar, 1, 1, tzinfo=timezone.utc) + timedelta(days=doy - 1, hours=time)
        yield t, (None if v >= 9999 else v), (None if n >= 999.9 else n)


def omni(start, dage):
    t0 = datetime.fromisoformat(start).replace(tzinfo=timezone.utc)
    t1 = t0 + timedelta(days=dage)
    T, V, N = [], [], []
    for aar in range(t0.year, t1.year + 1):
        for t, v, n in omni_linjer(hent(OMNI.format(aar=aar))):
            if t0 <= t < t1 and v is not None and n is not None:
                T.append(t); V.append(v); N.append(n)
    return T, V, N, f"NASA OMNI2, timeværdier fra {start}"


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("noaa", "omni"):
        sys.exit(__doc__)
    if sys.argv[1] == "noaa":
        t, v, n, kilde = noaa()
    else:
        start = sys.argv[2] if len(sys.argv) > 2 else "2025-03-01"
        dage = float(sys.argv[3]) if len(sys.argv) > 3 else 109
        t, v, n, kilde = omni(start, dage)
    if len(t) < 10:
        sys.exit(f"For få datapunkter ({len(t)}) – tjek periode/kilde.")
    # fornuftstjek: solvind ligger typisk 250–900 km/s
    vmin, vmax = min(v), max(v)
    if vmin < 150 or vmax > 3000:
        print(f"ADVARSEL: hastighed {vmin:.0f}–{vmax:.0f} km/s ser forkert ud – tjek kolonner.")
    UD.parent.mkdir(parents=True, exist_ok=True)
    UD.write_text(json.dumps({
        "kilde": kilde,
        "t": [x.strftime("%Y-%m-%dT%H:%M:%SZ") for x in t],
        "v": [round(x, 1) for x in v],
        "n": [round(x, 2) for x in n],
    }), encoding="utf-8")
    print(f"Skrev {UD}: {len(t)} punkter, v = {vmin:.0f}–{vmax:.0f} km/s, n = {min(n):.1f}–{max(n):.1f} cm^-3")


if __name__ == "__main__":
    main()
