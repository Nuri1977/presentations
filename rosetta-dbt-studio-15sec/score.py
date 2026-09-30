#!/usr/bin/env python3
"""Original score and sound design for motion.html (30 s), synthesized with numpy only.

    python3 score.py            -> score.wav (48 kHz stereo, loudness-normalized to -14 LUFS)

Every cue time below comes from the timeline in motion.html. If you retime the video,
move the matching cue here and re-run; render.mjs muxes score.wav into the MP4.
"""
import os
import re
import subprocess
import wave

import numpy as np

SR = 48000
DUR = 24.0
PACE = 1.25           # motion.html PACE: the authored 24 s timeline plays 1.25x slower -> 30 s
N = int(SR * DUR * PACE)
HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(11)

BEAT = 0.5            # authored beat; real tempo is 120 / PACE = 96 BPM, one bar per panel
T_DROP = 4.1          # tour starts (motion.html T.tour)
T_PULL = 18.1         # pull back to the overview (T.pull)
T_END = 20.1          # end card (T.end)


# ---------------------------------------------------------------- basics
def L(sec):
    """Authored duration -> real duration (cue times go through put(), which scales them)."""
    return sec * PACE


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
    bus.add(sig, t0 * PACE, pan, gain)
    if rs:
        send_s.add(sig, t0 * PACE, pan, gain * rs)
    if rl:
        send_l.add(sig, t0 * PACE, pan, gain * rl)


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


# =================================================================== ARRANGEMENT
BAR = 4 * BEAT
SPEED = 0.75          # motion.html SPEED: panel content plays at 0.75x its authored pace
T_BUTTON = T_END + BAR  # final hit on the end card (motion.html shine sweep)


def cue(i, lt):
    """Real time of panel i's content at its authored time lt (renderWorld in motion.html)."""
    return T_DROP + i * BAR + (0.34 if i == 0 else 0.3) + lt / SPEED


#      pad voicing        bass  arp tones
AM = ([57, 60, 64, 71], 33, [69, 72, 76, 81, 83, 84, 88])
FM = ([57, 60, 65, 67], 29, [65, 69, 72, 77, 79, 81, 84])
CM = ([55, 60, 64, 71], 36, [67, 72, 76, 79, 81, 84, 88])
GM = ([55, 59, 62, 69], 31, [67, 71, 74, 79, 81, 83, 86])
PROG = [AM, FM, CM, GM, AM, FM, CM, GM]   # one bar per panel, then the overview bar

# ---------- 0.0-2.0  "One dbt project. Too many tools."
DR = L(1.97)
t = tt(S(DR))
fc = 180 * (1100 / 180) ** (t / DR)
drone = np.zeros((2, len(t)))
for d, p in ((-7, -0.5), (7, 0.5)):
    drone += pan2(saw(midi(33) * 2 ** (d / 1200), len(t), 1100, fc_t=fc, coherent=True), p)
drone += pan2(np.sin(2 * np.pi * midi(33) * t) * 0.7, 0)
drone *= (0.35 + 0.65 * (t / DR) ** 1.5) * np.clip(t / 0.08, 0, 1) * np.clip((DR - t) / 0.015, 0, 1)
put(pad, drone, 0.0, gain=0.2, rl=0.15)
put(drums, kick(), 0.06, gain=0.55)                                   # "One"
for k, t0 in enumerate(np.arange(0.1, 1.3, BEAT / 4)):               # tempo ticks, on the 120 BPM grid
    put(drums, hat(0.018, k), t0, pan=0.3 if k % 2 else -0.3, gain=(0.035 + 0.04 * t0 / 1.3) * (1.6 if k % 4 == 0 else 1))
CHIP_X = [380, 960, 1545, 245, 1690, 250, 1680, 400, 960, 1530]
for k, n in enumerate([69, 72, 74, 76, 79, 81, 84, 86, 88, 91]):   # tool chips pop in
    put(ui, pop(midi(n)), 0.15 + 0.065 * k, pan=(CHIP_X[k] / 1920 * 2 - 1) * 0.8, gain=0.13, rl=0.35)
