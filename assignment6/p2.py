import random

# ----- Step 1: Initialize population -----
# Let's take population size = 6 (you can change it)
population_size = 6

# Generate random population (values between 0 and 31)
population = [random.randint(0, 31) for _ in range(population_size)]

# Convert each value to 5-bit binary representation
binary_population = [format(x, '05b') for x in population]

print("Initial Population (Binary):", binary_population)
print("Decimal Values:", population)

# ----- Step 2: Objective Function -----
def fitness(x):
    return x**2  # f(x) = x^2

# Calculate fitness values
fitness_values = [fitness(x) for x in population]
print("Fitness Values:", fitness_values)

# ----- Step 3: Roulette Wheel Selection -----
def roulette_wheel_selection(pop, fitness_vals):
    total_fitness = sum(fitness_vals)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness_vals):
        current += f
        if current > pick:
            return pop[i]

# ----- Step 4: Generate Next Generation -----
# Select same number of chromosomes as the population size
next_generation = [roulette_wheel_selection(population, fitness_values) for _ in range(population_size)]

# Convert to binary for display
binary_next_gen = [format(x, '05b') for x in next_generation]

print("\nNext Generation (Decimal):", next_generation)
print("Next Generation (Binary):", binary_next_gen)
