import librosa
import numpy as np

def correlation(signal1, signal2):
    return np.correlate(signal1, signal2, mode='full')

def energy(signal):
    return np.sum(np.abs(signal)**2)

def scale_signal(signal, factor):
    return factor * signal

# Auto correlation of input signal
def auto_correlation(signal):
    y = correlation(signal, signal)
    is_even = np.all(y % 2 == 0)
    energy_y = energy(y)
    significance_y_0 = y[len(y)//2]
    return y, is_even, energy_y, significance_y_0

# Auto correlation of delayed input signal
def delayed_auto_correlation(signal):
    p = correlation(signal[:-1], signal[:-1])
    return p

# Cross correlation of input signal and delayed input signal
def cross_correlation(signal1, signal2):
    q = correlation(signal1, signal2)
    return q

# Cross correlation of input signal and scaled input signal
def scaled_cross_correlation(signal1, scale_factor):
    s = correlation(signal1, scale_signal(signal1, scale_factor))
    return s

# Audio Authentication
def audio_authentication(audio_password, test_audio_password, threshold=0.9):
    min_length = min(len(audio_password), len(test_audio_password))
    r = np.corrcoef(audio_password[:min_length], test_audio_password[:min_length])[0, 1]
    return r > threshold

# Load audio files
audio_file1 = r'file1.wav'
audio_file2 = r'test_password.wav'
# E:\college\3rd year\SEM 6\FOSIP\exp2\file1.wav
# Load audio signals using librosa
audio_password, _ = librosa.load(audio_file1, sr=None)
test_audio_password, _ = librosa.load(audio_file2, sr=None)

# 1. Auto correlation of input signal
y, is_even, energy_y, significance_y_0 = auto_correlation(audio_password)
print("Auto-correlation of input signal:")
print("Is Even:", is_even)
print("Energy:", energy_y)
print("Significance at y[0]:", significance_y_0)

# 2. Auto correlation of delayed input signal
p = delayed_auto_correlation(audio_password)
print("\nDelayed Auto-correlation of input signal:")

# 3. Cross correlation of input signal and delayed input signal
q = cross_correlation(audio_password, np.roll(audio_password, 1))
print("\nCross-correlation of input signal and delayed input signal:")

# 4. Cross correlation of input signal and scaled input signal
a = 2.0
s = scaled_cross_correlation(audio_password, a)
print("\nCross-correlation of input signal and scaled input signal with a =", a)

# Audio Authentication Example
authenticated = audio_authentication(audio_password, test_audio_password)
print("\nAudio Authentication Result:", authenticated)