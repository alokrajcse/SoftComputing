import math

# Membership function for fuzzy set A
def mu_A(x):
    return math.exp(-((x - 3) ** 2) / 2)

# Complement membership function
def mu_A_complement(x):
    return 1 - mu_A(x)

# Generate values for x from 0 to 10
for x in range(0, 11):
    print(f"x = {x}, μA(x) = {mu_A(x):.4f}, μA'(x) = {mu_A_complement(x):.4f}")
