import random

# ----- Step 1: Define two parent chromosomes -----
parent1 = "110101"
parent2 = "001110"

print("Parent 1:", parent1)
print("Parent 2:", parent2, "\n")

# ----- Step 2a: One-Point Crossover -----
def one_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)  # choose crossover point (not at ends)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    print(f"One-Point Crossover at {point}:")
    return child1, child2

# ----- Step 2b: Two-Point Crossover -----
def two_point_crossover(p1, p2):
    point1 = random.randint(1, len(p1) - 2)
    point2 = random.randint(point1 + 1, len(p1) - 1)
    child1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    child2 = p2[:point1] + p1[point1:point2] + p2[point2:]
    print(f"Two-Point Crossover between {point1} and {point2}:")
    return child1, child2

# ----- Step 2c: Uniform Crossover -----
def uniform_crossover(p1, p2):
    mask = [random.randint(0, 1) for _ in range(len(p1))]  # random mask
    child1 = ''.join([p1[i] if mask[i] == 1 else p2[i] for i in range(len(p1))])
    child2 = ''.join([p2[i] if mask[i] == 1 else p1[i] for i in range(len(p1))])
    print("Uniform Crossover Mask:", mask)
    return child1, child2

# ----- Step 3: Perform Crossovers -----
child1_1p, child2_1p = one_point_crossover(parent1, parent2)
print("Child 1:", child1_1p)
print("Child 2:", child2_1p, "\n")

child1_2p, child2_2p = two_point_crossover(parent1, parent2)
print("Child 1:", child1_2p)
print("Child 2:", child2_2p, "\n")

child1_uni, child2_uni = uniform_crossover(parent1, parent2)
print("Child 1:", child1_uni)
print("Child 2:", child2_uni)
