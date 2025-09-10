import numpy as np
import matplotlib.pyplot as plt

# Generate x values between -5 and 5
x = np.linspace(-5, 5, 200)

# Membership function μx = (1 - e^(-x)) / (1 + e^(-x))
mu_x = (1 - np.exp(-x)) / (1 + np.exp(-x))

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: μx = (1 - e^(-x)) / (1 + e^(-x))")
plt.grid()
plt.show()

