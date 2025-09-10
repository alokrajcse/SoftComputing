import numpy as np
import matplotlib.pyplot as plt

# LR-Type parameters
c = 0      # center
alpha = 5  # left spread
beta = 5   # right spread

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 300)

# Membership function calculation
mu_x = []
for val in x:
    if val <= c:
        y = (c - val) / alpha
        mu_x.append(max(0, 1 - y))  # Left function L(y)
    else:
        y = (val - c) / beta
        mu_x.append(max(0, 1 - y))  # Right function R(y)

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("LR-Type Membership Function: c=0, α=5, β=5")
plt.ylim(0, 1.1)
plt.grid()
plt.show()
