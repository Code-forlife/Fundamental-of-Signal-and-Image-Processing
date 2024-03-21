import numpy as np

def auto_correlation(x):
    l = len(x)
    h = x[::-1]
    m = len(h)
    n = l + m - 1
    y = np.zeros(n)
    for i in range(l):
        for j in range(m):
            y[i + j] += x[i] * h[j]
    return y

def cross_correlation(x, h):
    l = len(x)
    m = len(h)
    n = l + m - 1
    y = np.zeros(n)
    h = h[::-1]
    for i in range(l):
        for j in range(m):
            y[i + j] += x[i] * h[j]
    return y

def energy(signal):
    return np.sum(np.abs(signal) ** 2)

# Input Signals
x = list(map(float, input("Enter the input sequence x(n): ").split()))
a = 2

# Task 1: Auto-correlation of input signal
y = auto_correlation(x)
print("Auto-correlation of x[n]:", y)

# Significance of y[0]
y_0_significance = "Even" if y[0] % 2 == 0 else "Odd"
print("Significance of y[0]:", y_0_significance)

# Energy of the signal
signal_energy = energy(y)
print("Energy of the signal:", signal_energy)

# Task 2: Auto-correlation of delayed input signal
p = auto_correlation([0]+x)
print("\nAuto-correlation of p[n]:", p)

# Compare p[n] with y[n]
if np.array_equal(p, y):
    print("Conclusion: p[n] is equal to y[n]")
else:
    print("Conclusion: p[n] is not equal to y[n]")

# Task 3: Cross-correlation of input signal and delayed input signal
q = cross_correlation(x+[0], [0]+x)
print("\nCross-correlation of q[n]:", q)

# Compare q[n] with p[n] and y[n]
if np.array_equal(q, p) and np.array_equal(q, y):
    print("Conclusion: q[n] is equal to p[n] and y[n]")
else:
    print("Conclusion: q[n] is not equal to p[n] or y[n]")

# Task 4: Cross-correlation of input signal and scaled input signal
s = cross_correlation(x+[0, 0], [0, 0]+x)
print("\nCross-correlation of s[n]:", s)

# Compare s[n] with y[n]
if np.array_equal(s, y):
    print("Conclusion: s[n] is equal to y[n]")
else:
    print("Conclusion: s[n] is not equal to y[n]")
