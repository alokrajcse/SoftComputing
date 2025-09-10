import numpy as np
import matplotlib.pyplot as plt

# Define domain
x = np.linspace(0.01, 10, 1000)  # Avoid division by zero at x=0

# Membership functions
mu_A = x / (x + 1)
mu_B = np.clip(2 - x, 0, 1)  # Ensure values stay within [0,1]

# Fuzzy operations
mu_union = np.maximum(mu_A, mu_B)
mu_intersection = np.minimum(mu_A, mu_B)
mu_union_complement = 1 - mu_union
mu_intersection_complement = 1 - mu_intersection

# Plotting
plt.figure(figsize=(14, 8))

# Original Sets
plt.subplot(2, 2, 1)
plt.plot(x, mu_A, label='μA(x) = x / (x + 1)', color='blue')
plt.plot(x, mu_B, label='μB(x) = 2 - x', color='green')
plt.title('Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)


plt.subplot(2, 2, 2)
plt.plot(x, mu_union, label='Union (max)', color='purple')
plt.plot(x, mu_intersection, label='Intersection (min)', color='orange')
plt.title('Union and Intersection')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)


plt.subplot(2, 2, 3)
plt.plot(x, mu_union_complement, label='Complement of Union', color='red')
plt.title('Complement of Union')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)


plt.subplot(2, 2, 4)
plt.plot(x, mu_intersection_complement, label='Complement of Intersection', color='brown')
plt.title('Complement of Intersection')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.ylim(0, 1.2)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()