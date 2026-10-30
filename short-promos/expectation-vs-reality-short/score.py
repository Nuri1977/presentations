#!/usr/bin/env python3
"""Original score and sound design for motion.html (22 s, "Setting up dbt: Expectation vs. Reality"), numpy only.

    python score.py             -> score.wav (48 kHz stereo, loudness-normalized to -14 LUFS)

120 BPM, one bar = 2 s. Every cue time below comes from the timeline in motion.html (T, LINES, STEPS).
If you retime the video, move the matching cue here and re-run; render.mjs muxes score.wav into the MP4.
Three moods: a bright, bouncy jingle for the expectation, the same jingle warping and crushing as the
terminal falls apart, then a laid-back half-time groove with electric piano for the Rosetta walkthrough.
Instruments are the same synths as rosetta-dbt-studio-15sec/score.py plus an electric piano and a marker squeak.
"""
import os
import re
import subprocess
import wave

import numpy as np

SR = 48000
DUR = 22.0
N = int(SR * DUR)
HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(31)

BEAT = 0.5
BAR = 4 * BEAT
SIX = BEAT / 4      # a 16th note
T_SPLIT = 2.0       # split screen (motion.html T.split)
T_NOPE = 7.0        # marker scribble + "NOPE." (T.nope)
T_OPT3 = 7.4        # "...or there's option 3" (T.opt3)
T_DROP = 8.0        # Rosetta walkthrough starts (T.drop)
T_END = 18.0        # "EXPECTATION:" (T.end)
T_MET = 18.5        # "MET." stamp (T.met)
T_LOCK = 19.0       # logo lockup (T.lock)
E_TICKS = [2.5 + i * 0.5 for i in range(5)]                       # expectation checkboxes (E_TICK)
ERR_LINES = [2.70, 3.75, 4.75, 4.95, 5.25, 5.95, 6.80]            # red terminal lines (LINES)
CMD_LINES = [2.30, 3.40, 4.10, 4.45, 5.70, 6.25, 6.55]            # "$ ..." terminal lines
STEP_T0 = [8.0, 9.5, 11.5, 13.5, 15.0, 16.5]                      # STEPS[i].t0
STEP_TICK = [t - 0.3 for t in STEP_T0[1:] + [18.0]]               # chip ticks (TICK)
RINGS = [8.6, 11.75, 12.75, 13.9, 15.55, 17.0]                    # highlight rings


# ---------------------------------------------------------------- basics
def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tt(n):
    return np.arange(n) / SR


def S(sec):
    return int(round(sec * SR))


def pan2(sig, pan):
    th = (np.clip(pan, -1, 1) + 1) * np.pi / 4
    return np.stack([sig * np.cos(th), sig * np.sin(th)]) * np.sqrt(2)


class Bus:
    def __init__(self):
        self.x = np.zeros((2, N))

    def add(self, sig, t0, pan=0.0, gain=1.0):
        s = pan2(sig, pan) if sig.ndim == 1 else sig
        s = s * gain
        i0 = S(t0)
        j0, j1 = max(i0, 0), min(i0 + s.shape[1], N)
        if j1 > j0:
            self.x[:, j0:j1] += s[:, j0 - i0:j1 - i0]



drums, bass, keys, fx, ui, bells = (Bus() for _ in range(6))
happy = Bus()                     # the 0-7 s jingle, kept apart so it can warp and crush
send_s, send_l = Bus(), Bus()     # short room / long hall


def put(bus, sig, t0, pan=0.0, gain=1.0, rs=0.0, rl=0.0):
    bus.add(sig, t0, pan, gain)
    if rs:
        send_s.add(sig, t0, pan, gain * rs)
    if rl:
        send_l.add(sig, t0, pan, gain * rl)


def put_sweep(bus, sig, t0, p0, p1, gain=1.0, rs=0.0, rl=0.0):
    th = (np.linspace(p0, p1, len(sig)) + 1) * np.pi / 4
    st = np.stack([sig * np.cos(th), sig * np.sin(th)]) * np.sqrt(2)
    put(bus, st, t0, gain=gain, rs=rs, rl=rl)


