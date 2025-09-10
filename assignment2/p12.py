import math

# Fuzzy set A
A = [0.0, 0.2, 0.5, 0.8, 1.0]

def concentration(mu):
    return mu ** 2

def dilation(mu):
    return math.sqrt(mu)

print(" x     μ(x)   Concentration   Dilation")
print("-----------------------------------------")

for mu in A:
    print(f"{mu:.1f}   {mu:.1f}       {concentration(mu):.3f}         {dilation(mu):.3f}")
