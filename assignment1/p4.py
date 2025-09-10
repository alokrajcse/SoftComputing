import numpy as np
import matplotlib.pyplot as plt

# Generate x values between -5 and 5
x = np.linspace(-5, 5, 100)

# Membership function μx = |x| / 10
mu_x = np.abs(x) / 10

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: μx = |x|/10")
plt.ylim(0, 1)
plt.grid()
plt.show()
