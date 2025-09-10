# Test pairs (a, b)
pairs = [(1, 0.6), (0.8, 1), (0.0, 0.9), (0.5, 0.0), (0.7, 0.4), (1, 1), (0, 0)]

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

print("   a     b   |  Drastic Product   Drastic Sum")
print("---------------------------------------------")

for a, b in pairs:
    print(f" {a:.1f}   {b:.1f}  |       {drastic_product(a,b):.1f}              {drastic_sum(a,b):.1f}")
