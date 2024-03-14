import numpy as np
from scipy.fft import fft, ifft
# Input signal
x = [1, 2, 3, 4, 5, 6, 7, 8]
# Filter taps
h = [0.5, 0.5]
# Overlap add
def overlap_add(x, h, N, L):
    y = []
    for i in range(0, len(x), N - L):
        x_blk = x[i:i + N]
        x_pad = np.pad(x_blk, (0, N - len(x_blk)), mode='constant')
        X = fft(x_pad)
        h_pad = np.pad(h, (0, N - len(h)), mode='constant')
        H = fft(h_pad)
        Y = X * H
        y_blk = np.real(ifft(Y))
        y.extend(y_blk[:N - L])
    return y
y_oa = overlap_add(x, h, 4, 2)
print("Overlap Add Output:", y_oa)
def overlap_save(x, h, N, L):
    x_blocks = [x[i:i + N - L] for i in range(0, len(x), N - L)]
    y = []
    for x_blk in x_blocks:
        x_pad = np.pad(x_blk, (0, N - L - len(x_blk)), mode='constant')
        X = fft(x_pad, N)
        h_pad = np.pad(h, (0, N - len(h)), mode='constant')
        H = fft(h_pad, N)
        Y = X * H
        y_blk = np.real(ifft(Y))
        y.extend(y_blk[:N - L])
    return y
y_os = overlap_save(x, h, 4, 2)
print("Overlap Save Output:", y_os)


