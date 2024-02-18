def circular_convolution(x, h):
    # Determine the length of the resulting circular convolution
    N = max(len(x), len(h))

    # Pad the signals with zeros to make their lengths equal to N
    x_change = x + [0] * (N - len(x))
    h_change = h + [0] * (N - len(h))

    # Perform circular convolution
    y = []
    for i in range(N):
        conv_sum = 0
        for j in range(N):
            conv_sum += x_change[j] * h_change[(i - j) % N]
        y.append(conv_sum)

    return y


x_length = int(input("Enter the length of signal x: "))
h_length = int(input("Enter the length of signal h: "))

# Take user input for the values of signal x
x = []
print("Enter the values of signal x:")
for i in range(x_length):
    value = float(input(f"x[{i}]: "))
    x.append(value)

# Take user input for the values of signal h
h = []
print("Enter the values of signal h:")
for i in range(h_length):
    value = float(input(f"h[{i}]: "))
    h.append(value)


result = circular_convolution(x, h)
print("Circular convolution result:", result)
