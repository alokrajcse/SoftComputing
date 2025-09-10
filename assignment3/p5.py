import numpy as np

# Triangular membership function
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    return 0

# Define fuzzy set A on X = [0, 10]
X = np.linspace(0, 10, 11)
A = [(x, triangular(x, 0, 5, 10)) for x in X]

# Cylindrical extension into X × Y, where Y = {0,1,2,3}
Y = [0, 1, 2, 3]
A_cylindrical = [((x, y), mu) for x, mu in A for y in Y]

# Print fuzzy set A
print("Fuzzy set A:")
for x, mu in A:
    print(f"A({x}) = {mu:.2f}")

# Print cylindrical extension
print("\nCylindrical Extension of A in X × Y:")
for (x, y), mu in A_cylindrical:
    print(f"A_cyl({x}, {y}) = {mu:.2f}")
