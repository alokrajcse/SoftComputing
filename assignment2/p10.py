# Fuzzy sets A and B as dictionaries (x: μ(x))
A = {1: 1.0, 2: 0.8, 3: 0.0, 4: 0.5, 5: 0.7}
B = {1: 0.6, 2: 1.0, 3: 0.9, 4: 0.0, 5: 0.4}

def drastic_product(a, b):
    if b == 1:
        return a
    elif a == 1:
        return b
    else:
        return 0

def drastic_sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return 1

print("x   A(x)   B(x)   Drastic Product   Drastic Sum")
print("------------------------------------------------")

for x in A:
    a, b = A[x], B[x]
    print(f"{x}   {a:.1f}    {b:.1f}        {drastic_product(a,b):.1f}              {drastic_sum(a,b):.1f}")
