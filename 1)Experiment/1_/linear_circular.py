import numpy as np


def circular_convolution(x, h):
    l = len(x)
    m = len(h)
    n = max(l, m)
    y = np.zeros(n)
    for i in range(l):
        for j in range(m):
            y[i] += x[(i-j) % l] * h[j]
    return y


def linear_convolution(x, h):
    l = len(x)
    m = len(h)
    n = l+m-1
    x = np.append(x, np.zeros(n-l))
    h = np.append(h, np.zeros(n-m))
    y = circular_convolution(x, h)
    return y


if __name__ == "__main__":
    x = list(map(float, input("x[n]: ").split()))
    h = list(map(float, input("h[n]: ").split()))
    y = linear_convolution(x, h)
    print('\nLinear convolution using circular convolution is:  ', y)