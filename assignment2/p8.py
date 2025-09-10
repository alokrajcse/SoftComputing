import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(0, 10, 400)

# Define fuzzy sets A and B
mu_A = np.maximum(0, np.minimum(1, (5 - np.abs(x - 5)) / 3))
mu_B = np.exp(-((x - 7)**2) / (2 * (3**2)))

# ---- Fuzzy Operations ----
algebraic_sum = mu_A + mu_B - (mu_A * mu_B)
algebraic_product = mu_A * mu_B
bounded_sum = np.minimum(1, mu_A + mu_B)
bounded_product = np.maximum(0, mu_A + mu_B - 1)
bounded_difference = np.maximum(0, mu_A - mu_B)

# ---- Plotting ----
plt.figure(figsize=(10, 8))

plt.subplot(3, 2, 1)
plt.plot(x, mu_A, label="A")
plt.plot(x, mu_B, label="B")
plt.title("Fuzzy Sets A & B")
plt.legend()
plt.grid()

plt.subplot(3, 2, 2)
plt.plot(x, algebraic_sum, 'g')
plt.title("Algebraic Sum (A ⊕ B)")
plt.grid()

plt.subplot(3, 2, 3)
plt.plot(x, algebraic_product, 'r')
plt.title("Algebraic Product (A ⊗ B)")
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(x, bounded_sum, 'm')
plt.title("Bounded Sum (min(1, A+B))")
plt.grid()

plt.subplot(3, 2, 5)
plt.plot(x, bounded_product, 'c')
plt.title("Bounded Product (max(0, A+B-1))")
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(x, bounded_difference, 'y')
plt.title("Bounded Difference (max(0, A-B))")
plt.grid()

plt.tight_layout()
plt.show()
