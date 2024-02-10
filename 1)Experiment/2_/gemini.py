import librosa
import sounddevice as sd
import scipy.io.wavfile as wav
import pickle
import numpy as np
import fastdtw

# ---------------------- Configuration ---------------------
FS = 16000  # Sampling frequency
RECORDING_DURATION = 2  # Recording time in seconds
MFCC_COEFFICIENTS = 13  # Number of MFCC features to extract 
TEMPLATE_FILE = 'user_template.pickle'
DISTANCE_THRESHOLD = 0.5  # Adjust as needed for verification

# --------------------- Helper Functions -------------------
def record_audio():
    """Records audio from the microphone."""
    print("Start speaking your password...")
    recording = sd.rec(int(RECORDING_DURATION * FS), samplerate=FS, channels=1)
    sd.wait()  # Wait for recording to finish
    print("Recording complete.")
    return recording, FS

def extract_mfccs(audio, fs):
    """Extracts Mel-Frequency Cepstral Coefficients (MFCCs)."""
    mfccs = librosa.feature.mfcc(y=audio, sr=fs, n_mfcc=MFCC_COEFFICIENTS)
    return mfccs

def enroll_user():
    """Enrolls a new user by creating a voice template."""
    audio, fs = record_audio()
    mfccs = extract_mfccs(audio, fs)

    with open(TEMPLATE_FILE, 'wb') as f:
        pickle.dump(mfccs, f)
    print("Enrollment template saved.")

def verify_user():
    """Verifies a user based on their stored voice template."""
    try:
        with open(TEMPLATE_FILE, 'rb') as f:
            authorized_template = pickle.load(f)
    except FileNotFoundError:
        print("No enrollment template found. Please enroll first.")
        return

    audio, fs = record_audio()
    verification_mfccs = extract_mfccs(audio, fs)

    distance = fastdtw(verification_mfccs.T, authorized_template.T).normalizedDistance

    if distance < DISTANCE_THRESHOLD:
        print('Access Granted')
    else:
        print('Access Denied')

# -------------------------- Main Logic ----------------------
if __name__ == "__main__":
    while True:
        choice = input("Choose an action (enroll / verify / exit): ").lower()

        if choice == 'enroll':
            enroll_user()
        elif choice == 'verify':
            verify_user()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice.")
