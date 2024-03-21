import numpy as np
import matplotlib.pyplot as plt
import time

def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = fft(x[0::2])
    odd = fft(x[1::2])

    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]

    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x

    even = ifft(x[0::2])
    odd = ifft(x[1::2])

    T = [np.exp(2j * np.pi * k / N) * odd[k] for k in range(N // 2)]

    return [(even[k] + T[k]) / 2 for k in range(N // 2)] + [(even[k] - T[k]) / 2 for k in range(N // 2)]  

def fft_with_count(x):
    global complex_additions, complex_multiplications
    N = len(x)
    if N <= 1:
        return x

    even = fft_with_count(x[0::2])
    odd = fft_with_count(x[1::2])

    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    
    for k in range(N // 2):
        complex_additions += 2  
        complex_multiplications += 1  

    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def calculate_complexity(N):
    # For FFT, number of complex additions = N * log2(N)
    # Number of complex multiplications is the same as additions
    complex_additions = N * np.log2(N)
    complex_multiplications = complex_additions
    return complex_additions, complex_multiplications

# User Input
N = int(input("Enter the length of the signal (N): "))
x = []
for i in range(N):
    val = float(input(f"Enter the value of x[{i}]: "))
    x.append(val)

# FFT
start_time = time.time()
X = fft(x)
fft_time = time.time() - start_time

# DFT
start_time = time.time()
X_dft = dft(x)
dft_time = time.time() - start_time

# IFFT
x_iff = ifft(X)

# Print Magnitude of FFT output
print("Magnitude of FFT output:", np.abs(X))

# Plotting
plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
plt.stem(np.abs(x))
plt.title('Magnitude of x[n]')
plt.subplot(3,1,2)
plt.stem(np.abs(X))
plt.title('Magnitude of X[k] = FFT(x[n])')
plt.subplot(3,1,3)
plt.stem(np.abs(x_iff))
plt.title('Magnitude of x_ifft[n] = IFFT(X[k])')
plt.show()

# Operation Counts
complex_additions = 0
complex_multiplications = 0
signal = x
fft_result = fft_with_count(signal)
print("\nOperation Counts for FFT:")
print(f"Complex Additions: {complex_additions}")
print(f"Complex Multiplications: {complex_multiplications}")

# Print time comparison
print("\nTime Comparison:")
print(f"DFT time: {dft_time} seconds")
print(f"FFT time: {fft_time} seconds")
