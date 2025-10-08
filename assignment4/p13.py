import math

# Parameter
p = 0.3

# Membership function for fuzzy set A
def mu_A(x):
    return math.exp(-((x - 3) ** 2) / 2)

# Yager's complement
def yager_complement(x):
    return (1 - (mu_A(x) ** p)) ** (1 / p)

# Compute values for x = 0 to 6
print("x\tμA(x)\tYager’s Complement")
for x in range(0, 7):
    mu = mu_A(x)
    yag = yager_complement(x)
    print(f"{x}\t{mu:.4f}\t{yag:.4f}")
