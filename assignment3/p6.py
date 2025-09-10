import numpy as np

# 2D Gaussian membership function
def gaussian_2d(x, y, cx, sx, cy, sy):
    return np.exp(-(((x - cx) ** 2) / (2 * sx ** 2) + ((y - cy) ** 2) / (2 * sy ** 2)))

# Parameters
cx, sx = 5, 1.5
cy, sy = 5, 2.0

# Domain
X = np.linspace(0, 10, 11)   # 0 to 10
Y = np.linspace(0, 10, 11)

# Fuzzy set A in 2D
A = [((x, y), gaussian_2d(x, y, cx, sx, cy, sy)) for x in X for y in Y]

# Projection of A onto X-axis
proj_X = []
for x in X:
    mu_values = [gaussian_2d(x, y, cx, sx, cy, sy) for y in Y]
    proj_X.append((x, max(mu_values)))

# Print results
print("Projection of 2D Gaussian fuzzy set A onto X-axis (1D):")
for x, mu in proj_X:
    print(f"x={x:.1f}, μ_proj(x)={mu:.4f}")
