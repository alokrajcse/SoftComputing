pairs = [(0.2, 0.7), (0.5, 0.5), (1.0, 0.3), (0.9, 1.0), (0.0, 0.8)]

def algebraic_sum(a, b):
    return a + b - a * b

def algebraic_product(a, b):
    return a * b

def bounded_sum(a, b):
    return min(1, a + b)

def bounded_product(a, b):
    return max(0, a + b - 1)

def bounded_difference(a, b):
    return max(0, a - b)


print(" a     b   |  Alg.Sum  Alg.Prod  Bnd.Sum  Bnd.Prod  Bnd.Diff")
print("------------------------------------------------------------")

for a, b in pairs:
    print(f"{a:.1f}   {b:.1f}  |   "
          f"{algebraic_sum(a,b):.3f}    "
          f"{algebraic_product(a,b):.3f}     "
          f"{bounded_sum(a,b):.3f}     "
          f"{bounded_product(a,b):.3f}      "
          f"{bounded_difference(a,b):.3f}")
