"""Laver eksempel-lydfiler (WAV, 44100 Hz, 16 bit mono) til lydanalyse.html.

Samme syntese som eksempellydene inde i programmet.
Kør fra crsite-mappen:  python3 scripts/lydanalyse/lav_demolyde.py
Filerne lægges i static/lyd/lydanalyse/
"""
from pathlib import Path
import numpy as np
from scipy.io import wavfile

FS = 44100
UD = Path(__file__).resolve().parents[2] / "static" / "lyd" / "lydanalyse"

# dele: (frekvens, amplitude, henfaldstid tau i s eller None = vedvarende)
DEMOS = {
    "stemmegaffel_440Hz": dict(dur=3, att=0.005, dele=[(440, 1, 2.5)]),
    "klarinet_220Hz": dict(dur=3, att=0.06, dele=[(220, 1, None), (440, .04, None), (660, .55, None),
        (880, .03, None), (1100, .38, None), (1320, .02, None), (1540, .22, None), (1760, .02, None),
        (1980, .12, None), (2420, .07, None)]),
    "trompet_466Hz": dict(dur=3, att=0.04, dele=[(466.2 * n, a, None) for n, a in
        zip(range(1, 11), [.55, 1, .8, .6, .42, .28, .18, .11, .07, .04])]),
    "guitar_110Hz": dict(dur=3, att=0.003, dele=[(110 * n, 1 / n, 2.5 / (1 + 0.4 * (n - 1))) for n in range(1, 13)]),
    "sang_stemmeA_262Hz": dict(dur=3, att=0.08, dele=[(262 * n, a, None) for n, a in
        zip(range(1, 8), [1, .7, .45, .12, .08, .05, .03])]),
    "sang_stemmeB_262Hz": dict(dur=3, att=0.08, dele=[(262 * n, a, None) for n, a in
        zip(range(1, 9), [.45, .35, .5, .8, 1, .55, .3, .15])]),
    "metalroer_4slag": dict(dur=3.2, att=0.002, slag=[0, 0.8, 1.6, 2.4], dele=[(523.3, 1, 1.2),
        (523.3 * 2.756, .6, .5), (523.3 * 5.404, .35, .25), (523.3 * 8.933, .2, .12)]),
    "svaevning_440_443Hz": dict(dur=4, att=0.05, dele=[(440, 1, None), (443, 1, None)]),
}


def syntese(d):
    n = round(d["dur"] * FS)
    x = np.zeros(n)
    i = np.arange(n)
    for f, a, tau in d["dele"]:
        for ts in d.get("slag", [0]):
            i0 = round(ts * FS)
            t = (i[i0:] - i0) / FS
            env = np.minimum(1, t / d["att"])
            if tau:
                env = env * np.exp(-t / tau)
            else:
                env = env * np.minimum(1, (d["dur"] - i[i0:] / FS) / 0.05)
            x[i0:] += a * env * np.sin(2 * np.pi * f * t)
    rng = np.random.default_rng(1)
    x = 0.8 * x / np.abs(x).max() + 0.002 * rng.uniform(-1, 1, n)
    return x


if __name__ == "__main__":
    UD.mkdir(parents=True, exist_ok=True)
    for navn, d in DEMOS.items():
        wavfile.write(UD / f"{navn}.wav", FS, np.int16(np.clip(syntese(d), -1, 1) * 32767))
        print("skrev", UD / f"{navn}.wav")
