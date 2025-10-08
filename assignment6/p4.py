import random

# ----- Step 1: Initialize population -----
population_size = 6  # You can change this
max_value = 31       # x ranges from 0 to 31

# Generate random population (values between 0 and 31)
population = [random.randint(0, max_value) for _ in range(population_size)]

# Convert each value to 5-bit binary representation
binary_population = [format(x, '05b') for x in population]

print("Initial Population (Binary):", binary_population)
print("Decimal Values:", population)

# ----- Step 2: Objective Function -----
def fitness(x):
    return (x + 1)**2  # f(x) = (x + 1)^2

# Calculate fitness values
fitness_values = [fitness(x) for x in population]
print("Fitness Values:", fitness_values)

# ----- Step 3: Rank-Based Selection -----
def rank_based_selection(pop, fitness_vals):
    # Sort population by fitness (ascending order)
    sorted_pop = sorted(list(zip(pop, fitness_vals)), key=lambda x: x[1])
    ranks = [i + 1 for i in range(len(sorted_pop))]  # Rank starts from 1

    total_rank = sum(ranks)
    pick = random.uniform(0, total_rank)
    current = 0

    for i, rank in enumerate(ranks):
        current += rank
        if current > pick:
            return sorted_pop[i][0]

# ----- Step 4: Generate Next Generation -----
next_generation = [rank_based_selection(population, fitness_values) for _ in range(population_size)]

# Convert to binary for display
binary_next_gen = [format(x, '05b') for x in next_generation]

print("\nNext Generation (Decimal):", next_generation)
print("Next Generation (Binary):", binary_next_gen)
