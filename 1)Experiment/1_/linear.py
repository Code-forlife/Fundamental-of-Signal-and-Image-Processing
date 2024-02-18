def linear_convolution(x, h):
    # Length of the output signal
    output_length = len(x) + len(h) - 1
    # Initialize the output signal with zeros
    y = [0] * output_length

    # Perform linear convolution
    for n in range(output_length):
        for k in range(len(x)):
            if n - k >= 0 and n - k < len(h):
                y[n] += x[k] * h[n - k]

    return y


# Take user input for the lengths of signals x and h
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

print("x[n]: \n" , x)
print("h[n]: \n " ,h)
# Compute linear convolution
result = linear_convolution(x, h)
print("Linear convolution result:", result)
