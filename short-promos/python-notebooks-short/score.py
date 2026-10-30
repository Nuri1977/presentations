#!/usr/bin/env python3
"""Original score and sound design for motion.html (22 s, Notebooks short), synthesized with numpy only.

    python score.py             -> score.wav (48 kHz stereo, loudness-normalized to -14 LUFS)

120 BPM, one bar = 2 s, in D major (Dmaj7 / Bm7 / Gmaj7 / A). Every cue time below comes from the timeline
in motion.html (SCN = [...] and the per-scene typing / click / reveal times). If you retime the video, move the
matching cue here and re-run; render.mjs muxes score.wav into the MP4.
Synth helpers are the same as the earlier promos' score.py; the music and the arrangement are new.
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
rng = np.random.default_rng(7)

BEAT = 0.5
BAR = 4 * BEAT
SCN = [2.0, 4.0, 6.5, 10.0, 13.5, 17.5, 19.5]   # scene starts (motion.html SCN); 19.5 = end card
T_SQL = 1.5        # hook: "SQL." slam
T_CHART = 12.0     # the chart starts drawing (the build lands here)
T_PEAK = 12.5      # the line reaches the December spike
T_DROP = 13.5      # "Just ask." -- the drop
T_NB = 20.0        # end card: "notebooks." slam


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



drums, bass, pad, pluckb, fx, ui, bells = (Bus() for _ in range(7))
send_s, send_l = Bus(), Bus()   # short room / long hall


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



def bass_note(f, dur=0.23):
    n = S(dur)
    t = tt(n)
    y = saw(f, n, 900, fc_t=280 + 1600 * np.exp(-t / 0.05)) * 0.8 + np.sin(2 * np.pi * f * t) * 0.9
    return np.tanh(1.4 * y) * env_ar(n, 0.004, 0.07, dur - 0.07)




# =================================================================== ARRANGEMENT
DM = ([62, 66, 69, 73], 38, [74, 78, 81, 85, 86, 88, 90])
BM = ([59, 62, 66, 69], 35, [71, 74, 78, 81, 83, 86, 88])
GM = ([55, 59, 62, 66], 31, [67, 71, 74, 78, 79, 83, 86])
AM = ([57, 61, 64, 69], 33, [69, 73, 76, 81, 83, 85, 88])
ARP = [0, 2, 4, 2, 1, 3, 5, 3, 2, 4, 6, 4, 3, 5, 4, 2]
HAT_V = [0.55, 0.22, 0.0, 0.3]   # 16ths in a beat; the 3rd is the open hat


def groove(t0, t1, chords, kick_list, pad_fc=2600, arp_gain=0.15, bass_gain=0.4, claps=True, full=True):
    """Kick on every beat, claps on 2 and 4, offbeat open hats, 8th bass, pad, 16th arp."""
    bars = int(np.ceil((t1 - t0) / BAR - 1e-6))
    for b in range(bars):
        tb = t0 + b * BAR
        notes, root, arp = chords[b % len(chords)]
        seg = min(BAR, t1 - tb)
        pad.add(pad_chord(notes, seg + 0.25, pad_fc, a=0.02, r=0.3), tb, gain=0.2)
        send_s.add(pad_chord(notes, seg + 0.25, pad_fc, a=0.02, r=0.3), tb, gain=0.05)
        for s in range(int(round(seg / 0.25))):
            bass.add(pan2(bass_note(midi(root + (12 if s % 2 else 0))), 0), tb + s * 0.25, gain=bass_gain)
        for s in range(int(round(seg / 0.125))):
            note = arp[ARP[s]]
            pluckb.add(pan2(pluck(midi(note), 0.3), 0.35 * np.sin(s * 1.3)), tb + s * 0.125, gain=arp_gain)
            send_s.add(pan2(pluck(midi(note), 0.3), 0), tb + s * 0.125, gain=arp_gain * 0.4)
    k = 0
    tb = t0
    while tb < t1 - 1e-6:
        drums.add(pan2(kick(), 0), tb, gain=0.7)
        kick_list.append(tb)
        if claps and k % 2 == 1:
            drums.add(pan2(clap(), 0), tb, gain=0.4)
            send_s.add(pan2(clap(), 0), tb, gain=0.22)
        for s in range(4 if full else 0):
            if s == 2:
                drums.add(pan2(hat(0.12, k), 0.25), tb + 0.25, gain=0.15)
            else:
                drums.add(pan2(hat(0.03, s + k), -0.3), tb + s * 0.125, gain=HAT_V[s] * 0.26)
        tb += BEAT
        k += 1


def typing(t0, t1, n, gain=0.22):
    """Soft mechanical key clicks while a screenshot types itself."""
    for k in range(n):
        tk = t0 + (t1 - t0) * k / max(1, n - 1) + rng.uniform(-0.006, 0.006)
        put(ui, tick(), tk, pan=rng.uniform(-0.35, 0.35), gain=gain * rng.uniform(0.55, 1.0), rs=0.3)


def mouse(t):
    put(ui, click(), t, pan=0.15, gain=0.3, rs=0.3)


def card_in(t):
    """A new cell rises in: whoosh into the beat, a low thump on it."""
    put_sweep(fx, whoosh(0.45, 0.7, 240, 3200, 600), t - 0.32, 0.4, -0.4, gain=0.26, rl=0.25)
    put(fx, boom(0.7, 100, 45), t, gain=0.3)


kicks = []

# ---------- 0.0-2.0  hook: a cell types `import pandas as pd`, runs, headline slams
put(pad, pad_chord(BM[0], 2.1, 1400, a=0.4, r=0.5), 0.0, gain=0.16, rl=0.4)
typing(0.12, 0.85, 19)
put(ui, bloop(midi(81)), 1.0, gain=0.24, rl=0.4)            # In [*]
put(ui, pop(midi(88)), 1.12, gain=0.3, rl=0.5)              # In [1]
for i, m in enumerate([74, 78, 81, 83]):                    # "Your notebook just learned"
    put(pluckb, pluck(midi(m), 0.35), 1.0 + i * 0.125, pan=-0.3 + 0.2 * i, gain=0.24, rl=0.4)
put(fx, riser(0.75, 500, 11000), 0.78, gain=0.2, rl=0.3)
put(fx, boom(2.0, 85, 30), T_SQL, gain=0.85)                # "SQL."
put(fx, crash(1.8), T_SQL, gain=0.26, rl=0.6)
put(ui, glitch(0.2), T_SQL, gain=0.14)

# ---------- 2.0-12.0  the groove: create, pip, SQL, Python
groove(SCN[0], 11.0, [DM, BM, GM, AM], kicks)
for s in SCN[0:4]:
    card_in(s)
typing(2.35, 3.05, 16)               # "Revenue Analysis"
mouse(3.5)                           # Create
typing(4.3, 4.82, 17)                # pandas matplotlib
mouse(5.0)                           # Install
put(bells, bell(midi(86), 1.4, decay=0.6), 5.5, gain=0.2, rl=0.6)   # Packages installed
put(ui, pop(midi(93)), 5.5, pan=0.4, gain=0.26, rl=0.4)
typing(7.0, 8.25, 38)                # the SQL query
mouse(8.5)                           # Run
put(ui, bloop(midi(76)), 8.5, gain=0.18, rl=0.3)
glitter(9.05, 9.6, 10, 2200, 4200, 0.13)                    # DataFrame rows drop in
put(ui, pop(midi(90)), 9.0, gain=0.26, rl=0.4)
typing(10.5, 11.35, 30)              # the Python code
mouse(11.5)                          # Run
# build into the chart: claps double up, hats drop out, a riser
groove(11.0, T_CHART, [AM], kicks, claps=False, full=False, bass_gain=0.3)
for k in range(8):
    put(drums, clap(0.2), 11.0 + k * 0.125, gain=0.12 + 0.03 * k, rs=0.3)
for k in range(8):
    put(drums, clap(0.15), 11.5 + k * 0.0625, gain=0.18 + 0.03 * k, rs=0.3)
put(fx, riser(1.0, 300, 12000), 11.0, gain=0.24, rl=0.4)
put(fx, rev_crash(0.6), 11.4, gain=0.16)

# ---------- 12.0-13.5  the chart draws itself: impact, then a breath (pad + rising plucks)
put(fx, boom(2.2, 90, 28), T_CHART, gain=0.95)
put(fx, crash(2.4), T_CHART, gain=0.3, rl=0.7)
put(ui, glitch(0.22), T_CHART, gain=0.14)
put(pad, pad_chord(GM[0] + [43], 1.6, 3200, a=0.01, r=0.8), T_CHART, gain=0.22, rl=0.5)
for k, m in enumerate([67, 71, 74, 78, 79, 83, 86, 90]):    # follows the line as it draws
    put(pluckb, pluck(midi(m), 0.4), T_CHART + k * 0.1125, pan=-0.6 + 0.17 * k, gain=0.2, rl=0.5)
put(bells, bell(midi(90), 1.6, decay=0.7), T_PEAK, gain=0.24, rl=0.7)   # the December spike
put(drums, kick(), T_CHART, gain=0.8)
kicks.append(T_CHART)
for k in range(4):
    put(drums, kick(), 12.5 + k * 0.25, gain=0.35 + 0.1 * k)
    kicks.append(12.5 + k * 0.25)
put(fx, riser(0.5, 800, 12000), 13.0, gain=0.22, rl=0.3)

# ---------- 13.5-19.5  THE DROP: the AI writes and runs a cell, then .ipynb import
put(fx, boom(2.4, 85, 28), T_DROP, gain=0.9)
put(fx, crash(2.4), T_DROP, gain=0.28, rl=0.6)
groove(T_DROP, SCN[6], [DM, BM, GM, AM], kicks, pad_fc=3400, arp_gain=0.17, bass_gain=0.46)
for s in SCN[4:6]:
    card_in(s)
typing(13.8, 14.6, 26, gain=0.18)    # the prompt
put_sweep(fx, whoosh(0.35, 0.5, 600, 5000, 1500), 14.72, -0.3, 0.6, gain=0.2)   # send
for k, tc in enumerate([15.0, 15.25, 15.5]):                 # three green checks
    put(ui, pop(midi(86 + 3 * k)), tc, pan=0.3, gain=0.3, rl=0.4)
glitter(15.75, 16.1, 6, 2400, 4400, 0.11)                    # the answer + table
put(ui, pop(midi(93)), 16.0, gain=0.28, rl=0.4)              # sticker
glitter(16.45, 16.95, 8, 1800, 3400, 0.1)                    # the AI's cell appears
mouse(18.0)                                                  # + menu
put(ui, bloop(midi(81)), 18.02, gain=0.18)
put(bells, bell(midi(88), 1.2, decay=0.5), 18.5, gain=0.18, rl=0.6)   # ring on .ipynb
put(ui, pop(midi(91)), 18.55, pan=-0.3, gain=0.26, rl=0.4)
put(fx, riser(0.8, 400, 12000), 18.7, gain=0.2, rl=0.4)

# ---------- 19.5-22.0  end card
card_in(SCN[6])
put(pad, pad_chord(DM[0] + [50], 2.6, 3600, a=0.02, r=1.4), SCN[6], gain=0.18, rl=0.4)
for i, m in enumerate([78, 81, 85]):
    put(pluckb, pluck(midi(m), 0.35), 19.6 + i * 0.125, pan=0.3 - 0.2 * i, gain=0.22, rl=0.4)
put(fx, boom(2.6, 85, 28), T_NB, gain=0.95)                  # "notebooks."
put(fx, crash(2.4), T_NB, gain=0.3, rl=0.7)
groove(T_NB, 21.0, [DM], kicks, pad_fc=3000, arp_gain=0.08, bass_gain=0.36)
for i, f in enumerate([190, 160, 135]):                      # logo slabs
    put(drums, tom(f, 0.3), 20.25 + 0.06 * i + 0.24, gain=0.32, rs=0.4)
glitter(20.55, 20.9, 5, 2000, 4000, 0.12)
glitter(21.0, 21.6, 7, 2400, 4600, 0.11, curve=0.8)          # shine sweep
put(bells, bell(midi(86), 2.2, decay=1.0), 21.0, gain=0.2, rl=0.7)
put(bells, bell(midi(81), 2.2, decay=1.0), 21.0, pan=-0.4, gain=0.12, rl=0.7)
put(drums, kick(), 21.0, gain=0.8)
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


def ping_pong(x, dt=0.375, fb=0.33, taps=4, gain=0.5):   # dotted eighth
    mono = x.sum(axis=0) / 2
    mono = fft_filter(mono, lp(4500, 1))
    out = np.zeros_like(x)
    for m in range(1, taps + 1):
        d = S(dt * m)
        out[m % 2, d:] += mono[:N - d] * (fb ** (m - 1)) * gain
    return out


IR_S, IR_L = make_ir(0.9, 6000, 0.008), make_ir(2.8, 5000, 0.025)

pad.x *= sidechain(kicks, 0.55)
bass.x *= sidechain(kicks, 0.85, 0.09)
pluckb.x = pluckb.x + ping_pong(pluckb.x)

wet_s = convolve(send_s.x, IR_S) * 0.35
wet_l = convolve(send_l.x, IR_L) * 0.35
mix = drums.x + bass.x + pad.x + pluckb.x + fx.x + ui.x + bells.x + wet_s + wet_l
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
M = [(float(a), float(b)) for a, b in re.findall(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)', log)]
for name, a, b in (('hook', 0.0, 2.0), ('groove', 2.0, 11.0), ('build', 11.0, 12.0), ('chart', 12.0, 13.5), ('drop', 13.5, 19.5), ('end', 19.5, 21.3)):
    vals = [m for tm, m in M if a + 0.4 <= tm <= b]
    if vals:
        print(f'  {name:7s} momentary loudness {np.mean(vals):6.1f} LUFS (min {min(vals):6.1f}, max {max(vals):6.1f})')