# ---------------------------------------------------------------- filters
def fft_filter(x, gain_fn):
    n = len(x)
    nfft = 1 << (n + 2048 - 1).bit_length()
    X = np.fft.rfft(x, nfft)
    f = np.fft.rfftfreq(nfft, 1 / SR)
    return np.fft.irfft(X * gain_fn(f), nfft)[:n]


def lp(fc, order=2):
    return lambda f: 1 / np.sqrt(1 + (f / fc) ** (2 * order))


def hp(fc, order=2):
    return lambda f: 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order))


def bp(fc, width_oct=0.8):
    return lambda f: np.exp(-0.5 * (np.log2(np.maximum(f, 1) / fc) / width_oct) ** 2)


def stft_filter(x, mask_fn, frame=2048, hop=512):
    """Time-varying filter: mask_fn(t_seconds[:,None], freqs[None,:]) -> gain."""
    n = len(x)
    win = np.hanning(frame)
    xp = np.concatenate([np.zeros(frame), x, np.zeros(2 * frame)])
    nf = (len(xp) - frame) // hop + 1
    idx = np.arange(frame)[None, :] + hop * np.arange(nf)[:, None]
    F = np.fft.rfft(xp[idx] * win, axis=1)
    freqs = np.fft.rfftfreq(frame, 1 / SR)
    tc = (hop * np.arange(nf) + frame / 2 - frame) / SR
    yf = np.fft.irfft(F * mask_fn(tc[:, None], freqs[None, :]), frame, axis=1) * win
    y = np.zeros(len(xp))
    ws = np.zeros(len(xp))
    for i in range(nf):
        y[i * hop:i * hop + frame] += yf[i]
        ws[i * hop:i * hop + frame] += win ** 2
    return (y / np.maximum(ws, 1e-6))[frame:frame + n]


# ---------------------------------------------------------------- instruments
def saw(f, n, fc, fc_t=None, kmax=48, coherent=False):
    """Band-limited additive saw with a (optionally time-varying) 12 dB/oct low-pass baked in."""
    t = tt(n)
    top = fc if fc_t is None else float(np.max(fc_t))
    K = max(1, int(min(kmax, 3.2 * top / f, 17000 / f)))
    w = 2 * np.pi * f * t
    out = np.zeros(n)
    ph = rng.random() * 2 * np.pi
    for k in range(1, K + 1):
        g = 1 / np.sqrt(1 + (k * f / (fc if fc_t is None else fc_t)) ** 4)
        pk = k * ph if coherent else rng.random() * 2 * np.pi
        out += g * np.sin(k * w + pk) / k
    return out


def env_ar(n, a, r, hold):
    t = tt(n)
    e = np.minimum(1.0, t / a) if a > 0 else np.ones(n)
    rel = np.clip((t - hold) / r, 0, 1)
    return e * (1 - rel) ** 2


def pad_chord(notes, dur, fc, a=0.05, r=0.4, fc_t=None, detune=(-12, 0, 12), spread=0.7):
    n = S(dur)
    out = np.zeros((2, n))
    pans = np.linspace(-spread, spread, len(detune))
    for m in notes:
        for d, p in zip(detune, pans):
            v = saw(midi(m) * 2 ** (d / 1200), n, fc, fc_t)
            out += pan2(v, p)
    out /= np.sqrt(len(notes) * len(detune))
    return out * env_ar(n, a, r, dur - r)


def pluck(f, dur=0.45, bright=1.0):
    n = S(dur)
    t = tt(n)
    out = np.zeros(n)
    K = int(min(36, 14000 / f))
    for k in range(1, K + 1):
        out += np.sin(2 * np.pi * k * f * t + rng.random() * 0.4) / k * np.exp(-t * (5 + (k - 1) * 3.2 / bright))
    return out * np.clip(t / 0.002, 0, 1) * 0.6


