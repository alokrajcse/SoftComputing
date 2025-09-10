import numpy as np
import matplotlib.pyplot as plt

# Sigmoid membership function parameters
a = 1   # slope
c = 0   # center

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 300)

# Calculate membership values
mu_x = 1 / (1 + np.exp(-a * (x - c)))

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Sigmoid Membership Function: μx = 1 / (1 + e^{-a(x - c)})")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