for n, t0, g in ((40, 0.53, 0.8), (43, 0.61, 0.85), (45, 0.69, 1.0)):  # "Too / many / tools."
    put(bass, pluck(midi(n), 0.5, 0.6) + 0.8 * tom(midi(n), 0.5), t0, gain=0.34 * g, rl=0.1)
    put(pluckb, pluck(midi(n + 24), 0.4, 1.2), t0, gain=0.07 * g, rl=0.3)
put(fx, glitch(), 0.86, pan=0.75, gain=0.12, rs=0.3)                    # error chip shakes
put(fx, riser(L(0.85), 300, 7500), 1.12, gain=0.3, rl=0.2)                 # chips get pulled in
put(fx, rev_crash(L(0.9)), 1.07, gain=0.22)
SWD = L(0.7)
sw = tt(S(SWD))
put(fx, np.sin(2 * np.pi * np.cumsum(150 * (8 ** (sw / SWD))) / SR) * (sw / SWD) ** 2 * 0.5, 1.27, gain=0.12)

# ---------- 2.0-4.1  logo reveal
put(drums, boom(), 2.0, gain=0.7)
put(drums, crash(), 2.0, gain=0.3, rl=0.4)
put(pad, pad_chord([45, 57, 60, 64, 71], L(0.9), 3400, a=0.004, r=0.8), 2.0, gain=0.3, rl=0.5)
lt = tt(S(L(1.95)))
put(pad, pad_chord([45, 57, 60, 64, 71], L(1.95), 2400, a=0.25, r=0.25, fc_t=700 * (2600 / 700) ** (lt / L(1.95))), 2.05, gain=0.16, rl=0.4)
for k, (n, p) in enumerate(((45, -0.25), (48, 0.0), (52, 0.25))):     # cube slabs land
    t0 = 2.14 + 0.1 * k
    put(drums, tom(midi(n) * 2), t0, pan=p, gain=0.35, rs=0.3)
    put(pluckb, pluck(midi(n + 24), 0.6, 1.2), t0, pan=p, gain=0.1, rl=0.4)
for k, n in enumerate([81, 84, 88, 93]):                               # frame draws
    put(bells, pluck(midi(n), 0.5, 1.5), 2.32 + 0.1 * k, pan=-0.4 + 0.27 * k, gain=0.06, rl=0.7)
put(bells, bell(midi(88)), 2.7, pan=0.35, gain=0.2, rl=0.6)            # sparkle
put(bells, bell(midi(95), 1.2, idx=1.2), 2.72, pan=0.45, gain=0.07, rl=0.6)
glitter(2.66, 3.05, 14, 3500, 8000, 0.03, 0.1, 0.8)
put_sweep(fx, whoosh(L(0.6), 0.45, 400, 3200, 900), 2.72, -0.6, 0.6, gain=0.2, rl=0.2)  # name reveals
put(pluckb, pluck(midi(76), 0.8, 1.0), 3.2, gain=0.07, rl=0.5)          # tagline
for k, t0 in enumerate(np.arange(T_DROP - 6 * BEAT / 4, T_DROP - 0.01, BEAT / 4)):   # arp sneaks in
    put(pluckb, pluck(midi(AM[2][[0, 2, 4, 3, 1, 3][k]]), 0.35, 0.6 + 0.1 * k), t0, pan=0.25 if k % 2 else -0.25, gain=0.06 + 0.015 * k, rl=0.3)
for k, t0 in enumerate(list(np.arange(3.6, 3.85, BEAT / 4)) + list(np.arange(3.85, 4.08, BEAT / 8))):  # snare roll
    put(drums, clap(0.2), t0, gain=0.1 + 0.035 * k, rs=0.2)
put(fx, riser(L(0.65), 500, 9000), 3.45, gain=0.45, rl=0.2)                # orange wipe
put(fx, rev_crash(L(0.6)), 3.5, gain=0.3)

# ---------- 4.1-20.1  the tour, one bar per panel, then the overview
GROOVE_END = T_END - BEAT                      # drums step out for the build into the end card
kicks = list(np.arange(T_DROP, GROOVE_END - 1e-6, BEAT))
for tk in kicks:
    put(drums, kick(), tk, gain=0.42)
