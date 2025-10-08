import math

# Parameters
sigma = 2
lambda_val = 0.7
p = 7

# Membership function (Gaussian)
def mu_A(x):
    return math.exp(- (x**2) / (2 * sigma**2))

# Complements
def standard_complement(x):
    return 1 - mu_A(x)

def sugeno_complement(x):
    return (1 - mu_A(x)) / (1 + lambda_val * mu_A(x))

def yager_complement(x):
    return (1 - (mu_A(x) ** p)) ** (1 / p)

# Compute for x = 0 to 6
print("x\tμA(x)\tStandard\tSugeno\t\tYager")
for x in range(0, 7):
    mu = mu_A(x)
    std_c = standard_complement(x)
    sug_c = sugeno_complement(x)
    yag_c = yager_complement(x)
    print(f"{x}\t{mu:.4f}\t{std_c:.4f}\t\t{sug_c:.4f}\t\t{yag_c:.4f}")
