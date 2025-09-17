import numpy as np
import matplotlib.pyplot as plt

# Triangular membership function
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)

# Define fuzzy set A (universe [0,10])
X = np.linspace(0, 10, 100)   # x values
mu_A = np.array([triangular(x, 2, 5, 8) for x in X])

# Define fuzzy relation R(x,y) = exp(-((x-y)^2)/(1.5^2))
def R(x, y):
    return np.exp(-((x - y) ** 2) / (1.5 ** 2))

# Max-Min composition (A o R)(y)
Y = np.linspace(0, 10, 100)   # y values
mu_B = []   # result fuzzy set after composition

for y in Y:
    values = [min(mu_A[i], R(X[i], y)) for i in range(len(X))]
    mu_B.append(max(values))

mu_B = np.array(mu_B)

# ---- Plot results ----
plt.figure(figsize=(10,6))

plt.plot(X, mu_A, label="Fuzzy Set A", color="blue")
plt.plot(Y, mu_B, label="Composite (A o R)", color="red")
plt.xlabel("Universe of discourse")
plt.ylabel("Membership")
plt.title("Max-Min Composition of Fuzzy Set A with Relation R(x,y)")
plt.legend()
plt.grid(True)
plt.show()
