import numpy as np
import matplotlib.pyplot as plt

# Objective 1: Develop a function to perform DFT of N point signal
def compute_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

# Objective 2: Calculate DFT of a DT signal and Plot Spectrum of Signal
def plot_spectrum(x, title):
    X = compute_dft(x)
    magnitude_spectrum = np.abs(X)

    plt.figure(figsize=(10, 6))
    plt.stem(np.arange(len(x)), magnitude_spectrum, basefmt='b')
    plt.title(title)
    plt.xlabel('Frequency (k)')
    plt.ylabel('Magnitude Spectrum')
    plt.grid(True)
    plt.show()


# Objective 3: Calculate the effect of zero padding on magnitude spectrum
def zero_padding_experiment(x, padding_type):
    if padding_type == 'zero':
        padded_x = np.pad(x, (0, len(x)), mode='constant')
        title = 'Zero Padding'
    elif padding_type == 'alternate':
        padded_x = np.zeros(2 * len(x))
        padded_x[::2] = x
        title = 'Alternate Zero Insertion'

    plot_spectrum(padded_x, title)

    return padded_x

# Problem Definition

# (1) Take any four-point sequence x[n].
x1 = np.array([1, 2, 3, 4])
plot_spectrum(x1, 'Original Signal')

# (2) Append the input signal by four zeros.
x2 = zero_padding_experiment(x1, 'zero')

# (3) Expand the input signal by inserting alternate zero.
x3 = zero_padding_experiment(x1, 'alternate')

# Give your conclusion based on the observations from the plots.
print("Conclusion:")
print("The original signal has a certain magnitude spectrum.")
print("Zero padding increases the resolution of the magnitude spectrum.")
print("Alternate zero insertion changes the spectral characteristics, affecting the peaks and overall shape.")
