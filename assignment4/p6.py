# Define fuzzy set A
A = {"x1": 0.2, "x2": 0.5, "x3": 0.7, "x4": 0.9, "x5": 1.0}

# Compute complement
A_complement = {x: 1 - mu for x, mu in A.items()}

# Print results
print("x\tA(x)\tA_complement(x)")
for x in A.keys():
    print(f"{x}\t{A[x]:.1f}\t{A_complement[x]:.1f}")
