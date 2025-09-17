# Define fuzzy sets as dictionaries
A = {"x1": 0.2, "x2": 0.7, "x3": 1.0, "x4": 0.4, "x5": 1.0, "x6": 0.0}
B = {"x1": 0.5, "x2": 0.6, "x3": 0.8, "x4": 0.9, "x5": 1.0, "x6": 0.0}

# T-norm operators
def Tmin(a, b):
    return min(a, b)

def Tap(a, b):
    return a * b

def Tbp(a, b):
    return max(0, a + b - 1)

def Tdp(a, b):
    if b == 1: return a
    if a == 1: return b
    return 0

# Apply T-norms
print("x\tA(x)\tB(x)\tTmin\tTap\tTbp\tTdp")
for x in A.keys():
    a, b = A[x], B[x]
    print(f"{x}\t{a:.1f}\t{b:.1f}\t{Tmin(a,b):.2f}\t{Tap(a,b):.2f}\t{Tbp(a,b):.2f}\t{Tdp(a,b):.2f}")
