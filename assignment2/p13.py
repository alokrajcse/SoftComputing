import numpy as np
import matplotlib.pyplot as plt

# Membership function
def mu_A(x):
    return max(0, min(1, 1 - np.exp(-0.1 * (x - 5))))

# Operations
def concentration(mu):
    return mu ** 2

def dilation(mu):
    return np.sqrt(mu)

# Domain
xs = np.linspace(0, 11, 200)
A_vals = [mu_A(x) for x in xs]
conc_vals = [concentration(mu) for mu in A_vals]
dil_vals = [dilation(mu) for mu in A_vals]

# Plot
plt.figure(figsize=(10,6))
plt.plot(xs, A_vals, label="Original μA(x)")
plt.plot(xs, conc_vals, label="Concentration (μ^2)")
plt.plot(xs, dil_vals, label="Dilation (√μ)")
plt.title("Concentration and Dilation of Fuzzy Set A")
plt.xlabel("x")
plt.ylabel("Membership μ(x)")
plt.legend()
plt.grid(True)
plt.show()
