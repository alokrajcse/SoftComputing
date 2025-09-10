import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -5 to 100
x = np.linspace(-5, 100, 200)

# Membership function: 0 if x <= 20, else 1
mu_x = [0 if val <= 20 else 1 for val in x]

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: Step Function at x=20")
plt.ylim(-0.1, 1.1)  # keep y-axis between 0 and 1
plt.grid()
plt.show()
