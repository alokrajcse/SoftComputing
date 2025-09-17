# Define fuzzy sets
A = {"x1": 0.2, "x2": 0.7, "x3": 1.0, "x4": 0.4}
B = {"x1": 0.5, "x2": 0.6, "x3": 0.8, "x4": 0.9}

# T-conorm operators
def Smax(a, b):
    return max(a, b)

def Sas(a, b):
    return a + b - a * b

def Sbs(a, b):
    return min(1, a + b)

def Sds(a, b):
    if b == 0: return a
    if a == 0: return b
    return 1  # if both > 0

# Apply T-conorms
print("x\tA(x)\tB(x)\tSmax\tSas\tSbs\tSds")
for x in A.keys():
    a, b = A[x], B[x]
    print(f"{x}\t{a:.1f}\t{b:.1f}\t{Smax(a,b):.2f}\t{Sas(a,b):.2f}\t{Sbs(a,b):.2f}\t{Sds(a,b):.2f}")
