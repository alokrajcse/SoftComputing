import numpy as np
import matplotlib.pyplot as plt

# Gaussian parameters
c = 0      # center
sigma = 2  # standard deviation (controls width)

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate membership values
mu_x = np.exp(-((x - c)**2) / (2 * sigma**2))

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Gaussian Membership Function: μx = e^(-(x - c)^2 / (2σ²))")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
