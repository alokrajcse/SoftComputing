import numpy as np

# Membership function
def mu(x):
    return max(0, min(1, 1 - 0.1 * x - 5))

# Define range for x
x_values = np.linspace(0, 11, 100)  # 0 to 11 in 100 steps
mu_values = [mu(x) for x in x_values]

# Lambda-cut
lam = 0.7
lambda_cut = [x for x, m in zip(x_values, mu_values) if m >= lam]

# Defuzzification: centroid of lambda-cut
if lambda_cut:
    defuzz_value = sum(lambda_cut) / len(lambda_cut)
    print("Lambda-cut values:", lambda_cut)
    print("Defuzzified value (centroid):", defuzz_value)
else:
    print("No values satisfy lambda-cut.")