def bell(f, dur=1.8, idx=2.2, ratio=3.5, decay=0.8):
    t = tt(S(dur))
    I = idx * np.exp(-t / 0.22)
    y = np.sin(2 * np.pi * f * t + I * np.sin(2 * np.pi * ratio * f * t)) * np.exp(-t / decay)
    y += 0.25 * np.sin(2 * np.pi * 2.0 * f * t) * np.exp(-t / (decay * 0.45))
    return y * np.clip(t / 0.002, 0, 1) * 0.5


def pop(f, dur=0.12):
    t = tt(S(dur))
    fi = f * (1 + 1.0 * np.exp(-t / 0.01))
    return np.sin(2 * np.pi * np.cumsum(fi) / SR) * np.exp(-t / 0.032) * np.clip(t / 0.001, 0, 1)


def kick(dur=0.55):
    t = tt(S(dur))
    f = 46 + 120 * np.exp(-t / 0.032)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.3)
    click = fft_filter(rng.standard_normal(len(t)), bp(3500, 1.0)) * np.exp(-t / 0.004)
    return np.tanh(1.6 * (body + 0.18 * click)) / np.tanh(1.6)


def clap(dur=0.45):
    n = S(dur)
    t = tt(n)
    x = fft_filter(rng.standard_normal(n), bp(1600, 0.9))
    e = np.zeros(n)
    for ti in (0.0, 0.009, 0.019):
        e += (t >= ti) * np.exp(-np.maximum(t - ti, 0) / 0.005)
    e += (t >= 0.026) * np.exp(-np.maximum(t - 0.026, 0) / 0.13) * 0.8
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.05) * 0.3
    return (x / np.max(np.abs(x)) * e + body) * 0.8


HAT_BANK = [fft_filter(rng.standard_normal(S(0.3)), hp(7500, 2)) for _ in range(4)]


def hat(decay=0.03, v=0):
    x = HAT_BANK[v % 4]
    t = tt(len(x))
    return x / np.max(np.abs(x)) * np.exp(-t / decay)


def crash(dur=2.4):
    n = S(dur)
    t = tt(n)
    out = np.zeros((2, n))
    for c in range(2):
        x = fft_filter(rng.standard_normal(n), hp(3200, 2))
        x /= np.max(np.abs(x))
        metal = sum(np.sin(2 * np.pi * f * t + rng.random() * 6) for f in (3120, 4470, 5330, 6810)) * 0.12
        out[c] = (x + metal) * np.exp(-t / 0.85) * np.clip(t / 0.002, 0, 1)
    return out


def rev_crash(dur=1.0):
    c = crash(dur + 0.2)[:, :S(dur)]
    c = c[:, ::-1]
    return c * (np.linspace(0, 1, c.shape[1]) ** 2)


def boom(dur=2.4, f0=70, f1=29):
    t = tt(S(dur))
    f = f1 + (f0 - f1) * np.exp(-t / 0.28)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.95)
    y += 0.5 * fft_filter(rng.standard_normal(len(t)), lp(700, 2)) * np.exp(-t / 0.1)
    return np.tanh(1.4 * y) / np.tanh(1.4)


def tom(f, dur=0.35):
    t = tt(S(dur))
    fi = f * (1 + 0.6 * np.exp(-t / 0.018))
    return np.sin(2 * np.pi * np.cumsum(fi) / SR) * np.exp(-t / 0.14)


def whoosh(dur, peak_at, f0, f1, f2, width=0.9):
    n = S(dur)
    x = rng.standard_normal(n)

    def mask(tc, f):
        u = np.clip(tc / dur, 0, 1)
        fc = np.where(u < peak_at, f0 * (f1 / f0) ** (u / peak_at), f1 * (f2 / f1) ** ((u - peak_at) / (1 - peak_at + 1e-9)))
        return np.exp(-0.5 * (np.log2(np.maximum(f, 1) / fc) / width) ** 2)

    y = stft_filter(x, mask)
    u = tt(n) / dur
    e = np.where(u < peak_at, (u / peak_at) ** 2.4, np.exp(-((u - peak_at) / (1 - peak_at + 1e-9)) * 4.5))
    y = y * e
    return y / (np.max(np.abs(y)) + 1e-9)


def riser(dur, f0=300, f1=8000):
    return whoosh(dur, 0.985, f0, f1, f1, width=0.7)