put(drums, boom(1.6, 60, 30), T_DROP, gain=0.35)
T_HALF = T_DROP + 4 * BAR                      # panel 05 (Analytics): second half lifts
for tc in (T_DROP, T_HALF, T_PULL):
    put(drums, crash(), tc, gain=0.26, rl=0.3)
for k, (t0, n) in enumerate(zip(np.arange(T_HALF - BEAT, T_HALF - 0.01, BEAT / 4), [52, 50, 47, 45])):  # tom fill
    put(drums, tom(midi(n)), t0, pan=0.4 - 0.27 * k, gain=0.3, rs=0.3)
for tcl in np.arange(T_DROP + BEAT, GROOVE_END, 2 * BEAT):
    put(drums, clap(), tcl, gain=0.3, rs=0.35)
for bi in (5, 6):                                                     # pickup claps late in the tour
    put(drums, clap(0.25), T_DROP + bi * BAR + BAR - BEAT / 4, gain=0.14, rs=0.3)
for k, th in enumerate(np.arange(T_DROP, GROOVE_END, BEAT / 4)):
    pos, bar_i = k % 4, int((th - T_DROP + 1e-6) // BAR)
    if pos == 2 and bar_i >= 2:
        put(drums, hat(0.12 if bar_i >= 4 else 0.07, k), th, pan=0.2, gain=0.1, rs=0.1)   # opens up from panel 03
    elif pos != 0:
        put(drums, hat(0.022, k), th, pan=-0.25 if pos == 1 else 0.3, gain=0.055 + 0.02 * (pos == 3))
ARP = [0, 2, 4, 3, 1, 3, 5, 4, 2, 4, 6, 5, 3, 4, 2, 1]
for bi, (voicing, root, arp) in enumerate(PROG):
    b0 = T_DROP + bi * BAR
    last = bi == len(PROG) - 1
    bar_len = GROOVE_END - b0 if last else BAR
    if not last:
        put(pad, pad_chord(voicing, L(BAR + 0.3), 2200 + 160 * bi, a=0.03, r=0.35), b0, gain=0.16, rl=0.35)
    else:  # the overview chord holds through the build and opens into the end card
        pl = L(T_END - b0) - 0.03
        pt = tt(S(pl))
        put(pad, pad_chord(voicing, pl, 7000, a=0.03, r=0.04, fc_t=2600 * (7000 / 2600) ** (pt / pl)), b0, gain=0.16, rl=0.35)
    for j, off in enumerate(np.arange(BEAT / 2, bar_len, BEAT)):          # bass on the off-beats
        f = midi(root + (12 if j % 4 == 2 else 0))
        n = S(L(0.22))
        v = saw(f, n, 480, coherent=True) * 0.8 + np.sin(2 * np.pi * f * tt(n)) * 0.9
        put(bass, v * env_ar(n, 0.004, 0.07, 0.14), b0 + off, gain=0.26)
    for s in range(int(round(bar_len / (BEAT / 4)))):
        put(pluckb, pluck(midi(arp[ARP[s % 16]]), 0.35, 0.7 + 0.1 * bi), b0 + s * BEAT / 4, pan=0.3 if s % 2 else -0.3,
            gain=(0.16 if bi < 2 else 0.2) * (1.25 if s % 4 == 0 else 1.0), rs=0.2, rl=0.2)
for bi, notes in ((4, (88, 84)), (5, (84, 81)), (6, (83, 79)), (7, (86,))):   # bell melody, second half
    for k, n in enumerate(notes):
        put(bells, bell(midi(n), 1.6, idx=1.6, decay=0.9), T_DROP + bi * BAR + k * 2 * BEAT, pan=0.25 - 0.5 * k, gain=0.1, rl=0.6)

# whooshes on every camera move (peak at mid-whip), panned against the motion
WHIP_PAN = [None, (0.65, -0.65), (0.65, -0.65), (0.65, -0.65), (-0.35, 0.35), (-0.65, 0.65), (-0.65, 0.65)]
for i in range(1, 7):
    put_sweep(fx, whoosh(L(0.6), 0.42, 260, 2600, 500), T_DROP + i * BAR, *WHIP_PAN[i], gain=0.38, rl=0.15)
put(fx, whoosh(L(0.5), 0.12, 2400, 2600, 600), T_DROP, gain=0.12, rl=0.2)   # wipe opens

# panel UI sounds, pitched to each panel's chord (quiet; they sit under the music)
put(ui, click(), cue(0, 0.58), pan=-0.2, gain=0.1, rs=0.3)              # 01 click PostgreSQL
for k, n in enumerate([88, 93]):
    put(bells, pluck(midi(n), 0.5, 1.4), cue(0, 0.72) + 0.07 * k, gain=0.07, rl=0.5)
for c, n in enumerate([77, 81, 84, 89]):                                 # 02 lineage columns
    put(ui, pop(midi(n)), cue(1, 0.14 * c + 0.04), pan=-0.5 + 0.33 * c, gain=0.05, rl=0.4)
for k, n in enumerate([84, 89]):
    put(bells, pluck(midi(n), 0.5, 1.4), cue(1, 0.6) + 0.07 * k, pan=0.4, gain=0.06, rl=0.5)
put(ui, click(), cue(2, 0.02), pan=-0.4, gain=0.1, rs=0.3)              # 03 Run
for k in range(9):
    put(ui, tick(), cue(2, 0.1 + 0.065 * k), pan=rng.uniform(-0.3, 0.3), gain=0.05)
for k, n in enumerate([79, 84, 88]):
    put(bells, pluck(midi(n), 0.5, 1.4), cue(2, 0.76) + 0.06 * k, pan=0.3, gain=0.07, rl=0.5)
for t0 in np.sort(rng.uniform(cue(3, 0.0), cue(3, 0.42), 18)):          # 04 typing SQL
    put(ui, tick(), t0, pan=rng.uniform(-0.3, 0.3), gain=0.04)
put(ui, click(), cue(3, 0.47), pan=-0.2, gain=0.1, rs=0.3)
for k, n in enumerate([74, 79, 81, 83, 86, 91]):                         # chart bars grow
    put(ui, pop(midi(n)), cue(3, 0.58 + 0.045 * k), pan=0.1 + 0.1 * k, gain=0.045, rl=0.4)
for k in range(12):                                                      # 05 analytics: page lines
    put(ui, tick(), cue(4, 0.02 + 0.035 * k), pan=-0.5, gain=0.03)
put(ui, click(), cue(4, 0.46), pan=-0.4, gain=0.1, rs=0.3)              # Run all
for k, n in enumerate([81, 84]):                                         # BigValues pop
    put(ui, pop(midi(n)), cue(4, 0.6 + 0.06 * k), pan=0.2 + 0.2 * k, gain=0.06, rl=0.4)
for k, n in enumerate([76, 79, 81, 84, 86, 88]):                         # line chart points
    put(ui, pop(midi(n)), cue(4, 0.72 + 0.06 * k), pan=0.1 + 0.1 * k, gain=0.045, rl=0.4)
put(ui, click(), cue(4, 0.97), pan=0.5, gain=0.1, rs=0.3)               # Build Analytics Site
for k, n in enumerate([84, 88, 93]):
    put(bells, pluck(midi(n), 0.5, 1.4), cue(4, 1.03) + 0.06 * k, pan=0.4, gain=0.07, rl=0.5)
for k, n in enumerate([72, 77, 81]):                                     # 06 files hit the lake
    put(ui, bloop(midi(n)), cue(5, 0.28 + 0.13 * k), pan=-0.45 + 0.2 * k, gain=0.1, rl=0.5)
for k, n in enumerate([84, 86, 89, 91, 93]):
    put(ui, pop(midi(n)), cue(5, 0.47 + 0.05 * k), pan=-0.6 + 0.3 * k, gain=0.035, rl=0.4)
put_sweep(ui, whoosh(L(0.25), 0.3, 1500, 4000, 2000), cue(6, 0.0), 0.5, 0.2, gain=0.06)   # 07 message sent
for k in range(8):
    put(ui, tick(), cue(6, 0.2 + 0.025 * k), pan=-0.3, gain=0.03)
for lt0, n in ((0.47, 88), (0.59, 91)):
    put(bells, pluck(midi(n), 0.4, 1.4), cue(6, lt0), pan=0.2, gain=0.06, rl=0.4)
put(ui, click(), cue(6, 0.67), pan=0.3, gain=0.1, rs=0.3)               # Allow
for k, n in enumerate([84, 88, 91]):
    put(bells, pluck(midi(n), 0.5, 1.4), cue(6, 0.8) + 0.06 * k, pan=0.2, gain=0.07, rl=0.5)

# pull back to the overview, arrows draw, then build into the end card
put_sweep(fx, whoosh(L(1.1), 0.35, 200, 1800, 300), T_PULL - 0.05, -0.3, 0.3, gain=0.3, rl=0.25)
for k, n in enumerate([74, 79, 81, 83, 86, 91]):
    put(ui, pop(midi(n)), T_PULL + 0.6 + 0.07 * k, pan=-0.6 + 0.24 * k, gain=0.045, rl=0.5)
for k, t0 in enumerate(list(np.arange(GROOVE_END, GROOVE_END + 0.25, BEAT / 4)) + list(np.arange(GROOVE_END + 0.25, T_END - 0.03, BEAT / 8))):
    put(drums, clap(0.18), t0, gain=0.07 + 0.02 * k, rs=0.25)
put(fx, riser(L(0.6), 600, 9500), T_END - 0.6, gain=0.42, rl=0.2)
put(fx, rev_crash(L(0.55)), T_END - 0.57, gain=0.25)

# ---------- 20.1-24.0  end card: resolve to C, one light bar, then the final hit
put(drums, boom(2.2, 62, 28), T_END, gain=0.6)
put(drums, crash(2.2), T_END, gain=0.28, rl=0.5)
end_kicks = [T_END + BEAT * k for k in range(4)]
for tk in end_kicks:
    put(drums, kick(), tk, gain=0.34)
for tcl in (T_END + BEAT, T_END + 3 * BEAT):
    put(drums, clap(), tcl, gain=0.2, rs=0.35)
for k, th in enumerate(np.arange(T_END, T_BUTTON - 0.01, BEAT / 4)):
    if k % 4:
        put(drums, hat(0.022, k), th, pan=0.25 if k % 2 else -0.25, gain=0.045)
put(pad, pad_chord([55, 60, 64, 67, 74], L(BAR + 0.2), 3000, a=0.01, r=0.3), T_END, gain=0.2, rl=0.5)
for j, off in enumerate(np.arange(BEAT / 2, BAR, BEAT)):
    f = midi(36 + (12 if j == 2 else 0))
    n = S(L(0.22))
    put(bass, (saw(f, n, 480, coherent=True) * 0.8 + np.sin(2 * np.pi * f * tt(n)) * 0.9) * env_ar(n, 0.004, 0.07, 0.14), T_END + off, gain=0.22)
for s in range(16):
    put(pluckb, pluck(midi(CM[2][ARP[s]]), 0.35, 1.2), T_END + s * BEAT / 4, pan=0.3 if s % 2 else -0.3, gain=0.12, rs=0.2, rl=0.2)
put(drums, tom(midi(48) * 2), 20.49, gain=0.25, rs=0.3)                  # icon pops
put(pluckb, pluck(midi(72), 0.9, 1.1), 20.49, gain=0.1, rl=0.5)
put(bells, bell(midi(91)), 20.76, pan=0.3, gain=0.18, rl=0.6)            # sparkle
glitter(20.72, 21.05, 12, 3500, 8000, 0.028, 0.0, 0.7)
put_sweep(fx, whoosh(L(0.45), 0.4, 500, 3000, 900), 20.52, -0.4, 0.4, gain=0.12, rl=0.2)  # name rises
for k, n in enumerate([76, 79, 84]):                                     # three pills
    put(pluckb, pluck(midi(n), 0.7, 1.2), 21.0 + 0.095 * k, pan=-0.4 + 0.4 * k, gain=0.12, rl=0.5)
put(bells, bell(midi(86), 1.4, idx=1.4), 21.3, gain=0.08, rl=0.6)        # github url
for k, t0 in enumerate(np.arange(T_BUTTON - BEAT, T_BUTTON - 0.01, BEAT / 4)):
    put(drums, clap(0.18), t0, gain=0.08 + 0.03 * k, rs=0.25)
put(fx, riser(L(0.5), 700, 9000), T_BUTTON - 0.5, gain=0.25, rl=0.2)
put(drums, boom(2.0, 60, 28), T_BUTTON, gain=0.55)                        # final hit
put(drums, crash(2.2), T_BUTTON, gain=0.28, rl=0.5)
et = tt(S(L(DUR - T_BUTTON)))
put(pad, pad_chord([48, 55, 60, 64, 67, 74], L(DUR - T_BUTTON), 3600, a=0.01, r=1.2, fc_t=1400 + 2200 * np.exp(-et / 0.6)), T_BUTTON, gain=0.26, rl=0.6)
nb = S(L(DUR - T_BUTTON))
put(bass, np.sin(2 * np.pi * midi(36) * tt(nb)) * np.exp(-tt(nb) / 1.1) * np.clip(tt(nb) / 0.01, 0, 1), T_BUTTON, gain=0.35)
put(bells, bell(midi(96), 2.0, idx=1.2, decay=1.1), T_BUTTON, pan=0.2, gain=0.08, rl=0.7)
glitter(T_BUTTON, T_BUTTON + 0.75, 26, 5000, 9500, 0.018, -0.8, 0.8, curve=0.8)   # shine sweep


# =================================================================== MIX
def sidechain(times, depth, rel=0.12):
    g = np.ones(N)
    for tk in times:
        i0 = S(tk * PACE)
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


def ping_pong(x, dt=L(0.375), fb=0.33, taps=4, gain=0.55):   # dotted eighth
    mono = x.sum(axis=0) / 2
    mono = fft_filter(mono, lp(4500, 1))
    out = np.zeros_like(x)
    for m in range(1, taps + 1):
        d = S(dt * m)
        out[m % 2, d:] += mono[:N - d] * (fb ** (m - 1)) * gain
    return out


all_kicks = kicks + end_kicks
pad.x *= sidechain(all_kicks, 0.55)
bass.x *= sidechain(all_kicks, 0.85, 0.09)
pluckb.x = (pluckb.x + ping_pong(pluckb.x)) * sidechain(all_kicks, 0.35)

wet_s = convolve(send_s.x, make_ir(0.9, 6000, 0.008)) * 0.35
wet_l = convolve(send_l.x, make_ir(2.8, 5000, 0.025)) * 0.35
mix = drums.x + bass.x + pad.x + pluckb.x + fx.x + ui.x + bells.x + wet_s + wet_l
mix = np.stack([fft_filter(mix[c], hp(28, 2)) for c in range(2)])

fade = np.ones(N)
fs0 = S(L(DUR) - 0.8)
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
print(f'wrote {out}: {L(DUR):.1f}s, {I:.1f} LUFS, true peak {tp:.1f} dBTP')
for name, b in (('drums', drums), ('bass', bass), ('pad', pad), ('pluck', pluckb), ('fx', fx), ('ui', ui), ('bells', bells)):
    seg = b.x[:, S(L(T_DROP)):S(L(T_PULL))]
    print(f'  {name:6s} tour rms {20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-12):6.1f} dB   peak {20 * np.log10(np.max(np.abs(b.x)) + 1e-12):6.1f} dB')
M = [(float(a), float(b)) for a, b in re.findall(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)', log)]
for name, a, b in (('intro', 0.0, 2.0), ('logo', 2.0, T_DROP), ('tour', T_DROP, T_PULL), ('overview', T_PULL, T_END), ('end', T_END, DUR - 0.7)):
    vals = [m for tm, m in M if L(a) + 0.4 <= tm <= L(b)]
    if vals:
        print(f'  {name:8s} momentary loudness {np.mean(vals):6.1f} LUFS (min {min(vals):6.1f}, max {max(vals):6.1f})')
