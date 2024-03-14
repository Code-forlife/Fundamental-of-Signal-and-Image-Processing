import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt

# Function to calculate energy spectral density
def calculate_energy_spectral_density(signal):
    _, _, Sxx = spectrogram(signal)
    return Sxx

# Function to calculate coefficient of correlation
def calculate_coefficient_of_correlation(X, Y):
    numerator = np.sum(X * Y)
    denominator = np.sqrt(np.sum(X**2) * np.sum(Y**2))
    return numerator / denominator

# Step 1: Record Audio Password and filter the noise è x[n]
# Assuming you have an audio file. Replace 'audio_password.wav' with the actual file path.
sample_rate, audio_password = wavfile.read('test_password.wav')

# Step 2: Record Test Audio Password and filter the noise è y[n]
# Assuming you have a test audio file. Replace 'test_audio_password.wav' with the actual file path.
_, test_audio_password = wavfile.read('test_password.wav')

# Step 3: Calculate X[k] and Y[k] using FFT
X = np.fft.fft(audio_password)
Y = np.fft.fft(test_audio_password)

# Step 4: Calculate |X[k]|^2 and |Y[k]|^2 (Energy Spectral Density)
ESD_X = np.abs(X)**2
ESD_Y = np.abs(Y)**2

# Step 5: Calculate Coefficient of Correlation of |X[k]|^2 and |Y[k]|^2 ==> r
correlation_coefficient = calculate_coefficient_of_correlation(ESD_X, ESD_Y)
print(f"Coefficient of Correlation: {correlation_coefficient}")

# Step 6: Authenticate the user by selecting an appropriate Threshold value (e.g., > 0.9)
threshold = 0.9
if correlation_coefficient > threshold:
    print("Authentication successful.")
else:
    print("Authentication failed.")
