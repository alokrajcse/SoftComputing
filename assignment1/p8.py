import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -5 to 100
x = np.linspace(-5, 100, 200)

# Membership function: 1 if x < 20, else 0
mu_x = [1 if val < 20 else 0 for val in x]

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: Step Function (μx = 1 for x<20, else 0)")
plt.ylim(-0.1, 1.1)  # Keep y-axis between 0 and 1
plt.grid()
plt.show()
