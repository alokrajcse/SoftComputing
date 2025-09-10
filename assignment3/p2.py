import numpy as np

# ----------------- Membership Functions -----------------
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    return 0

def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)
    return 0

def gaussian(x, c, sigma):
    return np.exp(-((x - c) ** 2) / (2 * sigma ** 2))

def bell(x, a, b, c):
    return 1 / (1 + abs((x - c) / a) ** (2 * b))

# ----------------- Core, Crossover, Bandwidth -----------------
def fuzzy_props(func, params, x_range):
    mu_values = [func(x, *params) for x in x_range]
    core = [x for x, mu in zip(x_range, mu_values) if np.isclose(mu, 1.0)]
    crossover = [x for x, mu in zip(x_range, mu_values) if np.isclose(mu, 0.5, atol=0.01)]
    positive_x = [x for x, mu in zip(x_range, mu_values) if mu > 0.0]
    bandwidth = max(positive_x) - min(positive_x) if positive_x else 0
    return core, crossover, bandwidth

# ----------------- Test with given sets -----------------
x_range = np.linspace(0, 100, 1001)  # step = 0.1 for smoothness

tri_core, tri_cross, tri_band = fuzzy_props(triangular, (20, 60, 80), x_range)
trap_core, trap_cross, trap_band = fuzzy_props(trapezoidal, (10, 20, 40, 70), x_range)
gauss_core, gauss_cross, gauss_band = fuzzy_props(gaussian, (5, 1.5), np.linspace(-5, 15, 1001))
bell_core, bell_cross, bell_band = fuzzy_props(bell, (1.5, 2, 5), np.linspace(-5, 15, 1001))

# ----------------- Print Results -----------------
print("Triangular (20,60,80):")
print(" Core:", tri_core, "Crossover:", tri_cross, "Bandwidth:", tri_band)

print("\nTrapezoidal (10,20,40,70):")
print(" Core:", trap_core, "Crossover:", trap_cross, "Bandwidth:", trap_band)

print("\nGaussian (5,1.5):")
print(" Core:", gauss_core, "Crossover:", gauss_cross, "Bandwidth:", gauss_band)

print("\nBell (1.5,2,5):")
print(" Core:", bell_core, "Crossover:", bell_cross, "Bandwidth:", bell_band)