def click():
    t = tt(S(0.06))
    x = fft_filter(rng.standard_normal(len(t)), bp(3800, 0.6)) * np.exp(-t / 0.005)
    x = x / np.max(np.abs(x))
    return x + 0.6 * np.sin(2 * np.pi * 1900 * t) * np.exp(-t / 0.012)


def tick():
    t = tt(S(0.03))
    x = fft_filter(rng.standard_normal(len(t)), bp(rng.uniform(2600, 5200), 0.5)) * np.exp(-t / 0.0028)
    return x / np.max(np.abs(x))


def bloop(f):
    t = tt(S(0.3))
    fi = f * (0.6 + 0.8 * (1 - np.exp(-t / 0.03)))
    y = np.sin(2 * np.pi * np.cumsum(fi) / SR) * np.exp(-t / 0.09)
    n = fft_filter(rng.standard_normal(len(t)), bp(2400, 0.8)) * np.exp(-t / 0.05)
    return y + 0.25 * n / np.max(np.abs(n))


def glitch(dur=0.28):
    t = tt(S(dur))
    sq = np.sign(np.sin(2 * np.pi * 110 * t)) * 0.6 + np.sign(np.sin(2 * np.pi * 233 * t)) * 0.35
    gate = (np.floor(t / 0.019) % 3 != 1).astype(float)
    y = fft_filter(np.round(sq * gate * 3) / 3, lp(2600, 2)) * np.exp(-t / 0.22)
    return y / np.max(np.abs(y))


def glitter(t0, t1, count, fmin, fmax, gain, p0=-0.8, p1=0.8, curve=1.0):
    for k in range(count):
        u = (k / max(1, count - 1)) ** curve
        tk = t0 + (t1 - t0) * u + rng.uniform(-0.01, 0.01)
        put(ui, pop(rng.uniform(fmin, fmax), 0.07), tk, pan=np.clip(p0 + (p1 - p0) * u + rng.uniform(-0.2, 0.2), -1, 1),
            gain=gain * rng.uniform(0.6, 1.0), rl=0.6)



def epiano(f, dur=0.9):
    """FM electric piano: soft bell-like body plus a short tine click."""
    n = S(dur)
    t = tt(n)
    idx = 1.6 * np.exp(-t / 0.3) + 0.25
    y = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t)) * np.exp(-t / 1.1)
    y += 0.12 * np.sin(2 * np.pi * f * 14 * t) * np.exp(-t / 0.018)
    return y * np.clip(t / 0.003, 0, 1) * np.clip((dur - t) / 0.06, 0, 1) * 0.5


def epi_chord(notes, dur=0.9):
    out = np.zeros((2, S(dur)))
    for k, m in enumerate(notes):
        out += pan2(epiano(midi(m), dur), -0.4 + 0.8 * k / max(1, len(notes) - 1))
    return out / np.sqrt(len(notes))


def marimba(f, dur=0.45):
    return bell(f, dur, idx=1.1, ratio=4.0, decay=0.16)


def strum(notes, dur=0.35):
    """Ukulele-ish strum: bright plucks, each string a hair later than the last."""
    gap = S(0.012)
    out = np.zeros(S(dur) + gap * len(notes))
    for k, m in enumerate(notes):
        p = pluck(midi(m), dur, bright=1.6)
        out[k * gap:k * gap + len(p)] += p
    return out / np.sqrt(len(notes))


def bass_note(f, dur=0.3):
    n = S(dur)
    t = tt(n)
    y = saw(f, n, 700, fc_t=220 + 1100 * np.exp(-t / 0.06)) * 0.6 + np.sin(2 * np.pi * f * t) * 1.0
    return np.tanh(1.3 * y) * env_ar(n, 0.005, 0.08, dur - 0.08)


def error_beep():
    """Two-tone 'nope' beep, falling."""
    out = []
    for f, d in ((523, 0.07), (392, 0.12)):
        t = tt(S(d))
        sq = np.sign(np.sin(2 * np.pi * f * t))
        out.append(fft_filter(sq, lp(3500, 2)) * np.clip((d - t) / 0.01, 0, 1) * np.clip(t / 0.002, 0, 1))
    return np.concatenate(out) * 0.6


