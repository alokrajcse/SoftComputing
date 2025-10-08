# Fuzzy set given as (x, membership)
A = [(1, 0.1), (2, 0.5), (3, 0.9), (4, 0.9), (5, 0.7)]

# Weighted Average Defuzzification
numerator = sum(x * mu for x, mu in A)
denominator = sum(mu for _, mu in A)

weighted_avg = numerator / denominator if denominator != 0 else None

print("Fuzzy Set A:", A)
print("Defuzzified value using Weighted Average Method:", weighted_avg)

