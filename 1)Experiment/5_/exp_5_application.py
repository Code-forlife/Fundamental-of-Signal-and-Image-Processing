import numpy as np
from scipy.io import wavfile
from scipy.signal import firwin, lfilter
import matplotlib.pyplot as plt

# Function to filter audio signal
def apply_filter(audio_signal, filter_coefficients):
    filtered_signal = lfilter(filter_coefficients, 1.0, audio_signal)
    return filtered_signal

# Step 1: Record Audio in the presence of noise with Fs = 8000 Hz ==> x[n]
# Assuming you have an audio file. Replace 'noisy_audio.wav' with the actual file path.
sample_rate, audio_signal = wavfile.read('file1.wav')

# Step 2: Play the recorded signal x[n] and observe the quality of sound.
plt.plot(audio_signal)
plt.title('Original Audio Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

# Step 3: Design FIR Low Pass Filter using MATLAB filter design Tool.
# Take Fpass = 2000Hz, Fstop = 3000Hz, Fs = 8000
Fpass = 2000  # Passband frequency in Hz
Fstop = 3000  # Stopband frequency in Hz
Fs = sample_rate  # Sampling frequency
filter_order = 101  # Adjust the filter order as needed

# Design FIR Low Pass Filter
filter_coefficients = firwin(filter_order, cutoff=Fpass, fs=Fs, pass_zero=True)

# Step 4: Filter the audio signal x[n]
filtered_signal = apply_filter(audio_signal, filter_coefficients)

# Save the filtered audio signal to a file
wavfile.write('file1.wav', sample_rate, np.int16(filtered_signal))

# Display a plot of the original and filtered signals
plt.plot(audio_signal, label='Original Signal')
plt.plot(filtered_signal, label='Filtered Signal')
plt.title('Audio Signal Filtering')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Download the filtered audio file
from google.colab import files
files.download('file1.wav')
