import numpy as np

# Objective 1: Develop a program to perform FFT of N point Signal
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return np.concatenate([even + T, even - T])

# Objective 2: Calculate FFT of a given DT signal and verify the results using mathematical formula
def verify_fft(x):
    X_fft = fft(x)
    X_math = np.fft.fft(x)

    # Check if the results match using numpy's fft
    np.testing.assert_allclose(X_fft, X_math, rtol=1e-10)

    # Compute the inverse FFT to get back x[n]
    x_ifft = np.fft.ifft(X_fft)

    # Check if the inverse FFT recovers the original signal
    np.testing.assert_allclose(x, x_ifft, rtol=1e-10)

    return X_fft

# Objective 3: Computational efficiency of FFT
def compute_complexity(N):
    # FFT involves log2(N) stages, each with N/2 butterflies
    num_stages = int(np.log2(N))
    num_butterflies = N // 2
    total_complexity = num_stages * num_butterflies

    return num_stages, num_butterflies, total_complexity

# Problem Definition
# (1) Take any four-point sequence x[n].
x = np.array([1, 2, 3, 4])

# Find FFT of x[n] and IFFT of {X[k]}.
X_fft = verify_fft(x)

# (2) Calculate Real and Complex Additions & Multiplications involved to find X[k].
num_stages, num_butterflies, total_complexity = compute_complexity(len(x))
print("\nFFT Computational Complexity:")
print(f"Number of Stages: {num_stages}")
print(f"Number of Butterflies per Stage: {num_butterflies}")
print(f"Total Computational Complexity: {total_complexity}")

# Display the results
print("\nResults:")
print("Original Signal x[n]:", x)
print("FFT Result X[k]:", X_fft)

