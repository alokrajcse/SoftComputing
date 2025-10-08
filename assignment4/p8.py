def sugeno_measure(membership_values, lambda_value):
    measures = []
    for mu in membership_values:
        # Sugeno measure formula: g(x) = mu / (1 + lambda * (1 - mu))
        g = mu / (1 + lambda_value * (1 - mu))
        measures.append(round(g, 4))
    return measures


# Given data
membership_values = [0.0, 0.25, 0.5, 0.75, 1.0]
lambda_value = 0.5

result = sugeno_measure(membership_values, lambda_value)

print("Membership Values:", membership_values)
print("Sugeno Measures  :", result)