def squeak(dur, f):
    """One stroke of a felt marker: narrow-band noise that bends upward."""
    n = S(dur)
    x = rng.standard_normal(n)
    y = stft_filter(x, lambda tc, fr: np.exp(-0.5 * (np.log2(np.maximum(fr, 1) / (f * (1 + 0.6 * np.clip(tc / dur, 0, 1)))) / 0.18) ** 2), frame=512, hop=128)
    u = tt(n) / dur
    return y / (np.max(np.abs(y)) + 1e-9) * np.sin(np.pi * np.clip(u, 0, 1)) ** 0.6


def warp(x, t0, t1, sag=0.0148, wob=0.0016, crush_from=5.5):
    """The jingle falls apart: pitch sags and warbles, then gets bit-crushed."""
    i0, i1 = S(t0), S(t1)
    n = np.arange(i1 - i0)
    tc = n / SR
    u = tc / (t1 - t0)
    delay = sag * tc ** 2 + wob * u * np.sin(2 * np.pi * 6 * tc)
    pos = i0 + n - delay * SR
    y = x.copy()
    for c in range(2):
        y[c, i0:i1] = np.interp(pos, np.arange(x.shape[1]), x[c])
    c0 = S(crush_from)
    m = i1 - c0
    k = np.arange(m) / m
    hold = np.maximum(1, np.round(1 + 9 * k)).astype(int)
    levels = 2.0 ** (12 - 8 * k)
    idx = np.arange(m)
    held = c0 + idx - (idx % hold)
    for c in range(2):
        seg = np.round(y[c, held] * levels) / levels
        y[c, c0:i1] = y[c, c0:i1] * (1 - k) + seg * k
    return y


# =================================================================== ARRANGEMENT
C = ([60, 64, 67, 72], 36)
G = ([59, 62, 67, 71], 31)
A = ([57, 60, 64, 69], 33)
F = ([57, 60, 65, 69], 29)
MEL = [0, 1, 2, 1, 0, 1, 3, 2]

# ---------- 0.0-7.0  the happy jingle (expectation), which then breaks
for b, (ch, root) in enumerate([C, G, A, F]):
    tb = b * BAR
    for s in range(4):   # bouncy staccato bass, octave hops
        put(happy, pluck(midi(root + [0, 12, 7, 12][s]), 0.22, bright=0.7), tb + s * BEAT, gain=0.42 if tb >= T_SPLIT else 0.3)
        put(happy, strum([m + 12 if m < 64 else m for m in ch], 0.3), tb + s * BEAT + 0.25, pan=0.25, gain=0.2)
    for s in range(8):   # marimba melody, eighths
        put(happy, marimba(midi(ch[MEL[s]] + 12)), tb + s * 0.25, pan=-0.3, gain=0.26)
    if tb >= T_SPLIT:
        for s in (0, 2):
            put(happy, kick(), tb + s * BEAT, gain=0.62)
        for s in (1, 3):
            put(happy, clap(0.3), tb + s * BEAT, gain=0.32)
        for s in range(16):
            put(happy, hat(0.018, s), tb + s * SIX + (0.02 if s % 2 else 0), pan=0.35, gain=0.05 + 0.04 * (s % 2 == 0))
# title words
for tc in (0.5, 1.5):
    put(happy, clap(0.3), tc, gain=0.22)
for i, tw in enumerate([0.1, 0.25, 0.5, 0.75]):
    put(ui, pop(midi([72, 76, 79, 84][i])), tw, gain=0.3, rl=0.4)
put(bells, bell(midi(84), 0.9, decay=0.4), 1.0, gain=0.18, rl=0.5)       # EXPECTATION
put(ui, tick(), 1.25, gain=0.3)                                           # vs.
put(ui, error_beep(), 1.5, gain=0.25)                                     # REALITY
put_sweep(fx, whoosh(0.45, 0.6, 300, 3000, 800), T_SPLIT - 0.3, -0.7, 0.7, gain=0.22)   # halves slide in
for tw in (2.2, 2.3):
    put(drums, tom(170, 0.25), tw, gain=0.35, rs=0.3)                     # stamps
