# Define fuzzy sets
X = ['a', 'b', 'c', 'd']
Y = [1, 2, 3, 4]

A = {'a': 0, 'b': 0.8, 'c': 0.6, 'd': 1}
B = {1: 0.2, 2: 1, 3: 0.8, 4: 0}

# Compute conclusion B'
B_prime = {}

for y in Y:
    values = []
    for x in X:
        values.append(min(A[x], B[y]))
    B_prime[y] = max(values)

# Print conclusion set
print("Conclusion B':")
for y in Y:
    print(f"y = {y}, μB'(y) = {B_prime[y]:.2f}")
