import numpy as np
import matplotlib.pyplot as plt

# Triangular membership function parameters
a = 0   # left point
b = 5   # peak point
c = 10  # right point

# Generate x values from -5 to 15
x = np.linspace(-5, 15, 300)

# Compute membership values
mu_x = []
for val in x:
    if val <= a or val >= c:
        mu_x.append(0)
    elif a < val <= b:
        mu_x.append((val - a) / (b - a))  # rising edge
    elif b < val < c:
        mu_x.append((c - val) / (c - b))  # falling edge

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Triangular Membership Function: triangle(x; 0, 5, 10)")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
