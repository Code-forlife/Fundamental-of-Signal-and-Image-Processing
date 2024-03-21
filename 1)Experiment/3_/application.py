import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile  # Use this library to read audio file

# Step 1: Record Audio Password and filter the noise (Assuming you have an audio file)
# You can replace 'your_audio_file.wav' with the actual file path
sample_rate, audio_data = wavfile.read('test_password.wav')

# Step 2: Plot x[n]
plt.figure(figsize=(12, 4))
plt.plot(audio_data)
plt.title('Time Domain Representation of Audio Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

# Step 3: Transform Audio Signal x[n] from Time Domain to Frequency Domain using DFT
X = np.fft.fft(audio_data)

d# Step 4: Plot Magnitude Spectrum of X[k]
freq = np.fft.fftfreq(len(X), 1/sample_rate)  # Frequency axis
magnitude_spectrum = np.abs(X)

plt.figure(figsize=(12, 6))
plt.plot(freq, magnitude_spectrum)
plt.title('Magnitude Spectrum of Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()
