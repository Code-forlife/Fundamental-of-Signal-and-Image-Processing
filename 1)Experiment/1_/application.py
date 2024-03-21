# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import sounddevice as sd
import warnings
warnings.filterwarnings("ignore")

fs, audio_data = wavfile.read("Experiment 1\Codes\sample.wav")
print("Sampling rate: ", fs)
print("Audio duration: ", audio_data.shape[0] / fs, "seconds")
print("No. of Samples: ", audio_data.shape[0])

# playing the audio
print("Playing the original audio...")
sd.play(audio_data, fs)
sd.wait()

# adding noise to the audio
noise = np.random.normal(0, 1, audio_data.shape)
noisy_signal = audio_data + noise

print("Playing the original signal with noise...")
sd.play(noisy_signal, fs)
sd.wait()

# save the noisy signal
wavfile.write("Experiment 1\Codes\\noisy_signal.wav", fs, noisy_signal.astype(np.int16))

# Function to design FIR Low Pass Filter
def design_low_pass_filter(Fpass, Fstop, Fs):
    nyquist = 0.5 * Fs
    Fpass_normalized = Fpass / nyquist
    Fstop_normalized = Fstop / nyquist
    taps = 101  # Adjust the number of taps as needed
    coefficients = signal.firwin(taps, cutoff=Fpass_normalized, window="hamming")
    return coefficients

# Function to filter audio signal using linear convolution
def filter_audio_signal(x, h):
    # convert to 1D array
    x = np.array(x).flatten()
    h = np.array(h).flatten()
    y = np.convolve(x, h, mode="same")
    return y.astype(np.int16)

# Function to plot audio
def plot_audio(audio_data, fs):
    plt.figure(figsize=(10, 4))
    plt.plot(np.arange(len(audio_data)) / fs, audio_data)
    plt.title("Audio Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

# Define parameters
Fpass = 4000  # Passband frequency in Hz
Fstop = 6000  # Stopband frequency in Hz
Fs = 44000  # Sampling frequency in Hz

plot_audio(noisy_signal, fs)

# Design FIR Low Pass Filter
h = design_low_pass_filter(Fpass, Fstop, Fs)

# Filter the audio signal using linear convolution
filtered_audio = filter_audio_signal(audio_data, h)
plot_audio(filtered_audio, fs)
wavfile.write("Experiment 1\Codes\\filtered_audio.wav", fs, filtered_audio)

print("Playing the filtered signal...")
sd.play(filtered_audio, fs)
sd.wait()
