# Fuzzy set A
A = [(0, 0.0), (1, 0.2), (2, 0.5), (3, 1.0), (4, 0.5), (5, 0.0)]

# Core: x values where μ(x) = 1
core = [x for x, mu in A if mu == 1.0]

# Crossover: x values where μ(x) = 0.5
crossover = [x for x, mu in A if mu == 0.5]

# Bandwidth: max(x) - min(x) where μ(x) > 0
x_values_with_membership = [x for x, mu in A if mu > 0]
bandwidth = max(x_values_with_membership) - min(x_values_with_membership)

# Output results
print("Core:", core)
print("Crossover:", crossover)
print("Bandwidth:", bandwidth)