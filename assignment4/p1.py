import numpy as np

# Define relations as 3x3 matrices
R1 = np.array([[0.3, 0.7, 0.5],
               [0.9, 0.2, 0.4],
               [0.6, 0.8, 0.1]])

R2 = np.array([[0.5, 0.2, 0.9],
               [0.4, 0.6, 0.3],
               [0.7, 0.8, 0.5]])

# Max-Min Composite
def max_min(R1, R2):
    n, m = R1.shape
    m2, p = R2.shape
    result = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            result[i, j] = max(min(R1[i, k], R2[k, j]) for k in range(m))
    return result

# Max-Product Composite
def max_product(R1, R2):
    n, m = R1.shape
    m2, p = R2.shape
    result = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            result[i, j] = max(R1[i, k] * R2[k, j] for k in range(m))
    return result

# Max-Average Composite
def max_average(R1, R2):
    n, m = R1.shape
    m2, p = R2.shape
    result = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            result[i, j] = max((R1[i, k] + R2[k, j]) / 2 for k in range(m))
    return result


print("Relation1:\n", R1)
print("Relation2:\n", R2)

print("\nMax-Min Composite:\n", max_min(R1, R2))
print("\nMax-Product Composite:\n", max_product(R1, R2))
print("\nMax-Average Composite:\n", max_average(R1, R2))
