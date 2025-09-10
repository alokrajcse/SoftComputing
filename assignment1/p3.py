import numpy as np
import matplotlib.pyplot as plt

# Generate x values between 0 and 10
x = np.linspace(0, 10, 100)  # 100 points for smooth curve

# Membership function μx = x / 10
mu_x = x / 10

# Plot
plt.plot(x, mu_x)
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Continuous Fuzzy Set: μx = x/10")
plt.ylim(0, 1)  # Membership values always between 0 and 1
plt.grid()
plt.show()
