import math
import dsp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


fs = 200
N = 1024

time = []
sig = []
for t in range(0, N):
    time.append(t * 1/fs)
    sig.append(5 * math.cos(2 * math.pi * 49 * time[-1]) * 2.5 * math.cos(2 * math.pi * 30 * time[-1]) * math.cos(2 * math.pi * 11 * time[-1]))

magnitudes = dsp.dft(sig)
mag2 = dsp.fft(sig)

frequencies = []
amplitudes = []
f_nyquist = fs / 2
for index in range(1, int(N)):
    freq = fs/N * index
    if freq >= f_nyquist:
        break
    frequencies.append(freq)
    amplitudes.append(round(abs(mag2[index] / N * 2), 2))

p = plt.plot(frequencies, amplitudes)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")
plt.show()
