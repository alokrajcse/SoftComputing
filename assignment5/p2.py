# Given fuzzy sets
A = [0.2, 0.7, 0.9]
B = [0.3, 0.5, 0.8, 1.0]

# Lambda value
lam = 0.5

# Apply lambda-cut
A_lambda = [val for val in A if val >= lam]
B_lambda = [val for val in B if val >= lam]

# Defuzzification (centroid method)
defuzz_A = sum(A_lambda) / len(A_lambda) if A_lambda else None
defuzz_B = sum(B_lambda) / len(B_lambda) if B_lambda else None

print("Lambda-cut of A:", A_lambda)
print("Lambda-cut of B:", B_lambda)
print("Defuzzified value of A:", defuzz_A)
print("Defuzzified value of B:", defuzz_B)
