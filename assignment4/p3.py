import numpy as np
import matplotlib.pyplot as plt

# Define fuzzy relations
def R1(x, y):
    return np.exp(-((x - y) ** 2) / (1.5 ** 2))

def R2(y, z):
    return np.exp(-((y - z) ** 2) / (2.0 ** 2))

# Universe of discourse
X = np.linspace(0, 10, 50)  # values for x
Y = np.linspace(0, 10, 50)  # values for y
Z = np.linspace(0, 10, 50)  # values for z

# Max-Min composition (R1 o R2)(x,z)
R_comp = np.zeros((len(X), len(Z)))

for i, x in enumerate(X):
    for k, z in enumerate(Z):
        # For each y, take min(R1(x,y), R2(y,z)), then max over y
        vals = [min(R1(x, y), R2(y, z)) for y in Y]
        R_comp[i, k] = max(vals)

# ---- Visualization ----
plt.figure(figsize=(6,5))
plt.imshow(R_comp, extent=[Z.min(), Z.max(), X.min(), X.max()],
           origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(label="Membership Value")
plt.xlabel("z")
plt.ylabel("x")
plt.title("Max-Min Composition: R1 o R2")
plt.show()
