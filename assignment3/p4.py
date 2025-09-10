# Fuzzy set A on X
A = {'a': 1.0, 'b': 0.6, 'c': 0.4, 'd': 0.3}

# Fuzzy relation R (X → Y)
R = {
    ('a', 'u'): 0.9,
    ('b', 'u'): 0.7,
    ('c', 'v'): 0.5,
    ('d', 'v'): 1.0
}

# Target fuzzy set B' on Y
Y = ['u', 'v']
B_prime = {}


for y in Y:
    values = []
    for x in A:
        if (x, y) in R:
            values.append(min(A[x], R[(x, y)]))
    B_prime[y] = max(values) if values else 0.0

# Print result
print("Fuzzy set B':")
for y, mu in B_prime.items():
    print(f"{y}: {mu:.2f}")
