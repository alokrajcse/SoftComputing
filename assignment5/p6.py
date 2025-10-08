# Fuzzy set given as (x, membership)
A = [(1, 0.1), (2, 0.5), (3, 0.9), (4, 0.9), (5, 0.7)]

# --------- Center of Gravity (CoG) / Center of Area (CoA) ---------
numerator = sum(x * mu for x, mu in A)
denominator = sum(mu for _, mu in A)
CoG = numerator / denominator if denominator != 0 else None

# --------- Center of Sum (CoS) ---------
# If we had multiple sets, we'd sum their memberships.
# For single fuzzy set A, CoS = CoG
CoS = CoG  

# --------- Center of Area (CoA) ---------
# For discrete set, CoA = CoG
CoA = CoG  

print("Fuzzy Set A:", A)
print("Center of Gravity (CoG):", CoG)
print("Center of Sum (CoS):", CoS)
print("Center of Area (CoA):", CoA)
