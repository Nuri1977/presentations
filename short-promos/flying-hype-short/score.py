#!/usr/bin/env python3
"""Original score and sound design for motion.html (22 s, vertical hype short), synthesized with numpy only.

    python score.py             -> score.wav (48 kHz stereo, loudness-normalized to -14 LUFS)

120 BPM, one bar = 2 s. Every cue time below comes from the timeline in motion.html (T = {...}).
If you retime the video, move the matching cue here and re-run; render.mjs muxes score.wav into the MP4.
Instruments are the same synths as rosetta-dbt-studio-15sec/score.py, plus an engine, a brass "sad trombone"
and a tape stop for the freeze frame.
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
rng = np.random.default_rng(23)

BEAT = 0.5
BAR = 4 * BEAT
T_LAUNCH = 2.0     # car fires its thrusters (motion.html T.launch)
T_FREEZE = 3.5     # freeze frame + "meanwhile..." (T.freeze)
T_STUCK = 4.0      # error traffic jam (T.stuck)
T_SLAM = 6.0       # "STUCK." (T.slam)
T_SUCK = 7.45      # errors get sucked into the core (T.suck)
T_DROP = 8.0       # the drop: logo assembles (T.drop)
T_LIFT = 9.35      # logo launches (T.lift)
T_FLY = 10.0       # first panel; one panel per bar (T.fly, T.D)
T_END = 18.0       # "CARS CAN FLY NOW." (T.end)
T_DATA = 19.0      # "DATA." final hit (T.data)
T_LOCK = 19.25     # end lockup (T.lock)


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
hook_dr, hook_mu, hook_send = Bus(), Bus(), Bus()   # 2-4 s groove, kept apart so the tape stop can bend it


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



def engine(dur, f0, f1, curve=1.0):
    """Electric-ish engine whine with a combustion rumble: rising pitch, opening filter."""
    n = S(dur)
    t = tt(n)
    u = t / dur
    f = f0 * (f1 / f0) ** (u ** curve)
    ph = 2 * np.pi * np.cumsum(f) / SR
    out = np.zeros(n)
    for k in range(1, 24):
        out += np.sin(k * ph + k * 0.3) / k / np.sqrt(1 + (k * f / (700 + 2600 * u)) ** 4)
    out *= 0.72 + 0.28 * np.sin(ph * 0.5)
    whine = np.sin(ph * 6.0) * 0.18 * u
    return np.tanh(1.8 * (out + whine)) * np.clip(t / 0.05, 0, 1)


def brass(f, dur, vib=0.0):
    """Muted-trombone 'wah': saw with a filter that opens and closes, optional vibrato."""
    n = S(dur)
    t = tt(n)
    fv = f * (1 + vib * 0.035 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.15) / 0.25, 0, 1))
    ph = 2 * np.pi * np.cumsum(fv) / SR
    fc = 320 + 1500 * np.exp(-t / 0.22) * (1 - np.exp(-t / 0.03)) + (380 * vib * (0.5 + 0.5 * np.sin(2 * np.pi * 5.2 * t)))
    out = np.zeros(n)
    for k in range(1, 30):
        out += np.sin(k * ph) / k / np.sqrt(1 + (k * fv / fc) ** 4)
    amp = np.clip(t / 0.03, 0, 1) * np.clip((dur - t) / 0.1, 0, 1)
    return np.tanh(1.6 * out) * amp


def bass_note(f, dur=0.23):
    n = S(dur)
    t = tt(n)
    y = saw(f, n, 900, fc_t=280 + 1600 * np.exp(-t / 0.05)) * 0.8 + np.sin(2 * np.pi * f * t) * 0.9
    return np.tanh(1.4 * y) * env_ar(n, 0.004, 0.07, dur - 0.07)


def rumble(dur, f0=60, f1=900):
    """Thruster roar: low noise that brightens over its length."""
    return whoosh(dur, 0.92, f0, f1, f1 * 0.6, width=1.4)


def shutter():
    t = tt(S(0.12))
    x = fft_filter(rng.standard_normal(len(t)), bp(2600, 1.2))
    x = x / np.max(np.abs(x))
    e = np.exp(-t / 0.006) + 0.7 * (t > 0.045) * np.exp(-np.maximum(t - 0.045, 0) / 0.01)
    return x * e


def tape_stop(x, t0, dur, t_end):
    """Freeze-frame tape stop: playback slows to zero over dur, then silence until t_end."""
    i0, m = S(t0), S(dur)
    u = np.arange(m) / m
    pos = i0 + np.cumsum((1 - u) ** 1.4)
    y = x.copy()
    for c in range(2):
        y[c, i0:i0 + m] = np.interp(pos, np.arange(x.shape[1]), x[c]) * (1 - u ** 4)
    y[:, i0 + m:S(t_end)] = 0
    return y


# =================================================================== ARRANGEMENT
AM = ([57, 60, 64, 71], 33, [69, 72, 76, 81, 83, 84, 88])
FM = ([57, 60, 65, 67], 29, [65, 69, 72, 77, 79, 81, 84])
CM = ([55, 60, 64, 71], 36, [67, 72, 76, 79, 81, 84, 88])
GM = ([55, 59, 62, 69], 31, [67, 71, 74, 79, 81, 83, 86])
ARP = [0, 2, 4, 3, 1, 3, 5, 4, 2, 4, 6, 5, 3, 4, 2, 1]
HAT_V = [0.55, 0.22, 0.0, 0.3]   # 16ths in a beat; the 3rd is the open hat


def groove(t0, t1, chords, dr, mu, bs, send, kick_list, pad_fc=2600, arp_gain=0.16):
    """Four-on-the-floor kick, claps on 2 and 4, offbeat open hats, pumping 8th bass, pad, 16th arp."""
    bars = int(round((t1 - t0) / BAR))
    for b in range(bars):
        tb = t0 + b * BAR
        notes, root, arp = chords[b % len(chords)]
        mu.add(pad_chord(notes, BAR + 0.25, pad_fc, a=0.02, r=0.3), tb, gain=0.21)
        send.add(pad_chord(notes, BAR + 0.25, pad_fc, a=0.02, r=0.3), tb, gain=0.05)
        for s in range(8):
            bs.add(pan2(bass_note(midi(root + (12 if s % 2 else 0))), 0), tb + s * 0.25, gain=0.42)
        for s in range(16):
            ts = tb + s * 0.125
            if ts >= t1:
                break
            mu.add(pan2(pluck(midi(arp[ARP[s]]), 0.3), 0.35 * np.sin(s * 1.3)), ts, gain=arp_gain)
            send.add(pan2(pluck(midi(arp[ARP[s]]), 0.3), 0), ts, gain=arp_gain * 0.4)
    k = 0
    tb = t0
    while tb < t1 - 1e-6:
        dr.add(pan2(kick(), 0), tb, gain=0.72)
        kick_list.append(tb)
        if k % 2 == 1:
            dr.add(pan2(clap(), 0), tb, gain=0.42)
            send.add(pan2(clap(), 0), tb, gain=0.25)
        for s in range(4):
            if s == 2:
                dr.add(pan2(hat(0.12, k), 0.25), tb + 0.25, gain=0.16)
            else:
                dr.add(pan2(hat(0.03, s + k), -0.3), tb + s * 0.125, gain=HAT_V[s] * 0.28)
        tb += BEAT
        k += 1


kicks = []

# ---------- 0.0-2.0  engine revs, the build into the launch
put(fx, engine(1.1, 48, 150, 1.4), 0.0, pan=-0.6, gain=0.26)
put(fx, engine(0.95, 118, 290, 0.8), 1.08, pan=0.25, gain=0.28)
put_sweep(fx, whoosh(0.9, 0.7, 300, 3000, 900), 1.1, 0.0, 0.7, gain=0.22, rl=0.3)
put(fx, riser(1.05, 400, 9000), 0.95, gain=0.16, rl=0.4)
put(pad, pad_chord(AM[0], 2.1, 900, a=0.6, r=0.2, fc_t=None), 0.0, gain=0.09)
for i in range(4):   # filtered heartbeat kick
    put(drums, fft_filter(kick(), lp(500, 2)), i * BEAT, gain=0.55 + 0.1 * i)
    kicks.append(i * BEAT)
for s in range(8, 16):
    put(drums, hat(0.025, s), s * 0.125, pan=0.2, gain=0.05 + 0.012 * (s - 8))
put(ui, pop(midi(81)), 0.25, gain=0.35, rl=0.5)   # "CARS"
put(ui, pop(midi(84)), 0.5, gain=0.35, rl=0.5)    # "CAN"

# ---------- 2.0-3.5  LAUNCH: thrusters + the hook groove (bent by the tape stop at 3.5)
put(fx, boom(2.2, 80, 30), T_LAUNCH, gain=0.8)
put(fx, crash(2.0), T_LAUNCH, gain=0.26, rl=0.5)
put(fx, rumble(1.6, 50, 1400), T_LAUNCH - 0.05, gain=0.42)
put(fx, glitch(0.22), T_LAUNCH, gain=0.18)
hook_kicks = []
groove(T_LAUNCH, T_STUCK, [FM], hook_dr, hook_mu, hook_mu, hook_send, hook_kicks, pad_fc=3200)
hook_mu.add(pan2(clap(), 0), T_LAUNCH + 0.25, gain=0.45)   # "NOW."
put(fx, shutter(), T_FREEZE, gain=0.5)                       # freeze frame
put(ui, pop(midi(76)), T_FREEZE + 0.06, gain=0.3, rl=0.4)    # "meanwhile..." sticker

# ---------- 4.0-7.45  meanwhile: sad trombone, error pops, a dark drone
for i, (m, d, v) in enumerate([(55, 0.38, 0), (54, 0.38, 0), (53, 0.38, 0), (52, 1.15, 1)]):
    put(bells, brass(midi(m), d, v), 4.05 + i * 0.4, pan=0.0, gain=0.42, rl=0.25)
put(pad, pad_chord([50, 53, 57], 3.6, 420, a=0.4, r=0.6), T_STUCK, gain=0.13)
for tw in (4.05, 4.2, 4.35):   # "YOUR DATA TEAM:"
    put(ui, tick(), tw, gain=0.3)
for i, tc in enumerate([4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.5, 6.75]):   # error chips
    put(ui, glitch(0.16), tc, pan=0.6 * np.sin(i * 2.1), gain=0.2)
    put(ui, tom(110 + 15 * (i % 3), 0.25), tc, pan=0.6 * np.sin(i * 2.1), gain=0.3, rs=0.4)
for i in range(4):   # clock tick on the beat
    put(drums, tick(), T_STUCK + i * BEAT, pan=0.4, gain=0.18)
put(fx, boom(1.8, 70, 32), T_SLAM, gain=0.85)          # "STUCK."
put(drums, kick(), T_SLAM, gain=1.0)
put(drums, clap(), T_SLAM, gain=0.55, rl=0.4)
put(fx, crash(1.6), T_SLAM, gain=0.18, rl=0.3)
for tk, g in ((6.75, 0.8), (7.0, 0.8)):
    put(drums, kick(), tk, gain=g)
    kicks.append(tk)
put(drums, clap(), 6.5, gain=0.4, rs=0.4)

# ---------- 7.0-8.0  build: accelerating clap roll, riser, a beat of silence before the drop
roll = [7.0, 7.25, 7.5, 7.625, 7.75, 7.8125]   # 8ths -> 16ths -> 32nds, then silence
for i, tr in enumerate(roll):
    put(drums, clap(0.25), tr, pan=0.2 * ((-1) ** i), gain=0.25 + 0.08 * i, rs=0.3)
put(fx, riser(0.88, 300, 11000), 7.0, gain=0.24, rl=0.4)
put(fx, rev_crash(0.9), 7.1, gain=0.22)
put(fx, rumble(0.85, 40, 500), 7.0, gain=0.2)

# ---------- 8.0-17.75  THE DROP
put(fx, boom(2.6, 85, 28), T_DROP, gain=0.95)
put(fx, crash(2.6), T_DROP, gain=0.32, rl=0.6)
put(fx, glitch(0.25), T_DROP, gain=0.2)
groove(T_DROP, 17.75, [AM, FM, CM, GM, AM], drums, pad, bass, send_s, kicks)
for i, f in enumerate([180, 150, 125]):   # logo slabs land (slow, gap 0.1)
    put(drums, tom(f, 0.4), T_DROP + 0.02 + 0.1 * i + 0.3, gain=0.5, rs=0.4)
glitter(T_DROP + 0.6, T_DROP + 1.0, 6, 1800, 3600, 0.16)   # sparkle spins in
put(fx, rumble(1.15, 40, 1600), 8.9, gain=0.36)            # thrusters ignite
put_sweep(fx, riser(0.66, 500, 12000), T_LIFT, 0.0, 0.0, gain=0.24, rl=0.4)   # launch

for i in range(4):   # panels: whip, slam, sticker pop, ring ping
    s = T_FLY + i * BAR
    put_sweep(fx, whoosh(0.5, 0.62, 260, 3600, 700), s - 0.31, -0.5, 0.5, gain=0.3, rl=0.25)
    put(fx, boom(0.9, 95, 40), s, gain=0.42)
    put(fx, crash(1.2), s, gain=0.12, rl=0.3)
    put(ui, glitch(0.18), s, gain=0.14)
    put(ui, pop(midi(88 - 2 * i)), s + 0.45, pan=0.5 if i % 2 == 0 else -0.5, gain=0.36, rl=0.4)
    put(bells, bell(midi([88, 84, 86, 83][i]), 1.2, decay=0.5), s + 0.6, gain=0.14, rl=0.6)
put(fx, riser(0.95, 400, 12000), 17.0, gain=0.22, rl=0.4)
put(fx, rev_crash(0.8), 17.2, gain=0.2)

# ---------- 18.0-22.0  "CARS CAN FLY NOW. SO CAN YOUR DATA." -> lockup
put(pad, pad_chord(FM[0], 1.1, 1800, a=0.05, r=0.3), T_END, gain=0.14)
for i, m in enumerate([76, 79, 81, 84]):
    put(pluckb, pluck(midi(m), 0.35), T_END + i * 0.125, pan=-0.3 + 0.2 * i, gain=0.24, rl=0.4)
for i, m in enumerate([84, 86, 88]):
    put(pluckb, pluck(midi(m), 0.35), 18.5 + i * 0.125, pan=0.3 - 0.2 * i, gain=0.26, rl=0.4)
    put(drums, clap(0.2), 18.5 + i * 0.125, gain=0.2 + 0.08 * i)
put(fx, riser(0.45, 800, 12000), 18.55, gain=0.2)
put(fx, boom(2.8, 85, 28), T_DATA, gain=1.0)                 # "DATA."
put(fx, crash(2.8), T_DATA, gain=0.34, rl=0.7)
put(pad, pad_chord(CM[0] + [48], 3.0, 3800, a=0.01, r=1.6), T_DATA, gain=0.2, rl=0.4)
groove(T_DATA, 21.0, [CM], drums, pad, bass, send_s, kicks, pad_fc=3000, arp_gain=0.09)
for i, f in enumerate([190, 160, 135]):   # end logo slabs (fast, gap 0.06)
    put(drums, tom(f, 0.3), T_LOCK + 0.06 * i + 0.24, gain=0.35, rs=0.4)
glitter(T_LOCK + 0.3, T_LOCK + 0.62, 5, 2000, 4000, 0.13)
put_sweep(fx, engine(1.35, 140, 420, 0.7), 19.35, -0.9, 0.9, gain=0.16)   # victory lap
put_sweep(fx, whoosh(1.35, 0.5, 300, 4000, 900), 19.35, -0.9, 0.9, gain=0.2, rl=0.3)
glitter(20.5, 21.25, 8, 2400, 4600, 0.12, curve=0.8)           # shine sweep
put(bells, bell(midi(84), 2.2, decay=1.0), 21.0, gain=0.2, rl=0.7)
put(bells, bell(midi(79), 2.2, decay=1.0), 21.0, pan=-0.4, gain=0.12, rl=0.7)
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

# the hook groove gets its own room, then the freeze frame bends all of it to a stop
hook_mu.x *= sidechain(hook_kicks, 0.7, 0.1)
hook = hook_dr.x + hook_mu.x + convolve(hook_send.x, IR_S) * 0.35
hook = tape_stop(hook, T_FREEZE, 0.4, T_STUCK)

pad.x *= sidechain(kicks, 0.55)
bass.x *= sidechain(kicks, 0.85, 0.09)
pluckb.x = pluckb.x + ping_pong(pluckb.x)

wet_s = convolve(send_s.x, IR_S) * 0.35
wet_l = convolve(send_l.x, IR_L) * 0.35
mix = drums.x + bass.x + pad.x + pluckb.x + fx.x + ui.x + bells.x + hook + wet_s + wet_l
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
for name, b in (('drums', drums.x), ('bass', bass.x), ('pad', pad.x), ('pluck', pluckb.x), ('fx', fx.x), ('ui', ui.x), ('bells', bells.x), ('hook', hook)):
    seg = b[:, S(T_DROP):S(T_END)] if name != 'hook' else b[:, S(T_LAUNCH):S(T_FREEZE)]
    print(f'  {name:6s} rms {20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-12):6.1f} dB   peak {20 * np.log10(np.max(np.abs(b)) + 1e-12):6.1f} dB')
M = [(float(a), float(b)) for a, b in re.findall(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)', log)]
for name, a, b in (('build', 0.0, 2.0), ('launch', 2.0, 3.5), ('stuck', 4.0, 7.0), ('drop', 8.0, 10.0), ('panels', 10.0, 18.0), ('end', 18.0, 21.3)):
    vals = [m for tm, m in M if a + 0.4 <= tm <= b]
    if vals:
        print(f'  {name:7s} momentary loudness {np.mean(vals):6.1f} LUFS (min {min(vals):6.1f}, max {max(vals):6.1f})')
