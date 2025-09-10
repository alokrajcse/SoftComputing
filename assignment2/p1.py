import numpy as np
import matplotlib.pyplot as plt

# Define domain
x = np.linspace(0, 10, 1000)

# Define membership functions
mu_A = np.minimum(1, x / 5)
mu_B = np.maximum(1, (5 - x) / 5)

# Fuzzy Union: max of memberships
mu_union = np.maximum(mu_A, mu_B)

# Fuzzy Intersection: min of memberships
mu_intersection = np.minimum(mu_A, mu_B)

# Plotting
plt.figure(figsize=(12, 6))

# Original Sets
plt.subplot(1, 2, 1)
plt.plot(x, mu_A, label='μA(x)', color='blue')
plt.plot(x, mu_B, label='μB(x)', color='green')
plt.title('Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)

# Union and Intersection
plt.subplot(1, 2, 2)
plt.plot(x, mu_union, label='Union (max)', color='purple')
plt.plot(x, mu_intersection, label='Intersection (min)', color='orange')
plt.title('Union and Intersection of A and B')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()