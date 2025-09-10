import numpy as np
import matplotlib.pyplot as plt

# Membership functions
def mu_A(x):
    return max(0, min(1, (x - 20) / 30))

def mu_B(x):
    return max(0, min(1, (80 - x) / 30))

# Operations
def algebraic_sum(a, b):
    return a + b - a * b

def algebraic_product(a, b):
    return a * b

def bounded_sum(a, b):
    return min(1, a + b)

def bounded_product(a, b):
    return max(0, a + b - 1)

def bounded_difference(a, b):
    return max(0, a - b)

# Evaluate over domain [0,10]
xs = np.linspace(0, 10, 100)
A_vals = [mu_A(x) for x in xs]
B_vals = [mu_B(x) for x in xs]

alg_sum = [algebraic_sum(mu_A(x), mu_B(x)) for x in xs]
alg_prod = [algebraic_product(mu_A(x), mu_B(x)) for x in xs]
bnd_sum = [bounded_sum(mu_A(x), mu_B(x)) for x in xs]
bnd_prod = [bounded_product(mu_A(x), mu_B(x)) for x in xs]
bnd_diff = [bounded_difference(mu_A(x), mu_B(x)) for x in xs]

# Plot results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.plot(xs, A_vals, label="A")
plt.plot(xs, B_vals, label="B")
plt.title("Original Sets A & B")
plt.legend()

plt.subplot(2,3,2)
plt.plot(xs, alg_sum, 'r')
plt.title("Algebraic Sum")

plt.subplot(2,3,3)
plt.plot(xs, alg_prod, 'g')
plt.title("Algebraic Product")

plt.subplot(2,3,4)
plt.plot(xs, bnd_sum, 'm')
plt.title("Bounded Sum")

plt.subplot(2,3,5)
plt.plot(xs, bnd_prod, 'c')
plt.title("Bounded Product")

plt.subplot(2,3,6)
plt.plot(xs, bnd_diff, 'y')
plt.title("Bounded Difference")

plt.tight_layout()
plt.show()
