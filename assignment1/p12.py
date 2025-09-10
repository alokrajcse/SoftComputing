import numpy as np
import matplotlib.pyplot as plt

# Bell-shaped membership function parameters
a = 2   # width
b = 2   # slope
c = 0   # center

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate membership values
mu_x = 1 / (1 + np.abs((x - c) / a)**(2 * b))

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Bell-Shaped Membership Function: μx = 1 / (1 + |(x - c)/a|^(2b))")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
