def sugeno_measure(fuzzy_set, lambda_value):
    measures = {}
    for x, mu in fuzzy_set:
        g = mu / (1 + lambda_value * (1 - mu))
        measures[x] = round(g, 4)
    return measures


# Given fuzzy set
fuzzy_set = [("x1", 0.2), ("x2", 0.5), ("x3", 0.7), ("x4", 0.9), ("x5", 1.0)]
lambda_value = 0.2

result = sugeno_measure(fuzzy_set, lambda_value)

print("Fuzzy Set A:", fuzzy_set)
print("Sugeno Measures:")
for x, g in result.items():
    print(f"{x}: {g}")