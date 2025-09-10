import numpy as np
import matplotlib.pyplot as plt

# Generate x values between -20 and 20
x = np.linspace(-20, 20, 200)

# Membership function μx = 1 / (1 + e^(-x))
mu_x = 1 / (1 + np.exp(-x))

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: μx = 1 / (1 + e^(-x))")
plt.ylim(0, 1)
plt.grid()
plt.show()
