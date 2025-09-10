# Membership function for A
def A_membership(x):
    return max(0, 1 - 0.1 * abs(x - 5))

# Mapping f(x) = x + 3
def f(x):
    return x + 3

# Construct fuzzy set A
A = [(x, A_membership(x)) for x in range(0, 12)]

# Apply mapping to get fuzzy set B
B = [(f(x), mu) for x, mu in A]

# Print results
print("Fuzzy set A:")
for x, mu in A:
    print(f"A({x}) = {mu:.2f}")

print("\nFuzzy set B (after mapping f(x) = x+3):")
for y, mu in B:
    print(f"B({y}) = {mu:.2f}")