# expectation ticks: satisfying rising dings, then the "Done in 5 minutes" chime
for i, te in enumerate(E_TICKS):
    put(bells, bell(midi([84, 86, 88, 91, 96][i]), 0.8, decay=0.35), te, pan=-0.4, gain=0.16, rl=0.5)
put(bells, bell(midi(91), 1.2, decay=0.5), 5.0, pan=-0.3, gain=0.14, rl=0.6)
put(bells, bell(midi(96), 1.2, decay=0.5), 5.08, pan=-0.3, gain=0.1, rl=0.6)
# reality: typing on every command, a nope-beep on every error, a clock that speeds up
for tc in CMD_LINES:
    for k in range(5):
        put(ui, click(), tc - 0.2 + k * 0.035 + rng.uniform(0, 0.01), pan=0.35, gain=0.1)
for i, te in enumerate(ERR_LINES):
    put(ui, error_beep(), te, pan=0.3, gain=0.17 + 0.03 * i)
    put(ui, glitch(0.12), te, pan=0.3, gain=0.06 + 0.03 * i)
tk = 2.3
while tk < 6.95:
    put(drums, tick(), tk, pan=0.5, gain=0.13 + 0.12 * (tk - 2.3) / 4.6)
    tk += 0.5 + (0.07 - 0.5) * ((tk - 2.3) / 4.6) ** 1.2

# ---------- 7.0-8.0  NOPE, "...or there's option 3", silence, drop
for k in range(9):
    put(fx, squeak(0.034, 2400 if k % 2 else 3200), T_NOPE + k * 0.035, pan=-0.5 + k * 0.12, gain=0.3)
put(fx, boom(1.0, 90, 40), T_NOPE + 0.22, gain=0.55)
put(drums, clap(), T_NOPE + 0.22, gain=0.45, rl=0.4)
put_sweep(fx, whoosh(0.4, 0.55, 260, 2400, 600), T_OPT3, 0.0, 0.0, gain=0.25)
put(fx, riser(0.5, 500, 10000), T_OPT3 + 0.05, gain=0.2, rl=0.4)
put(fx, rev_crash(0.5), T_OPT3 + 0.05, gain=0.2)
put(bells, bell(midi(79), 1.0, decay=0.45), T_OPT3 + 0.1, gain=0.16, rl=0.6)
put(ui, pop(midi(91)), T_OPT3 + 0.3, gain=0.4, rl=0.5)                  # the "3"
put(bells, bell(midi(91), 1.0, decay=0.4), T_OPT3 + 0.3, gain=0.14, rl=0.6)

# ---------- 8.0-18.0  the walkthrough: laid-back half-time groove, electric piano
kicks = []


def groove(t0, bars, chords, light=False):
    for b in range(bars):
        tb = t0 + b * BAR
        ch, root = chords[b % len(chords)]
        for s in (0, 6, 10):
            put(drums, kick(), tb + s * SIX, gain=0.75)
            kicks.append(tb + s * SIX)
        for s in (4, 12):
            put(drums, clap(), tb + s * SIX, gain=0.5, rs=0.35)
        for s in range(16):
            swing = 0.035 if s % 2 else 0.0
            if s == 14:
                put(drums, hat(0.12, b), tb + s * SIX, pan=0.3, gain=0.13)
            elif s % 2 == 0 or not light:
                put(drums, hat(0.025, s + b), tb + s * SIX + swing, pan=-0.25, gain=0.13 if s % 2 == 0 else 0.05)
        for s, iv, d in ((0, 0, 0.55), (6, 0, 0.3), (10, 7, 0.45), (14, 12, 0.2)):
            put(bass, bass_note(midi(root + 12 + iv), d), tb + s * SIX, gain=0.5)
        put(keys, epi_chord([m - 12 for m in ch], 1.0), tb, gain=0.5, rl=0.3)
        for s in (7, 11):
            put(keys, epi_chord(ch, 0.25), tb + s * SIX, gain=0.3, rs=0.3)


