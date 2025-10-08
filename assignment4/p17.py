# Define fuzzy sets
X = ['a', 'b', 'c', 'd']
Y = [1, 2, 3, 4]

A = {'a': 0, 'b': 0.8, 'c': 0.6, 'd': 1}
B = {1: 0.2, 2: 1, 3: 0.8, 4: 0}
C = {1: 0, 2: 0.4, 3: 1, 4: 0.8}

# Assume fact: x is A' (take A itself as A' for this example)
A_prime = A.copy()

# Compute conclusion B'
B_prime = {}

for y in Y:
    values = []
    for x in X:
        # Rule 1: if x is A -> y is B
        rule1 = min(A_prime[x], B[y])
        # Rule 2: else y is C
        rule2 = min(1 - A_prime[x], C[y])
        values.append(max(rule1, rule2))
    B_prime[y] = max(values)

# Print conclusion set
print("Conclusion B':")
for y in Y:
    print(f"y = {y}, μB'(y) = {B_prime[y]:.2f}")
