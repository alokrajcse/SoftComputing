import numpy as np
import matplotlib.pyplot as plt

# Define domain
x = np.linspace(0, 10, 1000)

# Membership functions
mu_A = np.minimum(1, x / 5)
mu_B = np.maximum(1, (5 - x) / 5)

# Complement operations
mu_A_complement = 1 - mu_A
mu_B_complement = 1 - mu_B

# Plotting
plt.figure(figsize=(12, 6))

# Original Sets
plt.subplot(1, 2, 1)
plt.plot(x, mu_A, label='μA(x)', color='blue')
plt.plot(x, mu_B, label='μB(x)', color='green')
plt.title('Original Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)

# Complements
plt.subplot(1, 2, 2)
plt.plot(x, mu_A_complement, label='Complement of A', color='red')
plt.plot(x, mu_B_complement, label='Complement of B', color='orange')
plt.title('Complement of Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()