put(fx, boom(2.4, 85, 30), T_DROP, gain=0.85)
put(fx, crash(2.2), T_DROP, gain=0.28, rl=0.6)
put(drums, tom(170, 0.25), T_DROP + 0.02, gain=0.35)                     # REALITY stamp
groove(T_DROP, 5, [C, A, F, G, C])
for i, tc in enumerate(STEP_T0[1:]):   # carousel swipe on every step
    put_sweep(fx, whoosh(0.32, 0.6, 400, 4200, 900), tc - 0.2, 0.6, -0.6, gain=0.22)
for i, tt_ in enumerate(STEP_TICK):     # chip ticks climb a pentatonic
    put(bells, bell(midi([84, 86, 88, 91, 93, 96][i]), 0.9, decay=0.35), tt_, pan=0.3, gain=0.17, rl=0.5)
    put(ui, pop(midi([84, 86, 88, 91, 93, 96][i])), tt_, gain=0.22)
for tr in RINGS:
    put(ui, pop(midi(100), 0.08), tr, gain=0.14, rl=0.4)
for k in range(9):                      # typing "northwind"
    put(ui, click(), 9.85 + k * 0.06, pan=0.1, gain=0.16)
for tc in (11.05, 12.05):               # Save, then PostgreSQL
    put(ui, click(), tc, gain=0.3)
    put(ui, bloop(900), tc, gain=0.12)
put(fx, rev_crash(0.5), 17.5, gain=0.18)

# ---------- 18.0-22.0  EXPECTATION: MET.
put_sweep(fx, whoosh(0.35, 0.5, 300, 3000, 700), T_END, 0.0, 0.0, gain=0.2)
put(drums, tom(150, 0.3), T_END + 0.2, gain=0.4, rs=0.3)                  # "EXPECTATION:"
put(fx, boom(2.6, 90, 30), T_MET, gain=0.95)                              # "MET."
put(fx, crash(2.6), T_MET, gain=0.3, rl=0.7)
put(drums, clap(), T_MET, gain=0.5, rl=0.5)
put(keys, pad_chord([48, 55, 60, 64, 67, 72], 3.4, 3200, a=0.01, r=1.6), T_MET, gain=0.2, rl=0.4)
put(keys, epi_chord([60, 64, 67, 72, 76], 2.0), T_MET, gain=0.4, rl=0.5)
for i, f in enumerate([190, 160, 135]):   # logo slabs land
    put(drums, tom(f, 0.3), T_LOCK + 0.06 * i + 0.24, gain=0.35, rs=0.4)
glitter(T_LOCK + 0.3, T_LOCK + 0.62, 5, 2000, 4000, 0.13)
groove(T_LOCK, 1, [C], light=True)
glitter(20.5, 21.25, 8, 2400, 4600, 0.12, curve=0.8)                      # shine sweep
put(keys, epi_chord([60, 64, 67, 71, 76], 1.6), 21.0, gain=0.4, rl=0.6)
put(bells, bell(midi(84), 2.0, decay=1.0), 21.0, gain=0.18, rl=0.7)
put(drums, kick(), 21.0, gain=0.7)
kicks.append(21.0)


# =================================================================== MIX
def sidechain(times, depth, rel=0.12):
    g = np.ones(N)
    for tk in times:
        i0 = S(tk)
        seg = tt(min(S(0.5), N - i0))
        g[i0:i0 + len(seg)] = np.minimum(g[i0:i0 + len(seg)], 1 - depth * np.exp(-seg / rel))
    return g


def make_ir(rt, lp_hz, pre):
    n = S(rt * 1.2)
    t = tt(n)
    ir = np.zeros((2, n + S(pre)))
    for c in range(2):
        x = rng.standard_normal(n) * np.exp(-6.9 * t / rt)
        x = fft_filter(x, lp(lp_hz, 1))
        ir[c, S(pre):] = x
    return ir / np.sqrt(np.sum(ir ** 2) / 2)


def convolve(x, ir):
    n = x.shape[1] + ir.shape[1]
    nfft = 1 << (n - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, nfft, axis=1) * np.fft.rfft(ir, nfft, axis=1), nfft, axis=1)
    return y[:, :N]


