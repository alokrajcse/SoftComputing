# Fuzzy sets represented as dictionaries
A = {"x1": 0.7, "x2": 0.8, "x3": 0.5, "x4": 1.0, "x5": 0.6}
B = {"x1": 0.5, "x2": 0.6, "x3": 0.3, "x4": 0.9, "x5": 0.4}

def is_fuzzy_subset(A, B):
    for key in B:
        if B[key] > A.get(key, 0):  # if B's value > A's value
            return False
    return True

# Check if A contains B
if is_fuzzy_subset(A, B):
    print("A contains B (B is a fuzzy subset of A).")
else:
    print("A does not contain B.")

