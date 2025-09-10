import numpy as np
import matplotlib.pyplot as plt

# Trapezoidal membership function parameters
a, b, c, d = 0, 3, 7, 10

# Generate x values from -5 to 15
x = np.linspace(-5, 15, 300)

# Compute membership values
mu_x = []
for val in x:
    if val <= a or val >= d:
        mu_x.append(0)
    elif a < val <= b:
        mu_x.append((val - a) / (b - a))  # rising slope
    elif b < val <= c:
        mu_x.append(1)  # top (flat) part
    elif c < val < d:
        mu_x.append((d - val) / (d - c))  # falling slope

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Trapezoidal Membership Function: trap(x; 0, 3, 7, 10)")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