IR_S, IR_L = make_ir(0.9, 6000, 0.008), make_ir(2.6, 5000, 0.025)

# the jingle warps from 4.3 s and is cut by the marker at 7.0 s
jingle = warp(happy.x * 1.7, 4.3, T_NOPE)
cut = np.ones(N)
cut[S(T_NOPE):S(T_NOPE) + S(0.012)] = np.linspace(1, 0, S(0.012))
cut[S(T_NOPE) + S(0.012):] = 0
jingle *= cut

keys.x *= 1.6     # bus balance: electric piano and dings sit too low against the drums
bells.x *= 1.6
bass.x *= sidechain(kicks, 0.6, 0.1)
keys.x *= sidechain(kicks, 0.25)

wet_s = convolve(send_s.x, IR_S) * 0.35
wet_l = convolve(send_l.x, IR_L) * 0.35
mix = drums.x + bass.x + keys.x + fx.x + ui.x + bells.x + jingle + wet_s + wet_l
mix = np.stack([fft_filter(mix[c], hp(28, 2)) for c in range(2)])

fade = np.ones(N)
fs0 = S(DUR - 0.7)
fade[fs0:] = np.cos(np.linspace(0, np.pi / 2, N - fs0)) ** 2
fade[:S(0.004)] = np.linspace(0, 1, S(0.004))
mix *= fade


def limiter(x, ceiling=0.84, release=0.08, look=0.003):
    a = np.max(np.abs(x), axis=0)
    need = np.minimum(1.0, ceiling / np.maximum(a, 1e-9))
    w = S(look)
    need = np.lib.stride_tricks.sliding_window_view(np.concatenate([need, np.ones(w)]), w + 1).min(axis=1)
    g = np.empty(N)
    cur = 1.0
    r = np.exp(-1 / (release * SR))
    for i, v in enumerate(need):
        cur = v if v < cur else v + (cur - v) * r
        g[i] = cur
    return x * g


def write_wav(path, x):
    y = np.clip(x, -1, 1) * 32767 + (rng.random(x.shape) - rng.random(x.shape))
    y = np.clip(np.round(y), -32768, 32767).astype('<i2').T.copy()
    with wave.open(path, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


def ebur128(path):
    return subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-'],
                          capture_output=True, text=True).stderr


TARGET = -14.0
out = os.path.join(HERE, 'score.wav')
master = mix / np.max(np.abs(mix)) * 0.5
for _ in range(3):
    write_wav(out, limiter(master))
    log = ebur128(out)
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', log)[-1])
    tp = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', log)[-1])
    if abs(I - TARGET) < 0.3:
        break
    master *= 10 ** ((TARGET - I) / 20)
print(f'wrote {out}: {DUR:.1f}s, {I:.1f} LUFS, true peak {tp:.1f} dBTP')
for name, b, a0, a1 in (('jingle', jingle, 2.0, 4.3), ('drums', drums.x, 8.0, 18.0), ('bass', bass.x, 8.0, 18.0), ('keys', keys.x, 8.0, 18.0),
                        ('fx', fx.x, 0.0, 22.0), ('ui', ui.x, 0.0, 22.0), ('bells', bells.x, 0.0, 22.0)):
    seg = b[:, S(a0):S(a1)]
    print(f'  {name:6s} rms {20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-12):6.1f} dB ({a0:.0f}-{a1:.0f}s)   peak {20 * np.log10(np.max(np.abs(b)) + 1e-12):6.1f} dB')
M = [(float(a), float(b)) for a, b in re.findall(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)', log)]
for name, a, b in (('title', 0.0, 2.0), ('split', 2.0, 4.5), ('chaos', 4.5, 7.0), ('walk', 8.0, 18.0), ('end', 18.0, 21.3)):
    vals = [m for tm, m in M if a + 0.4 <= tm <= b]
    if vals:
        print(f'  {name:6s} momentary loudness {np.mean(vals):6.1f} LUFS (min {min(vals):6.1f}, max {max(vals):6.1f})')
